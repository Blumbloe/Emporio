from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateReview
from django.contrib import messages
from .models import Review
# Create your views here.

