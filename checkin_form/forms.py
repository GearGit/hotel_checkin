from django import forms

GENDER_CHOICES = (
    ('male','MALE'),
    ('female','FEMALE'),
    ('others','OTHERS')
)
PAYMENT_CHOICES = (
    ('Cash','CASH'),
    ('Credit Card','CREDIT CARD'),
    ('Debit Card','DEBIT CARD'),
    ('UPI','UPI')
)
ROOM_CHOICES = (
    ('1001(1 bed)','1001'),
    ('1002(2 beds)','1002'),
    ('1003(3 beds)','1003'),
    ('1004(4 beds)','1004'),
    ('2001(1 bed)','2001'),
    ('2002(2 beds)','2002')
)
ADDITIONAL_CHOICES = (
    ('Air Conditioned','AC'),
    ('Free Pick-Up','PICK UP'),
    ('Mini Fridge','MINIFRIDGE'),
    ('Gym','GYM')
)
class CheckInModel(forms.Form):
    first_name = forms.CharField(required=True,max_length=30)
    last_name = forms.CharField(required=True,max_length=30)
    email = forms.EmailField(max_length=254)
    age = forms.IntegerField()
    address = forms.CharField(required=True,max_length=250)
    gender = forms.ChoiceField(required=True,choices=GENDER_CHOICES, widget=forms.RadioSelect())
    payment_method = forms.CharField(required=True, widget=forms.Select(choices=PAYMENT_CHOICES))
    additional_choices = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ADDITIONAL_CHOICES
    )
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))
    checkin = forms.DateField(required=True,widget=forms.SelectDateWidget())
    checkout = forms.DateField(required=True,widget=forms.SelectDateWidget())
    room_allocated = forms.CharField(required=True, widget=forms.Select(choices=ROOM_CHOICES))