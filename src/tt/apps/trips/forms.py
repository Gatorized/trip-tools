from django import forms

from .models import Trip
from .enums import TripStatus


class TripForm( forms.ModelForm ):

    class Meta:
        model = Trip
        fields = (
            'title',
            'description',
        )
        widgets = {
            'title': forms.TextInput( attrs = {
                'class': 'form-control',
                'placeholder': 'Entrez le titre du voyage',
                'autofocus': 'autofocus',
            }),
            'description': forms.Textarea( attrs = {
                'class': 'form-control',
                'placeholder': 'Entrez une description facultative',
                'rows': 3,
            }),
        }

    def save(self, commit = True):
        trip = super().save( commit = False )

        if not trip.pk:
            trip.trip_status = TripStatus.UPCOMING

        if commit:
            trip.save()

        return trip
