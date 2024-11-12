# bookings/forms.py
from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    rooms = forms.ModelMultipleChoiceField(
        queryset=Room.objects.none(),  # Initialize with no rooms
        widget=forms.CheckboxSelectMultiple,  # Render as checkboxes
        required=True  # Set to True to make it a required field
    )
    check_in_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',  # Use HTML5 date input
        }),
        required=True
    )
    check_out_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',  # Use HTML5 date input
        }),
        required=True
    )

    class Meta:
        model = Booking
        fields = ['guest', 'rooms', 'check_in_date', 'check_out_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter rooms to only include available ones
        self.fields['rooms'].queryset = Room.objects.filter(available=True)
