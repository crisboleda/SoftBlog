
from django.urls import path
from comments import views

urlpatterns = [
    path('post/<int:post>', views.CreateCommentPost.as_view(), name="make_comment"),
]