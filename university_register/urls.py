from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from app.views import LoginView, IndexView, sign_out
from university_register.api import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', sign_out, name='logout'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
