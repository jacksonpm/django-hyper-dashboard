from django.utils.html import mark_safe

def toggle(ativo, id):
    checked = 'checked' if ativo else ''
    return mark_safe('<input type="checkbox" data-on= "Sim" data-size="sm"'
                     'data-off="Não" {} id="toggle-{}" data-toggle="toggle" data-size="sm">'.format(checked, id))

def icon(label, icone):
    return mark_safe('<i class="{}"></i> {}'.format(icone, label))

def badge(nome , cor):
    return mark_safe('<span class="badge badge-{}-lighten p-1">{}</snpan>'.format(cor, nome))

def avatar(imagem):
    return mark_safe('<img src = "/media/{}" alt = "user-image" height = "42" class ="avatar">'.format(imagem))