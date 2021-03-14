from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'


class PasswordChangeViewMichal(auth_views.PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')


urlpatterns = [
    # path('login/', views.user_login, name="login")
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeViewMichal.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name='dashboard')
]

