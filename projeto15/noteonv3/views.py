from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404 as error404
from django.http import HttpResponse
from . import urls
from .models import tb_users,tb_notas

#pagina inicial
def index(request):
	return render(request,'index.html')
#pagina de login
def viewtlogin(request):
	return render(request,'tlogin.html')
#pagina de registro de usuário
def viewtregistro(request):
	return render(request,'tregistro.html')
#pagina onde se ver as informações do usuário
def viewtperfil(request,id):
	traz=tb_users.objects.get(pk=id)
	return render(request,'tperfil.html',{'dados':traz})
#página onde editamos as informações do usuário
def vieweditperfil(request,id):
	dadosPerfil=tb_users.objects.get(pk=id)
	return render(request,'teditperfil.html',{'dadosPerfil':dadosPerfil})
#página onde vemos as anotações
def viewlivraria(request,id):
	dados=tb_users.objects.get(pk=id)
	notas=tb_notas.objects.all()
	return render(request,'tlivraria.html',{'dadosPerfil':dados,'anotacoes':notas})
#página onde escrevo uma nova as anotação
def viewnvnota(request,id):
	dados=tb_users.objects.get(pk=id)
	return render(request,'tnvnota.html',{'dadosPerfil':dados})

#registro de usuário:
def btnregistro(request):
	if request.method=="POST":
		email=request.POST.get('email')
		usersemail = tb_users.objects.filter(email=email)
		if not usersemail:
			nome=request.POST.get('nome')
			email=request.POST.get('email')
			senha=request.POST.get('senha')
			numero=request.POST.get('numero')
			nvusuario=tb_users(name=nome,email=email,passw=senha,number=numero)
			nvusuario.save()
			return render(request,'tlogin.html')
		else:
			return render(request,'tregistro.html',{'ExistsAlert':"Email já cadastrado"})
	else:
		return redirect('noteonv3:tlogin')


def btnlogin(request):
	if request.method=="POST":
		email=request.POST.get('email')
		senha=request.POST.get('senha')
		try:
			recupera=error404(tb_users,email=email)
		except:
			return render(request,'tlogin.html',{'EmailAlert':"Email Não Reconhecido"})

		if recupera.passw == senha:
			return render(request,'tperfil.html',{'dados':recupera})
		else:
			return render(request,'tlogin.html',{'SenhaAlert':"Senha não Reconhecida"})
	else:
		return render(request,'tlogin.html')

def btneditar(request,id):
	if request.method=="POST":
		user=tb_users.objects.get(pk=id)
		user.name=request.POST.get('nome')
		
		user.email=request.POST.get('email')
		user.number=request.POST.get('numero')

		user.passw=request.POST.get('senha')
		user.save()
		
		user=tb_users.objects.get(pk=id)
		return render(request,'tperfil.html',{'dados':user})
	else:
		return HttpResponse("Acesso Get Negado")

def btndeletarconta(request,id):
	#deletando usuário
	user=tb_users.objects.get(pk=id)
	user.delete()
	return redirect('noteonv3:index')

def btnnvnota(request,id):
	if request.method=="POST":
		titulo=request.POST.get('titulo')
		subtitulo=request.POST.get('subtitulo')
		texto=request.POST.get('texto')
		cor=request.POST.get('cor')
		nvnota=tb_notas(title=titulo,subtitle=subtitulo,text=texto,cor=cor)
		nvnota.save()
		perfil=tb_users.objects.get(pk=id)
		notas=tb_notas.objects.all()

		return render(request,'tlivraria.html',{'dadosPerfil':perfil,'anotacoes':notas})

def btndeletenota(request,id,id2):
	#tratando erros graves!! DEU CERTOOOOOOOOOOOOOOOOOOO!!
	try:
		nota=tb_notas.objects.get(pk=id)
		nota.delete()
		notas=tb_notas.objects.all()
		user=tb_users.objects.get(pk=id2)
		return render(request,'tlivraria.html',{'anotacoes':notas,'dadosPerfil':user})
	except:
		notas2=tb_notas.objects.all()
		user2=tb_users.objects.get(pk=id2)
		return render(request,'tlivraria.html',{'anotacoes':notas2,'dadosPerfil':user2})
		
def vieweditnota(request,id,id2):
	nota=tb_notas.objects.get(pk=id)
	user=tb_users.objects.get(pk=id2)
	return render(request,'teditnota.html',{'anotacao':nota,'dadosPerfil':user})

def btnsaveedinota(request,id,id2):
	nota=tb_notas.objects.get(pk=id)
	nota.title=request.POST.get('titulo')
	nota.subtitle=request.POST.get('subtitulo')
	nota.text=request.POST.get('texto')
	nota.cor=request.POST.get('cor')
	nota.save()
	user=tb_users.objects.get(pk=id2)
	notas=tb_notas.objects.all()
	return render(request,'tlivraria.html',{'anotacoes':notas,'dadosPerfil':user})
