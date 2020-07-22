function alertaSucesso(mensagem)
{
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
    Swal.fire({
      icon: json.icon,
      title: json.mensagem,
      showConfirmButton: false,
      timer: 1500,
    })
}
