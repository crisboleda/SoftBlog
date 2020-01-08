from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from users.backends import EmailBackend
from users.forms import SignupForm, FormUpdateProfile
from posts.models import Post
# Create your views here.

class LoginUserView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logged_out.html'


class SignupUserView(FormView):
    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class ProfileUserView(DetailView):
    template_name = 'users/profile.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author__pk=self.kwargs['pk'])
        return context


class UpdateProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/update_profile.html'
    form_class = FormUpdateProfile

    def get_initial(self):
        initial = super().get_initial()
        initial = {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
            'picture': self.request.user.profile.picture
        }
        return initial

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)



    def get_success_url(self):
        return reverse_lazy('users:user_profile', kwargs={'pk':self.request.user.pk})
