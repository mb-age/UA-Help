from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail_view'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create_view'),
    path('post/verification/', views.PostVerificationView.as_view(), name='post_verification'),
    path('about/', views.AboutUsView.as_view(), name='about'),

]
