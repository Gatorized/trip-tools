from django import forms

from .models import ItineraryItem


class ItineraryItemForm( forms.ModelForm ):

    class Meta:
        model = ItineraryItem
        fields = (
            'item_type',
            'title',
            'start_datetime',
            'end_datetime',
            'description',
            'notes',
        )
        widgets = {
            'item_type': forms.Select( attrs = {
                'class': 'form-control',
            }),
            'title': forms.TextInput( attrs = {
                'class': 'form-control',
                'placeholder': 'e.g., Drive to Wotton',
                'autofocus': 'autofocus',
            }),
            'start_datetime': forms.DateTimeInput( attrs = {
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'end_datetime': forms.DateTimeInput( attrs = {
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'description': forms.Textarea( attrs = {
                'class': 'form-control',
                'placeholder': 'e.g., 32 Rang 16 EST, Wotton (Québec) J0A 1N0',
                'rows': 2,
            }),
            'notes': forms.Textarea( attrs = {
                'class': 'form-control',
                'placeholder': 'Optional notes',
                'rows': 2,
            }),
        }

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        # datetime-local inputs need naive "YYYY-MM-DDTHH:MM" strings, not
        # the ISO-with-offset format DateTimeField would otherwise produce.
        for field_name in ( 'start_datetime', 'end_datetime' ):
            value = getattr( self.instance, field_name, None )
            if value:
                self.initial[field_name] = value.strftime( '%Y-%m-%dT%H:%M' )
