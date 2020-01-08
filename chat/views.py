from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404, JsonResponse
import time

from .models import Group, Message
# Create your views here.


class ListGroupView(LoginRequiredMixin, ListView):
    template_name = 'chat/index.html'
    queryset = Group.objects.all()
    context_object_name = 'groups'


class DetailGroupView(LoginRequiredMixin, DetailView):
    template_name = 'chat/group_messages.html'
    model = Group
    context_object_name = 'group'

    def get_object(self):
        group = super().get_object()
        if self.request.user in group.members.all():
            return group
        else:
            raise Http404("You aren't in the group")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class JoinExitGroupView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        try:
            group = Group.objects.get(pk=self.kwargs['pk'])
            group.join_or_exit_group(self.request.user)
        except:
            raise Http404('Upps... There is a problem')
        return reverse_lazy('chat:index')


def add_message_to_group(request, pk):
    try:
        if request.user.is_authenticated:
            group = Group.objects.get(pk=pk)
            if request.user in group.members.all():
                Message.objects.create(content=request.GET['content'], group=group, author=request.user)
            else:
                return redirect(reverse_lazy('chat:index'))
        else:
            return redirect(reverse_lazy('users:login'))
    except:
        raise Http404('upss')

    return JsonResponse({'good': 'very good'})

