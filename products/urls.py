
from django.urls import path
from .views import create, detail, upvote

# apps = 'accounts'

urlpatterns = [
    path('create', create, name= 'create'),
    path('<int:product_id>', detail, name= 'detail'),
    path('<int:product_id>/upvote', upvote, name= 'upvote'),

]
