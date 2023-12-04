from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid. Redirecting to login page.")
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("Form is invalid. Rendering form with errors.")
        print(form.errors)
        return response


def index(request):
    return render(request, 'index.html')

