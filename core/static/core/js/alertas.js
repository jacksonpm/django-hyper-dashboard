function alertaSucesso(mensagem)
{
//    $.toast({
//        title: "Tudo Certo!",
//        content: mensagem,
//        type: 'success',
//        delay: 2000, img: {class: 'rounded avatar', src:'/media/avataaars.png'}
//    });
    Swal.fire({
      icon: 'success',
      title: mensagem,
      showConfirmButton: false,
      timer: 1500,
    })
}

function alertaErro(mensagem)
{
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: mensagem,
    })
}

function alertaGenerico(json)
{
//    $.toast({
//        title: json.icon,
//        content: json.mensagem,
//        type: json.icon,
//        delay: 2000, img: {class: 'rounded avatar', src:'/media/avataaars.png'}
//    });
    Swal.fire({
      icon: json.icon,
      title: json.mensagem,
      showConfirmButton: false,
      timer: 1500,
    })
}
