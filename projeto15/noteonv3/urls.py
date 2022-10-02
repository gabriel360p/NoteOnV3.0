from django.urls import path
from . import views

app_name="noteonv3"

urlpatterns=[
	#página index
	path('',views.index,name="index"),
	
	#página de login
	path('login/',views.viewtlogin,name="tlogin"),

	#página de registro
	path('registro/',views.viewtregistro,name="tregistro"),
	
	#página de perfil
	path('perfil/<int:id>',views.viewtperfil,name="tperfil"),
	
	#página onde se ver as anotações
	path('livraria/<int:id>',views.viewlivraria,name="tlivraria"),


	#página de editar informações perfil (so a pagina)
	path('editperfil/<int:id>',views.vieweditperfil,name="teditperfil"),
	
	#página de editar criar uma nova anotação
	path('nvnota/<int:id>',views.viewnvnota,name="tnvnota"),

	#botão para ir até página de editar anotação
	path('vieweditnota/<int:id> <int:id2>',views.vieweditnota,name="vieweditnota"),






	#botão de fazer cadastro de usuário
	path('btnregistro/',views.btnregistro,name="btnregistro"),
	
	#botão de fazer o login de usuário
	path('btnlogin/',views.btnlogin,name="btnlogin"),
	
	#botão de confirmar a edição de dados do perfil
	path('btneditar/<int:id>',views.btneditar,name="btneditar"),

	#botão de deletar a conta
	path('btndeletarconta/<int:id>',views.btndeletarconta,name="btndeletarconta"),
	
	#botão de salvar uma nova anotação
	path('btnnvnota/<int:id>',views.btnnvnota,name="btnnvnota"),

	#botão para deletar uma anotação
	path('btndeletenota/<int:id> <int:id2>',views.btndeletenota,name="btndeletenota"),
	
	#botão para salvar uma edição de anotação
	path('btnsaveedinota/<int:id> <int:id2>',views.btnsaveedinota,name="btnsaveedinota"),
]
