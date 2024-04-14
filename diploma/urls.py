"""
URL configuration for diploma project.

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
from django.urls import path,include
from django.conf.urls.static import static,settings
from user import views as u
from expense import views as e

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('login/', u.LoginUser.as_view(), name='login'),
                  path('register/', u.RegisterUser.as_view(), name='register'),
                  path('profile/', u.profile, name='profile'),
                  path('expenses/', e.expenses, name='expenses'),
                  path('update_expense/<int:id>/', e.update_expense, name='update_expense'),
                  path('delete_expense/<int:id>/', e.delete_expense, name='delete_expense'),
                  path('pdf/', e.pdf, name='pdf'),
                  path('financial_statistics/', e.financial_statistics, name='financial_statistics'),
                  path('diagrams/', e.diagrams, name='diagrams'),
                  path('goals/', e.goals, name='goals'),
                  path('home/', e.home, name='home'),

                  path('delete_goal/<int:goal_id>/', e.delete_goal, name='delete_goal'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)