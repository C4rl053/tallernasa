from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.

#VISTAS Y FUNCIONES PARA EL LOGIN
def vista_login(request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/about/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout(request):
	logout(request)
	return redirect('/login/')

def vista_register(request):
	formulario = register_form()
	if request.method== 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'register.html', locals())
		else:
			return render(request, 'registro.html', locals())
	return render(request, 'registro.html', locals())

def vista_about(request):
	return render(request,'about.html')

def vista_contacto(request):
	info_enviado=False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
	else:
		formulario = contacto_form()		
	return render(request,'contacto.html', locals())

	#VISTAS Y FUNCIONES PARA ACCESORIOS

def vista_lista_accesorio(request):
	lista = Accesorio.objects.filter()
	return render(request, 'lista_accesorio.html', locals())

def vista_agregar_accesorio(request):
	if request.method == "POST":
		formulario = agregar_accesorio_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_accesorio/')
	else:
		formulario = agregar_accesorio_form()		
	return render(request, 'vista_agregar_accesorio.html', locals())

def vista_ver_accesorio(request, id_prod):
	p = Accesorio.objects.get(id=id_prod)
	return render(request,'ver_accesorio.html',locals())	

def vista_editar_accesorio(request, id_prod):
	prod = Accesorio.objects.get(id=id_prod)
	if request.method == 'POST':
		formulario = agregar_accesorio_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			return redirect ('/lista_accesorio/')
	else:
		formulario = agregar_accesorio_form(instance = prod)
	return render(request, 'vista_agregar_accesorio.html', locals())

def vista_eliminar_accesorio(request, id_prod):
	prod = Accesorio.objects.get(id=id_prod)
	prod.delete()
	return redirect('/lista_accesorio/')



	#VISTAS Y FUNCIONES PARA REPUESTOS//////////////////////////////////////////////////////////
def vista_lista_repuesto(request):
	lista = Repuesto.objects.filter()
	return render(request, 'lista_repuesto.html', locals())

def vista_agregar_repuesto(request):
	if request.method == "POST":
		formulario = agregar_repuesto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_repuesto/')
	else:
		formulario = agregar_repuesto_form()		
	return render(request, 'vista_agregar_repuesto.html', locals())

def vista_ver_repuesto(request, id_prod):
	p = Repuesto.objects.get(id=id_prod)
	return render(request,'ver_repuesto.html',locals())	

def vista_editar_repuesto(request, id_prod):
	prod = Repuesto.objects.get(id=id_prod)
	if request.method == 'POST':
		formulario = agregar_repuesto_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			return redirect ('/lista_repuesto/')
	else:
		formulario = agregar_repuesto_form(instance = prod)
	return render(request, 'vista_agregar_repuesto.html', locals())

def vista_eliminar_repuesto(request, id_prod):
	prod = Repuesto.objects.get(id=id_prod)
	prod.delete()
	return redirect('/lista_repuesto/')




















