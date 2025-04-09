"""
URL configuration for recipes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import SimpleRouter
from menu import views
from rest_framework.authtoken import views as view1


router=SimpleRouter()
router.register('recipes',views.RecipeView)
router.register('register',views.UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('register/',include(router.urls)),
    path('filterbycusine',views.FilterByCuisine.as_view()),
    path('filterbyingredients',views.FilterByIngredients.as_view()),
    path('filterbymeal',views.FilterByMealType.as_view()),
    path('search',views.SearchRecipe.as_view()),
    path('login/', view1.obtain_auth_token),
    path('logout',views.LogoutView.as_view()),
    path('add_review/',views.CreateReview.as_view()),
    path('getreview/<int:pk>',views.GetAllReviews.as_view()),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
