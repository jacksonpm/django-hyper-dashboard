function toggleConvenio(elemento)
{
    $.ajax({
        type: 'POST',
        url: '/empresa/toggle-convenio/',
        data: {
            'id_convenio': elemento.attr("id").replace('toggle-', ''),
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
    toggleConvenio($(this));
    })
});