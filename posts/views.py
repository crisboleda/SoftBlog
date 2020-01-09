from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, FormView, ListView, DetailView, RedirectView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import Http404

from posts.forms import PostForm, UpdatePost
from posts.models import Post, Tag
from comments.models import Comment



class OwnerPostMixin(object):

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if self.request.user != post.author:
            raise Http404("You don't permission")
        return super().dispatch(request, *args, **kwargs)


# Create your views here.
class ListPostView(ListView):
    template_name = 'posts/index.html'
    queryset = Post.objects.all()
    ordering = '-data_published'
    context_object_name = 'posts'
    paginate_by = 5


class DetailPostView(DetailView):
    template_name = 'posts/post.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post__pk=self.kwargs['pk']).order_by('-created')
        return context 


class CreatePostView(LoginRequiredMixin, FormView):
    template_name = "posts/create.html"
    form_class = PostForm
    success_url = reverse_lazy('posts:list_post')

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


# System of likes
class LikePostView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        try:
            post = Post.objects.get(pk=self.kwargs['post'])
            post.likes.add(self.request.user)
            post.save()

        except Post.DoesNotExist:
            return reverse('posts:list_post')
        return reverse('posts:detail_post', kwargs={'pk':self.kwargs['post']})


class UnLikePostView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        try:
            post = Post.objects.get(pk=self.kwargs['post'])
            post.likes.remove(self.request.user)
            post.save()

        except Post.DoesNotExist:
            return reverse('posts:list_post')
        return reverse('posts:detail_post', kwargs={'pk':self.kwargs['post']})



class DeletePostView(LoginRequiredMixin, OwnerPostMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('users:user_profile', kwargs={'pk':self.request.user.pk})

    

class UpdatePostView(LoginRequiredMixin, OwnerPostMixin, UpdateView):
    template_name = 'posts/edit_post.html'
    form_class = UpdatePost
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_initial(self):
        initial = super().get_initial()
        post = Post.objects.get(pk=self.kwargs['pk'])

        initial = {
            'tags': self.get_tag_of_post(post)
        }
        return initial


    def form_valid(self, form):
        form.update_tags(self.kwargs['pk'])
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('posts:detail_post', kwargs={'pk':self.kwargs['pk']})


    # Convierto una lista en un string separados por , para enviarlo al fronted
    def get_tag_of_post(self, post):
        tags = ''
        for i, tag in enumerate(post.tags.all()):
            if len(post.tags.all()) -1 == i:
                tags += '{}'.format(tag.name_tag)
            else:
                tags += '{},'.format(tag.name_tag)
        return tags
