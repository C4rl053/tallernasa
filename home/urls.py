from django.urls import path
from .views import *

urlpatterns = [
	path('about/',vista_about, name='vista_about'),
	path('contacto/',vista_contacto, name='vista_contacto'),
	path('lista_repuesto/',vista_lista_repuesto, name='vista_lista_repuesto'),
	path('lista_accesorio/',vista_lista_accesorio, name='vista_lista_accesorio'),
	
	path('ver_repuesto/<int:id_prod>/',vista_ver_repuesto, name='vista_ver_repuesto'),
	path('ver_accesorio/<int:id_prod>/',vista_ver_accesorio, name='vista_ver_accesorio'),

	                            #CRUD agregar, editar y eliminar
	#CRUP PARA REPUESTOS:
	path('agregar_repuesto/',vista_agregar_repuesto, name='vista_agregar_repuesto'),
	path('editar_repuesto/<int:id_prod>/',vista_editar_repuesto, name='vista_editar_repuesto'),
	path('eliminar_repuesto/<int:id_prod>/',vista_eliminar_repuesto, name='vista_eliminar_repuesto'),

	#CRUD PARA ACCESORIOS:
	path('agregar_accesorio/',vista_agregar_accesorio, name='vista_agregar_accesorio'),
	path('editar_accesorio/<int:id_prod>/',vista_editar_accesorio, name='vista_editar_accesorio'),
	path('eliminar_accesorio/<int:id_prod>/',vista_eliminar_accesorio, name='vista_eliminar_accesorio'),

	#LOGIN DE REGISTRO
#	path('login/',vista_login, name='vista_login'),
#	path('logout/',vista_logout, name='vista_logout'),
#	path('registrar/',vista_register, name='vista_register'),

	
]