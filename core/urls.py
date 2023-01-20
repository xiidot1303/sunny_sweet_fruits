from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from app.views import main


urlpatterns = [
    # login
    path('control/', admin.site.urls),

    # main
    path('', main.pages),
    path('<str:page>/', main.pages),
    path('change-lang/<int:lang>/', main.change_lang, name='change_lang'),

    path('category/<int:pk>/', main.category, name='category'),
    path('sub-category/<int:pk>/', main.sub_category, name='sub_category'),

    # files
    re_path(r'^files/(?P<path>.*)$', main.get_file)
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
