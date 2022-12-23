from django.urls import path
from . import views


app_name = "website"
urlpatterns = [
    path('', views.index, name='index'),
    path('convert', views.convert_file, name='convert'),
    path('qrcode', views.qrcode, name='qrcode'),
    path('about_us', views.about_us, name='about_us'),
    path('p_generator', views.p_generator, name='p_generator'),
]
