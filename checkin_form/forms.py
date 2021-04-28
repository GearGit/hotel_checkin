from django import forms
from .models import CheckInModel

class CheckInForm(forms.ModelForm):
    
    class Meta:
        ADDITIONAL_CHOICES = (
    ('AC','Air Conditioned'),
    ('PICK UP','Free Pick-Up'),
    ('MINIFRIDGE','Mini Fridge'),
    ('GYM','Gym')
)
        model = CheckInModel
        fields='__all__'
        widgets={
            'gender':forms.RadioSelect(),
            'payment_method':forms.Select(),
            'file_field':forms.FileInput(),
            'checkin':forms.SelectDateWidget(),
            'checkout':forms.SelectDateWidget(),
            'room_allocated':forms.Select(),
            'additional_choices':forms.CheckboxSelectMultiple(choices=ADDITIONAL_CHOICES)
        }
