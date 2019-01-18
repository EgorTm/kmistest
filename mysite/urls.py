"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from blog.models import Post

from django.db import models
from django.utils import timezone


from rest_framework import generics
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),
#     url(r'^api-auth/', include('rest_framework.urls'))
# ]


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date')



class DetailsPostView(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    queryset = Post.objects.all()
    serializer_class = PostSerializer





# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'post', DetailsPostView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]