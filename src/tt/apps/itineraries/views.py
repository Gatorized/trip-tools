from uuid import UUID

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from tt.apps.trips.context import TripPageContext
from tt.apps.trips.enums import TripPage
from tt.apps.trips.mixins import TripViewMixin
from tt.async_view import ModalView

from .forms import ItineraryItemForm
from .models import Itinerary, ItineraryItem


class ItinerariesHomeView( LoginRequiredMixin, TripViewMixin, View ):

    def get(self, request, trip_uuid: UUID, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_viewer( request_member )
        trip = request_member.trip

        itinerary, _ = Itinerary.objects.get_or_create(
            trip = trip,
            defaults = { 'title': trip.title },
        )
        items = itinerary.items.order_by( 'start_datetime' )

        trip_page_context = TripPageContext(
            active_page = TripPage.ITINERARY,
            request_member = request_member,
        )
        context = {
            'trip_page': trip_page_context,
            'itinerary': itinerary,
            'items': items,
        }
        return render(request, 'itineraries/pages/itineraries_home.html', context)


class ItineraryItemCreateModalView( LoginRequiredMixin, TripViewMixin, ModalView ):

    def get_template_name(self) -> str:
        return 'itineraries/modals/itinerary-item-create.html'

    def get(self, request, trip_uuid: UUID, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_editor( request_member )

        form = ItineraryItemForm()
        context = {
            'trip': request_member.trip,
            'form': form,
        }
        return self.modal_response( request, context = context )

    def post(self, request, trip_uuid: UUID, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_editor( request_member )
        trip = request_member.trip

        form = ItineraryItemForm( request.POST )
        if form.is_valid():
            itinerary, _ = Itinerary.objects.get_or_create(
                trip = trip,
                defaults = { 'title': trip.title },
            )
            with transaction.atomic():
                item = form.save( commit = False )
                item.itinerary = itinerary
                item.save()
            return self.refresh_response( request )

        context = {
            'trip': trip,
            'form': form,
        }
        return self.modal_response( request, context = context, status = 400 )


class ItineraryItemEditModalView( LoginRequiredMixin, TripViewMixin, ModalView ):

    def get_template_name(self) -> str:
        return 'itineraries/modals/itinerary-item-edit.html'

    def get(self, request, trip_uuid: UUID, item_id: int, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_editor( request_member )
        item = get_object_or_404(
            ItineraryItem, id = item_id, itinerary__trip = request_member.trip,
        )

        form = ItineraryItemForm( instance = item )
        context = {
            'trip': request_member.trip,
            'item': item,
            'form': form,
        }
        return self.modal_response( request, context = context )

    def post(self, request, trip_uuid: UUID, item_id: int, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_editor( request_member )
        item = get_object_or_404(
            ItineraryItem, id = item_id, itinerary__trip = request_member.trip,
        )

        form = ItineraryItemForm( request.POST, instance = item )
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return self.refresh_response( request )

        context = {
            'trip': request_member.trip,
            'item': item,
            'form': form,
        }
        return self.modal_response( request, context = context, status = 400 )


class ItineraryItemDeleteModalView( LoginRequiredMixin, TripViewMixin, ModalView ):

    def get_template_name(self) -> str:
        return 'itineraries/modals/itinerary-item-delete.html'

    def get(self, request, trip_uuid: UUID, item_id: int, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_editor( request_member )
        item = get_object_or_404(
            ItineraryItem, id = item_id, itinerary__trip = request_member.trip,
        )
        context = {
            'trip': request_member.trip,
            'item': item,
        }
        return self.modal_response( request, context = context )

    def post(self, request, trip_uuid: UUID, item_id: int, *args, **kwargs) -> HttpResponse:
        request_member = self.get_trip_member( request, trip_uuid = trip_uuid )
        self.assert_is_editor( request_member )
        item = get_object_or_404(
            ItineraryItem, id = item_id, itinerary__trip = request_member.trip,
        )
        with transaction.atomic():
            item.delete()
        return self.refresh_response( request )
