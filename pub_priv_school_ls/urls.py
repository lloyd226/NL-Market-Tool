from django.urls import path, register_converter
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .converters import FloatConverter

register_converter(FloatConverter, 'float')

app_name = "pub_priv_school_ls"
urlpatterns = [
    path("" , views.index, name="index"),
    path("area/<str:loc>/" , views.area, name="area"),
    path("list/<str:radius>/<float:latitude>/<float:longitude>/<str:loc>/", views.list, name="list")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)