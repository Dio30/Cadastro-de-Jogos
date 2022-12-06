function mostrarSenha(){

	var tipo = document.getElementById('senha');
	const btn = document.querySelector('.icon');

	if (tipo.type == 'password') 
	{
		tipo.type = 'text'
		btn.src = 'static/imagens/eye-off.svg'
	}
	else
	{
		tipo.type = 'password'
		btn.src = 'static/imagens/eye.svg'
	}
}

function mostrarSenha1(){

	var tipo = document.getElementById('senha');
	const btn = document.querySelector('.icon');

	if (tipo.type == 'password') 
	{
		tipo.type = 'text'
		btn.src = '/static/imagens/eye-off.svg'
	}
	else
	{
		tipo.type = 'password'
		btn.src = '/static/imagens/eye.svg'
	}
}

function mostrarSenha2(){

	var tipo1 = document.getElementById('senha1');
	const btn = document.getElementById('icon');

	if (tipo1.type == 'password') 
	{
		tipo1.type = 'text'
		btn.src = '/static/imagens/eye-off.svg'
	}
	else
	{
		tipo1.type = 'password'
		btn.src = '/static/imagens/eye.svg'
	}
}


function mostrarSenha3(){

	var tipo2 = document.getElementById('senha2');
	const btn = document.getElementById('icon');

	if (tipo2.type == 'password') 
	{
		tipo2.type = 'text'
		btn.src = '/static/imagens/eye-off.svg'
	}
	else
	{
		tipo2.type = 'password'
		btn.src = '/static/imagens/eye.svg'
	}
}


function mostrarSenha4(){

	var tipo3 = document.getElementById('senha3');
	const btn = document.getElementById('icon1');

	if (tipo3.type == 'password') 
	{
		tipo3.type = 'text'
		btn.src = '/static/imagens/eye-off.svg'
	}
	else
	{
		tipo3.type = 'password'
		btn.src = '/static/imagens/eye.svg'
	}
}