from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        data =  super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, "Created New User Now you can login")
        
        return data
        
    

