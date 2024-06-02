from django import forms
from django.forms.widgets import NumberInput

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FAVORITE_COLORS_CHOICES_2 = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FAVORITE_COLORS_CHOICES_3 = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment_again = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES_2)
    favorite_colors_3 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES_3)