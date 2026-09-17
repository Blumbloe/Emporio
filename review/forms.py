from django import forms
from .models import Review
from . import models


class CreateReview (forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['title', 'body',]