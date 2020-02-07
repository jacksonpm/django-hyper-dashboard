import re

def formatar_real(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')

def formata_data(data):
    return data.strftime("%d/%m/%Y")

def formata_data_hora(data):
    return data.strftime("%d/%m/%Y - %Hh %Mm")

def formata_hora(hora , segundos = False):
    if segundos:
        return '{}:{}:{}'.format(hora.hour, hora.minute, hora.second)

    return '{}:{}'.format(str(hora.hour).zfill(2), str(hora.minute).zfill(2))

def formata_nome(string_nome):
    """
    :type string_nome: basestring
    """
    return str(string_nome).upper()

def somente_numeros(string):
    return re.sub("\D", "", string)