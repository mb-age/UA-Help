from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from uahelp_app.models import Post, Profile


# Create your views here.

'''
no na pewno strona główna (z listą postów), strona formularza profilu (edycja), strona profilu, strona posta, strona formularza do postu, logowanie, rejestracja formularz, informacja o zarejestrowaniu/wyslaniu maila aktywującego, podziękowanie za kliknięcie w link?, zmiana hasla, reset hasla, dodaj post( przekierowanie na strone logowania jesli niezalogowany, else strona z formularzem), strona z powiadomieniem o weryfikacji, akcja - mail o pozytywnej weryfikacji, 
'''

class HomePageView(TemplateView):
    template_name = 'uahelp_app/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_verificated=True).order_by('-created_at')
        return context

class ProfileView(DetailView):
    template_name = 'uahelp_app/profile.html'
    model = Profile

class ProfileUpdateView():
    pass

class PostDetailView(TemplateView):
    template_name = 'uahelp_app/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        pk = kwargs.get('pk', None)
        if pk:
            post = Post.objects.get(id=pk)
            context['post'] = post
        return context

class PostCreateView():
    pass

class PostUpdateView():
    pass

class LogInView():
    pass

class RegisterView():
    pass

class RegisterConfirmationView(TemplateView):
    pass

class VerificationInfoView(TemplateView):
    pass

class PasswordUpdateView():
    pass

class PasswordResetView():
    pass





