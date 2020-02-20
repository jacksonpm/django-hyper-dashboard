from django import template

register = template.Library()

@register.inclusion_tag('admin/navbar.html')
def navbar_topo(request):
    menu = [
        ['label', 'url', 'icon'],
        ['label', 'url', 'icon'],
        ['label', 'url', 'icon'],
        ['label', 'url', 'icon'],
        ['label', 'url', 'icon'],
    ]
    return {'info' : 'teste',
            'logo' : '',
            'avatar' : '',
            'color' : '#a465se',
            'username' : 'teste',
            'subtitle' : 'teste',
            'menu' : menu,
            }
