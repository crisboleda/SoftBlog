from django import forms
from ckeditor.widgets import CKEditorWidget
from posts.models import Caterory, Tag, Post

class PostForm(forms.Form):

    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title'}
    ))

    subtitle = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subtitle'}
    ))

    content = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control', 'placeholder': 'Content'}
        ),
    )

    category = forms.ChoiceField(
        choices=([(category.pk, category.name_category) for category in Caterory.objects.all()]),   
    )

    tags = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'readonly': 'true', 'style': 'display:none;'}
    ))


    def save(self, request):
        data = self.cleaned_data

        category = Caterory.objects.get(pk=int(data['category']))

        # Split to string the tags
        name_tags = data['tags'].split(',')
        tags = []

        for name_tag in name_tags:
            tags.append(Tag.objects.get(name_tag=name_tag))

        post = Post(
            title=data['title'],
            subtitle=data['subtitle'],
            content=data['content'],
            author=request.user,
            category=category
        )

        post.save()
        post.tags.set(tags)
        post.save()



class UpdatePost(forms.ModelForm):

    tags = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'readonly': 'true', 'style': 'display:none;'}
    ))

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorWidget(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'display:none;'})
        }

    def update_tags(self, post_id):
        data = self.cleaned_data
        post = Post.objects.get(pk=post_id)

        name_tags = data['tags'].split(',')
        tags = []

        for name_tag in name_tags:
            tags.append(Tag.objects.get(name_tag=name_tag))

        post.tags.set(tags)
        post.save()
        
        import pdb; pdb.set_trace()


    