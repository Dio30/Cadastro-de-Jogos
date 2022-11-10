# Como utilizar

## <li>Crie uma pasta com um nome a sua escolha e depois digite no prompt de comando: code . ou outro IDE que você use</li>

## Clonar repositório

## <li>git clone https://github.com/Dio30/Cadastro-de-Jogos.git</li>

# Preparando o ambiente virtual

## <li>python -m venv venv </li>
## <li>.\venv\Scripts\activate </li>
## <li>pip install django </li>
## <li>pip install -r requirements.txt </li>

# Rode as migrações

## <li>python manage.py migrate </li>

# Criar superusuario

## <li>python manage.py createsuperuser</li>

# Iniciando o servidor

## <li>python manage.py runserver</li>

# Cadastro de Jogos

## Foi feito um CRUD de jogos em django sendo responsivo para celular, pode visualizar imagens atraves do modal sem sair da pagina e para deletar um jogo é possivel através do modal tambem. No CRUD é possivel visualizar, adicionar, editar e deletar jogos selecionados e aparecerá uma mensagem no topo da pagina se a ação foi bem sucedida.

## Também é possivel adicionar/editar sua foto de perfil separadamente das fotos dos jogos adicionados, no perfil pode trocar o nome do usuario e o seu email tambem.

## É possivel tambem fazer paginação entre os jogos adicionados já que só é possivel visualizar um jogo por pagina por questão de responsividade.

## Caso queira pode trocar a senha sabendo a senha antiga e obedecendo os critérios solicitados

## Quando é cadastrado um usuario e um email se quiser esse usuario se torna unico e o email quando inserido também, acredito que em questão de segurança e privacidade são questões muito importantes.

## Esse projeto é mais voltado para pessoas que gostam de jogos e que queiram mantê-los guardados em um site e também serve para simular uma loja de jogos que queira manter seu estoque atualizado.

## Foi adicionado uma validação para que quando for redefinir a senha usando o email só será aceito o envio do email se o mesmo estiver cadastrado, se não irá aparecer uma mensagem de erro
