from django.urls import path
from users import views


urlpatterns = [
    path('signin/', views.LoginUserView.as_view(), name='login'),
    path('signup/', views.SignupUserView.as_view(), name="register"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/<int:pk>', views.ProfileUserView.as_view(), name='user_profile'),
    path('update/profile/', views.UpdateProfileView.as_view(), name='update_profile'),
]