from functools import cache

from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from Human.templatetags.news_tags import register
from Human.views import HomeHumans, HumansByCategory, AddHumans, register, user_login, user_logout

# from Human.views import index, get_category, view_human, add_human, test


urlpatterns = [
    # path('', index, name='Home'),
    # path('category/<int:category_id>', get_category, name='Category'),
    # path('human/<int:human_id>', view_human, name='view_human'),
    # path('human/add_human', add_human, name='add_human'),
    # path('test/', test, name='Test'),
    path('admin/', admin.site.urls),
    path('',HomeHumans.as_view(),  name='Home'),
    path('category/<int:category_id>/', HumansByCategory.as_view(), name='Category'),
    path('human/<int:pk>/', HumansByCategory.as_view(), name='view_human'),
    path('human/add_human', AddHumans.as_view(), name='add_human'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout')
]

