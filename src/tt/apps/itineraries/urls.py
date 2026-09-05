"""
URL configuration for itineraries app.
"""

from django.urls import path

from . import views

urlpatterns = [
    path(r'<uuid:trip_uuid>', views.ItinerariesHomeView.as_view(), name='itineraries_home'),
    path(
        r'<uuid:trip_uuid>/item/create',
        views.ItineraryItemCreateModalView.as_view(),
        name='itinerary_item_create',
    ),
    path(
        r'<uuid:trip_uuid>/item/<int:item_id>/edit',
        views.ItineraryItemEditModalView.as_view(),
        name='itinerary_item_edit',
    ),
    path(
        r'<uuid:trip_uuid>/item/<int:item_id>/delete',
        views.ItineraryItemDeleteModalView.as_view(),
        name='itinerary_item_delete',
    ),
]
