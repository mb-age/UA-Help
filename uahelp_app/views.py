from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from uahelp_app.forms import LoginForm, UserRegistrationForm
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


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Zalogowano pomyślnie")
                else:
                    return HttpResponse("Konto nie jest aktywne")
            else:
                return HttpResponse("Nieprawidłowe dane logownia")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


class RegisterConfirmationView(TemplateView):
    pass


class VerificationInfoView(TemplateView):
    pass


class PasswordUpdateView():
    pass


class PasswordResetView():
    pass

