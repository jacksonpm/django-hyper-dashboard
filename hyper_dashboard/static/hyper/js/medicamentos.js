function toggleMedicamento(elemento)
{
    $.ajax({
        type: 'POST',
        url: '/toggle-medicamento/',
        data: {
            'id_medicamento': elemento.attr("id").replace('toggle-', ''),
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
    toggleMedicamento($(this));
    })
});