### Aplicativo de Gestão de Clínicas

##### Ambiente de desenvolvimento

Instale o Python 3.5 (ou superior), qualquer versão acima de 3.5 vai servir.

Depois de instalado clone esse repositório em qualquer pasta.

```shell script
C:\Fontes\> git clone https://github.com/jacksonpm/app-clinica.git
cd app-clinica
```

Agora inicie um ambiente virtual do python nesse repositório e o ative.

Linux: 
https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

Windows: :fire:
https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/

Agora com o ambiente virtual ativado:
Instale as bibliotecas:


```shell script
(venv) C:\Fontes\app-clinica> pip install -r requiriments.txt
```

E instale também o django suit.
```shell script
(venv) C:\Fontes\app-clinica> pip install https://github.com/darklow/django-suit/tarball/v2
```

Pronto!
Agora execute o comando:
(LEMBRE-SE DE APAGAR O SEU ARQUIVO DB.SQLITE3!, CASO ELE EXISTA!)

```shell script
(venv) C:\Fontes\app-clinica> python manage.py run_dev
```

Esse comando pode demorar uns 10 a 20 minutos, pois ele cria uma grande base de dados para teste
e também todas as tabelas necessárias para rodar o projeto.


```shell script
(venv) C:\Fontes\app-clinica> python manage.py runserver
```





