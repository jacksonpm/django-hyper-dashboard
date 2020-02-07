from allauth.account import views as allauth_views
from allauth.account.views import login, password_reset
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from core.views.registrar import registrar

'''
Urls Primarias
'''
urlpatterns = [
  # Urls Autenticação
  url('registrar', registrar, name='account_signup'),
  url(r'^login/', login, name="account_login"),
  url(r'^resetar-senha/', password_reset, name="account_reset_password"),

  # E-mail
  path("email/", allauth_views.email, name="account_email"),
  path("confirm-email/", allauth_views.email_verification_sent,
       name="account_email_verification_sent"),
  re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", allauth_views.confirm_email,
          name="account_confirm_email"),

  # password reset
  path("password/reset/", allauth_views.password_reset,
       name="account_reset_password"),
  path("password/reset/done/", allauth_views.password_reset_done,
       name="account_reset_password_done"),
  re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
          allauth_views.password_reset_from_key,
          name="account_reset_password_from_key"),
  path("password/reset/key/done/", allauth_views.password_reset_from_key_done,
       name="account_reset_password_from_key_done"),
  path('', admin.site.urls),

  # Urls - Usuários
  path('', include('usuarios.urls')),

  # Urls - Empresas
  path('empresa/', include('empresa.urls')),

  # Urls - Receituário
  path('', include('receituario.urls')),

  # Urls - Laboratorial
  path('', include('laboratorial.urls')),

  # Urls - Tela Agendamneto
  path('', include('agenda.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
