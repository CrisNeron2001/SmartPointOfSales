from unicodedata import name
from django.urls import path 
from .views import form_del_cliente, form_del_medio_pago, form_del_producto, form_del_medio_pago, form_del_venta, form_mod_medio_pago, form_mod_producto, form_mod_venta, home, form_cliente, form_detalle_venta, form_medio_pago, form_mod_cliente, form_producto, form_producto, form_venta, home_cliente, home_detalle_venta, home_medio_pago, home_producto, home_producto, home_venta

urlpatterns = [
    #Home
    path('', home, name="home"),
    path('home_cliente', home_cliente, name="home_cliente"),
    path('home_producto', home_producto, name="home_producto"),
    path('home_medio_pago', home_medio_pago, name="home_medio_pago"),
    path('home_venta', home_venta, name="home_venta"),
    path('home_detalle_venta', home_detalle_venta, name="home_detalle_venta"),
    #Formulario
    path('form_cliente', form_cliente, name="form_cliente"),
    path('form_producto', form_producto, name="form_producto"),
    path('form_medio_pago', form_medio_pago, name="form_medio_pago"),
    path('form_venta', form_venta, name="form_venta"),
    path('form_detalle_venta', form_detalle_venta, name="form_detalle_venta"),
    #Formulario modificacion
    path('form_mod_cliente/<id_cliente>', form_mod_cliente, name="form_mod_cliente"),
    path('form_mod_producto/<id_producto>', form_mod_producto, name='form_mod_producto'),
    path('form_mod_medio_pago/<id_medio_pago>', form_mod_medio_pago, name="form_mod_medio_pago"),
    path('form_mod_venta/<id_venta>', form_mod_venta, name="form_mod_venta"),
    #Formulario eliminacion
    path('form_del_cliente/<id_cliente>', form_del_cliente, name="form_del_cliente"),
    path('form_del_producto/<id_producto>', form_del_producto, name="form_del_producto"),
    path('form_del_medio_pago/<id_medio_pago>', form_del_medio_pago, name="form_del_medio_pago"),
    path('form_del_venta/<id_venta>', form_del_venta, name="form_del_venta")
]

