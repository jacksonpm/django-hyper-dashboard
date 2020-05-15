from django.utils.html import mark_safe


def toggle(ativo, id):
    checked = 'checked' if ativo else ''
    return mark_safe('<input type="checkbox" data-on= "Sim" data-size="sm"'
                     'data-off="Não" {} id="toggle-{}" data-toggle="toggle" data-size="sm">'.format(checked, id))


def icon(label, icone):
    return mark_safe('<i class="{}"></i> {}'.format(icone, label))


def badge(nome, cor):
    return mark_safe('<span class="badge badge-{}-lighten p-1">{}</snpan>'.format(cor, nome))


def avatar(imagem):
    return mark_safe('<img src = "/media/{}" alt = "user-image" height = "42" class ="avatar">'.format(imagem))


def confirm(label='', url='', text='', icon='warning', title='Aviso', button_text='Sim'):
    html = '<a href="{url}" data-confirm="true" ' \
           'data-confirm-url="{url}" data-confirm-text="{text}" data-confirm-icon="warning" ' \
           'data-confirm-button-text="{button_text}" data-confirm-title="{title}">{label}</a>'.format(
        label=label, url=url, icon=icon, text=text, title=title, button_text=button_text
    )

    return mark_safe(html)
