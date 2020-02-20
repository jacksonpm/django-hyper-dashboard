function toggleClinica(elemento)
{
    $.ajax({
        type: 'POST',
        url: '/empresa/toggle-clinica/',
        data: {
            'id_clinica': elemento.attr("id").replace('toggle-', ''),
            'ativo': elemento[0].checked,
        },
        success: function (data) {
            alertaGenerico(data)
        },
        error: function (data) {
            alertaErro("Ocorreu um erro. Tente novamente.")
        }
    });
}

$(document).ready(function() {
    $("input[data-toggle='toggle']").change(function() {
        toggleClinica($(this));
    })
});


