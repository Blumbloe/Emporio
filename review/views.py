from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateReview
from django.contrib import messages
from .models import Review
# Create your views here.


def home_view(request):
    context = {}
    form = CreateReview(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "review/make_review.html", context)


@login_required(login_url="/users/login/")
def new_review(request):
    if request.method == 'POST':
        form = CreateReview(request.POST, request.FILES)
        if form.is_valid():
            newreview = form.save(commit=False)
            newreview.user = request.user
            newreview.save()
            messages.success(request, "Comment successfully created")
            return redirect('/review')
    else:
        form = CreateReview()
    return render(request, '', {'form': form})

@login_required(login_url="/users/login/")
def update_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = CreateReview(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review.save()
            messages.success(request, "Review successfully updated")
            return redirect(reverse('review_list'))
    else:
        form = CreateReview(instance=review)
    return render(request, 'review/update_review.html',
                  {'form': form, 'review': review})

@login_required(login_url="/users/login/")
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect(reverse('review_list'))
    return render(request, 'review/delete_review.html')

@login_required(login_url="/users/login/")
def review_list(request):
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'review/review_list.html',
                  {'reviews': reviews})


def review_list_all(request):
    reviews = Review.objects.filter(all)
    return render(request, 'review/make_review.html',
                  {'reviews': reviews})