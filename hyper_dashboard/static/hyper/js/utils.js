function numberToReal(numero) {
    return numero.toLocaleString('pt-BR')
}

function alterarItem(elemento) {
  window.location = elemento.children[1].children[0].href
}

function resize_for_popup() {
    if(/[?&]_popup=1(&|$)/.test(location.href)) {
        window.resizeTo(screen.availWidth, screen.availHeight);
    }
}

resize_for_popup();

(function($) {
    $('[data-confirm]').click( function() {
        let element = $(this)
        event.preventDefault();
        let text = element.attr('data-confirm-text')
        let icon = element.attr('data-confirm-icon')
        let title = element.attr('data-confirm-title')
        let button_text = element.attr('data-confirm-button-text')

        Swal.fire({
              title: title,
              text: text,
              icon: icon,
              showCancelButton: true,
              confirmButtonColor: '#5398fb',
              cancelButtonColor: '#fa6767',
              confirmButtonText: button_text,
              cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.value) {
                location.href = element.attr('href')
            }
        })

    })
})(jQuery);

