from django.urls import path
from .views import post_detail,about,create_post,register,home,like_post,update_post,delete_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",home, name='home'),
    path('post/<slug:slug>/',post_detail,name='post_detail'),
    path('post/<slug:slug>/like/', like_post, name='like_post'),
    path('post/<slug:slug>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/delete/', delete_post, name='delete_post'),

    path("about/",about,name="about"),
    path("create_post/",create_post,name='create_post'),
    
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/',register,name='register')
]

