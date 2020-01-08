
from django import forms
from comments.models import Comment
from posts.models import Post

class FormComment(forms.Form):

    description = forms.CharField(max_length=350, widget=forms.Textarea())

    def save(self, user, post_id):
        comment = self.cleaned_data['description']

        import pdb; pdb.set_trace()

        Comment.objects.create(
            description=comment,
            user=user,
            post=Post.objects.get(pk=post_id)
        )



