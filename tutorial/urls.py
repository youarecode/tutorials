"""
URL configuration for portfolio_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
import webapp.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', webapp.views.hello_world),
    path('age/<int:age_today>/<int:year>',  webapp.views.compute_age),
    path('machine_learning/',  webapp.views.machine_learning),
    path('control_theory/',  webapp.views.control_theory),
    path('search_product/',  webapp.views.search_products),
    path('search/',  webapp.views.search),

    path('',                include('webapp.urls')),
    path('services/',       include('services_app.urls')),
    path('blog/',           include('blog_app.urls')),
    path('contact/',        include('contact_app.urls')),
    path('store/',          include('store_app.urls')),
    path('cart/',           include('cart_app.urls')),
    path('authentication/', include('authentication_app.urls')),


]





urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)