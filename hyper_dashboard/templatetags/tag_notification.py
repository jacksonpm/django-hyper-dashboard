from django import template


register = template.Library()

@register.simple_tag
def notification(message):
    titulo = ''
    if message.level_tag == 'success':
        titulo = 'Sucesso'

    return {'icon': message.tags, 'conteudo': message.message, 'titulo': titulo}