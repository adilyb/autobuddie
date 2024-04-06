from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View, UpdateView
from userprofile.forms import UserProfileForm
from userprofile.models import UserProfileModel
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class UserRegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    def form_valid(self, form):
        UserProfileModel.objects.create(
            user = form.save()
        )
        return super().form_valid(form)
    


class UserLoginView(View):
    def get(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            pk = user.id
            settings.LOGIN_REDIRECT_URL = f'/accounts/profile/{pk}'
            return redirect(f'/accounts/profile/{pk}')
        return redirect("login")

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user_profile/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfileModel.objects.get(user=self.request.user)
        context['userprofile'] = user_profile
        return context


class DashboardView(TemplateView):
    template_name = 'user_profile/dashboard.html' 


class UserProfileUpdateView(UpdateView):
    template_name = "user_profile/profile_update.html"
    form_class = UserProfileForm
    model = UserProfileModel
    success_url = '/accounts/profile/'
    