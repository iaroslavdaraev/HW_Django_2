from random import randint

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        new_user = form.save()
        ver_num = randint(1000, 1000000)
        new_user.verification_code = ver_num
        new_user.save()
        send_mail(
            subject='Активация аккаунта',
            message=f'Ваш код активации: {ver_num}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False
        )
        return super().form_valid(form)


def verify(request):
    if request.method == 'POST':
        number = request.POST.get('number')
    try:
        user = User.objects.get(verification_code=number)
        user.verified = True
        user.save()
        return redirect(reverse('users:login'))
    except:
        return render(request, 'users/verification.html')


class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    new_password = ''.join([str(randint(0, 9)) for _ in range(10)])
    send_mail(
        subject='Ваш новый пароль',
        message=new_password,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False
    )

    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
