from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail_view'),

]
