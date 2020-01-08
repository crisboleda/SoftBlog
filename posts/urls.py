
from django.urls import path
from posts import views

urlpatterns = [
    path('', views.ListPostView.as_view(), name='list_post'),
    path('detail/<int:pk>', views.DetailPostView.as_view(), name="detail_post"),
    path('create/', views.CreatePostView.as_view(), name="create_post"),
    path('like/<int:post>', views.LikePostView.as_view(), name="like_post"),
    path('unlike/<int:post>', views.UnLikePostView.as_view(), name="unlike_post"),
    path('delete/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('edit/<int:pk>', views.UpdatePostView.as_view(), name="update_post"),
]