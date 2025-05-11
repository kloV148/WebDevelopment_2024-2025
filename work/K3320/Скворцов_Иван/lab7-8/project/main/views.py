from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'main/home.html', {'feedbacks': feedbacks})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'main/contact.html', {'form': form})