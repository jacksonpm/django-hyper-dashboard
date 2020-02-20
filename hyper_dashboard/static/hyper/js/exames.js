function toggleExame(elemento)
{
    $.ajax({
        type: 'POST',
        url: '/toggle-exame/',
        data: {
            'id_exame': elemento.attr("id").replace('toggle-', ''),
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
    toggleExame($(this));
    })
});