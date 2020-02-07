$("#id_cep").focusout(function(){
    $.ajax({
        url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/unicode/',
        dataType: 'json',
        success: function(resposta){
            if (resposta.logradouro != '') {
                $("#id_endereco").val(resposta.logradouro);
            }
            if (resposta.complemento != '') {
                $("#id_endereco_complemento").val(resposta.complemento);
            }

            if (resposta.bairro != '') {
                $("#id_bairro").val(resposta.bairro);
            }

            if (resposta.localidade != '') {
                $("#id_cidade").val(resposta.localidade);
            }
            if (resposta.uf != '') {
                $("#id_uf").val(resposta.uf);
            }

            $("#id_endereco_numero").focus();
        }
    });
});
