from django import forms

class GuyForm(forms.Form):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    name = forms.CharField(error_messages={'required':'cannot be null'})
    age = forms.IntegerField()
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=11)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)