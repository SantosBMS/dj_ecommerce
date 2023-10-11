from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
    context = {
                    "title": "Página Sobre",
                    "content": "Bem vindo a Página sobre",
              }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
                    "title": "Página Sobre",
                    "content": "Bem vindo a Página Sobre"
              }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                    "title": "Página de Contato",
                    "content": "Bem vindo a Página de Contato",
                    "form": contact_form	
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)