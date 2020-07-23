from django import forms
from .models import post

class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields =[
            "title","content","image","draft","publish",
        ]
