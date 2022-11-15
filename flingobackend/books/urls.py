from django.urls import re_path as url
from books import views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    url(r'^book$',views.bookApi),
    url(r'^book/([0-9]+)$',views.bookApi),
    url(r'^book/savefile',views.SaveFile)



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
