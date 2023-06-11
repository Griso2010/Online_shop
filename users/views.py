from django.contrib.auth.views import LoginView
from users.forms import *
from django.urls import reverse_lazy
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from users.models import User


__all_ = (
    'UserLoginView',
    'UserRegistrationView',
    'UserProfileView',
    'logout',
)
class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Регистрация'
        context['basket'] = Basket.objects.filter(user=self.object)
        return context

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

