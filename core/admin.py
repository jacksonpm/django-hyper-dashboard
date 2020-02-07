import django.contrib.auth.models
from django.contrib import auth, admin
from django.contrib.sites.models import Site
from .administracao.tenant import TenantAdmin

# Removendo Cadastros Padrao
admin.site.unregister(Site)
#admin.site.unregister(auth.models.Group)

# Registrando Admin - Tenant
TenantAdmin = TenantAdmin

# Título do App
admin.site.site_header = 'App Clinica'
admin.site.site_title = 'App Clínica'