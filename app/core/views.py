from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, AuthUserForm, RegistrUserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class HomeListView(ListView):
    
    model = Articles
    template_name = "home.html"
    context_object_name = 'list_articles'


class HomeDetailView(DetailView):
    
    model = Articles
    template_name = "article.html"
    context_object_name = 'get_articles'


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'editpage.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')

    def get_context_data(self,**kwargs):
        kwargs['list_articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin,UpdateView):

    model = Articles
    template_name = "editpage.html"
    form_class = ArticleForm
    success_url = reverse_lazy('editpage')
 
    def get_context_data(self, **kwargs):

        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs    

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Articles
    template_name = 'editpage.html'
    success_url = reverse_lazy('editpage')
    
    def post(self,request,*args,**kwargs):
        return super().post(request)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class MyprojectLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('editpage')
    def get_success_url(self):
        return self.success_url

class MyprojectLogOut(LogoutView):
    next_page = reverse_lazy('editpage')


class RegistrUserView(CreateView):
    model = User
    template_name = "registr-page.html"
    form_class = RegistrUserForm
    success_url = reverse_lazy('editpage')
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid




