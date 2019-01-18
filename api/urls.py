from django.conf.urls import url
from .views import DetailsPostView
from rest_framework.urlpatterns import format_suffix_patterns


# urlpatterns = [
    
#     url(r'^post/(?P<pk>[0-9]+)/$',
#         DetailsPostView.as_view(),
#         name='post_details'),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)