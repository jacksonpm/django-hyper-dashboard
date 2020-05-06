function numberToReal(numero) {
    return numero.toLocaleString('pt-BR')
}

function alterarItem(elemento) {
  window.location = elemento.children[1].children[0].href
}

function resize_for_popup() {
    if(/[?&]_popup=1(&|$)/.test(location.href)) {
        window.resizeTo();
    }
}

resize_for_popup();