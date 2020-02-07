def mascara(padrao, variavel):
    return padrao.replace('X', '{}').format(*str(variavel))
