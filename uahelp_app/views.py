from datetime import timedelta
from logging import getLogger

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, FormView, UpdateView
from django.urls import reverse_lazy

from uahelp_app.forms import LoginForm, UserRegistrationForm
from uahelp_app.models import Post, Profile
from uahelp_app.forms import PostDetailForm, ProfileUpdateForm

# Create your views here.

'''
no na pewno strona główna (z listą postów), strona formularza profilu (edycja), strona profilu, strona posta, strona formularza do postu, logowanie, rejestracja formularz, informacja o zarejestrowaniu/wyslaniu maila aktywującego, podziękowanie za kliknięcie w link?, zmiana hasla, reset hasla, dodaj post( przekierowanie na strone logowania jesli niezalogowany, else strona z formularzem), strona z powiadomieniem o weryfikacji, akcja - mail o pozytywnej weryfikacji, 
'''


class HomePageView(TemplateView):
    template_name = 'uahelp_app/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        verificated_time = timezone.now()-timedelta(minutes=5)
        context['posts'] = Post.objects.filter(is_verificated=True, created_at__lte=verificated_time).order_by('-created_at')
        return context


class ProfileView(DetailView):
    template_name = 'uahelp_app/profile.html'
    model = Profile


class ProfileUpdateView(UpdateView):
    template_name = 'uahelp_app/profile_update.html'
    model = Profile
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.request.user.profile_set.first().id])


class PostDetailView(TemplateView):
    template_name = 'uahelp_app/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        pk = kwargs.get('pk', None)
        if pk:
            post = Post.objects.get(id=pk)
            context['post'] = post
        return context


class PostCreateView(LoginRequiredMixin, FormView):
    template_name = 'uahelp_app/post_create.html'
    form_class = PostDetailForm
    success_url = reverse_lazy('post_verification')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Post.objects.create(
            title=cleaned_data['title'],
            content=cleaned_data['content'],
            profile_id=self.request.user.profile_set.first().id
        )
        return result


class PostUpdateView():
    pass


class AboutUsView(TemplateView):
    template_name = 'uahelp_app/about.html'


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
            print(new_user) #kita
            Profile.objects.create(account_type=user_form.cleaned_data['account_type'],
                                   name=user_form.cleaned_data['name'],
                                   user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


class PostVerificationView(TemplateView):
    template_name = 'uahelp_app/post_verification.html'


class SearchResultView(TemplateView):
    pass

