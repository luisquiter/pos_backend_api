from django.urls import path

from . import views

urlpatterns = [
    path('mesa',views.MesaView.as_view()),
    path('Categoria',views.CategoriaView.as_view()),
    path('plato',views.PlatoView.as_view()),
    path('categoria/<int:categoria_id>/platos',views.CategoriaPlatosView.as_view()),
    path('pedido',views.PedidoRegisterView.as_view()),
    path('pedido/get',views.PedidoDashboardView.as_view())
]