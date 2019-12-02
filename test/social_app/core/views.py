from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadDocumentForm
from .models import Download

def login(request):
    return render(request, 'login.html')
@login_required
def home(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)  # Do not forget to add: request.FILES
        if form.is_valid():
            form.save()
    return render(request, 'home.html', locals())