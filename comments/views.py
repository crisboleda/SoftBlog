from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# App comments
from comments.forms import FormComment
from comments.models import Comment
# Create your views here.


class CreateCommentPost(LoginRequiredMixin, FormView):
    template_name = 'posts/index.html'
    form_class = FormComment

    def form_valid(self, form):
        form.save(self.request.user, self.kwargs['post'])
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('posts:detail_post', kwargs={'pk': self.kwargs['post']})






