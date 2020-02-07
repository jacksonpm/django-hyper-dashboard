from django.utils.html import mark_safe
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem
from .widgets import *

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    menu_colaboradores = ParentItem(label=mark_safe('<i class="fa fa-user"></i> Colaboradores'), app="usuarios")
    menu_empresa = ParentItem(label=mark_safe('<i class="fa fa-building"></i> Empresa'), app="empresa")
    menu_auxiliar = ParentItem(label=mark_safe('<i class="fa fa-cog"></i> Sistema'), app="auxiliar")
    menu_paciente = ParentItem(label=mark_safe('<i class="fa fa-cog"></i> Pacientes'), app="paciente")
    menu_receituario = ParentItem(label=mark_safe('<i class="fa fa-cog"></i> Receituario'), app="receituario")
    menu_laboratorial = ParentItem(label=mark_safe('<i class="fa fa-file-text"></i> Laboratorial'), app="laboratorial")
    menu_permissoes = ParentItem(label=mark_safe('<i class="fa fa-cog"></i> Permissões'), app="auth",
                                 permissions=('Can view group',))
    menu_agendamento = ParentItem(label=mark_safe('<i class="fa fa-calendar"></i> Agendamento'), app="agenda",)

    menu = [
        menu_colaboradores,
        menu_empresa,
        menu_auxiliar,
        menu_paciente,
        menu_receituario,
        menu_laboratorial,
        menu_permissoes,
        menu_agendamento,
    ]
