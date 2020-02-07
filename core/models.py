from django.db.models import *
from django.utils import timezone

from core.tabelas.tenant import Tenant


class TenantManager(Manager):
    """
    Esse Manager faz o filtro por Tenant caso esse tributo exista
    """

    def get_queryset(self):
        return super().get_queryset().filter(data_exclusao=None)


class BaseModel(Model):
    """
    Esta model é uma model abstrata
    todas as outas models terão também estes campos e herdarão essa model
    isso fará o controle de dados por cada cliente
    """
    criado = DateTimeField(auto_now_add=True, editable=False)
    data_exclusao = DateTimeField(default=None, null=True, blank=True, editable=False)
    tenant = ForeignKey(Tenant, null=True, on_delete=CASCADE, editable=False)

    # Faz o filtro dos resultados que não foram excluidos (soft-delete)
    objects = TenantManager()

    def delete(self, using=None, keep_parents=False):
        self.data_exclusao = timezone.now()
        return super().save()

    def excluido(self):
        if self.data_exclusao is None:
            return True
        else:
            return False

    class Meta:
        abstract = True
