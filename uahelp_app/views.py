from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

'''
no na pewno strona główna (z listą postów), strona formularza profilu (edycja), strona profilu, strona posta, strona formularza do postu, logowanie, rejestracja formularz, informacja o zarejestrowaniu/wyslaniu maila aktywującego, podziękowanie za kliknięcie w link?, zmiana hasla, reset hasla, dodaj post( przekierowanie na strone logowania jesli niezalogowany, else strona z formularzem), strona z powiadomieniem o weryfikacji, akcja - mail o pozytywnej weryfikacji, 
'''

class HomePageView(TemplateView):
    template_name = 'uahelp_app/home.html'

class ProfileView(TemplateView):
    template_name = 'uahelp_app/profile.html'

class ProfileUpdateView():
    pass

class PostDetailView(TemplateView):
    template_name = 'uahelp_app/post_detail.html'

    def get_context_data(self, **kwargs):
        pass

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





