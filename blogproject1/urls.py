
from django.contrib import admin
from django.urls import path, include
import blogprojectapp.views
import portfolio.views
#Medai파일 url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogprojectapp.views.home, name="home"),
    path('blog/',include('blogprojectapp.urls')),
    path('blog/portfolio',portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
