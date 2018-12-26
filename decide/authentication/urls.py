from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView
from .views import GetUserView, LogoutView, RegisterUserView


urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]
