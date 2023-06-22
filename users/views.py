from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from common.views import TitleMixin
from users.models import User
from users.forms import *



__all_ = (
    'UserLoginView',
    'UserRegistrationView',
    'UserProfileView',
    'logout',
)

class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'

class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'
    title = 'Store - Регистрация'

class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))