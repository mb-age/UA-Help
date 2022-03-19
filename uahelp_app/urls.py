from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail_view'),
]

