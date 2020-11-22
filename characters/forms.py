from .models import Characters
from django import forms


class SearchCharacter(forms.Form):
    fullname = forms.CharField(label='', max_length=50)


query = Characters.objects.all()
set_choices = [(name.fullname, name.fullname) for name in query]
start = ('-', '-')
set_choices.append(start)
# print(set_choices)


class PlayGameForm(forms.Form):
    first = forms.CharField(label='',max_length=50,
                            required=True,
                            widget=forms.Select(choices=set_choices),
                            initial='-')
    second = forms.CharField(label='',
                             max_length=50,
                             required=True,
                             widget=forms.Select(choices=set_choices),
                             initial='-')
