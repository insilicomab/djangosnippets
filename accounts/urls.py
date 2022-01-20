from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from accounts.forms import EmailAuthenticationForm


urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),

    path('login/', LoginView.as_view(
        form_class=EmailAuthenticationForm,  # フォームクラスを指定
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
]