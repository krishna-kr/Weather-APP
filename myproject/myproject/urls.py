from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from . import routers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/', views.EmployeeList.as_view()),
    url(r'^api/v1/', include(routers.urls)),

]
