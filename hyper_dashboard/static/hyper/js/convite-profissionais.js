
function enviarConvite()
{
    let valor = $('#id_profissional').val()
    if (valor == '') {
        $('#id_profissional').focus();
        return false;
    }

    Swal.fire({
        title: "Atenção",
        text: "Revise as informações do profissional antes enviar o email.",
        icon: "info",
        buttons: true,
        dangerMode: false,
    })
    .then((willDelete) => {
    if (willDelete) {
        convidar();
    }
    });
}

function convidar()
{
     $.ajax({
        type: 'POST',
        url: '/empresa/gerar-convite-clinica/',
        data: {
            'id_profissional': $('#id_profissional').val(),
            'id_clinica': $('#id_clinica').val(),
        },
        success: function (data) {
            $('#tabela-profissionais-convidados').html(data);
            alertaGenerico(data)
            reloadTabela();
        },

        error: function (data) {
            alertaErro("Ocorreu um erro ao convidar o profissional, contate o suporte.")
        }
    });
}

function reloadTabela()
{
    let tabela = $('#tabela-profissionais-convidados')
     $.ajax({
        type: 'POST',
        url: '/empresa/tabela-profissionais-habilitados/',
        data: {
            'id_clinica': $('#id_clinica').val(),
        },
        success: function (data) {
            $('#tabela-profissionais-convidados').html(data);
            $("input[data-toggle='toggle']").bootstrapToggle();
            $("input[data-toggle='toggle']").change(function() {
                ativarDesativarProfissional($(this))
            })

        },

        error: function (data) {
            alertaErro("Ocorreu um erro ao carregar a tabela de profissionais, contate o suporte.")
        }
    });
}

function ativarDesativarProfissional(elemento)
{
    $.ajax({
        type: 'POST',
        url: '/toggle-profissional-convidado/',
        data: {
            'id_profissional': elemento.attr("id").replace('toggle-', ''),
            'ativo': elemento[0].checked,
        },
        success: function (data) {
            alertaGenerico(data)
        },
        error: function (data) {
            alertaErro(data)
        }
    });
}

$(document).ready(function() {
    reloadTabela();
});
