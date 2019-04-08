from rest_framework import routers
# from core import views as myapp_views
from .urls import *


router = routers.DefaultRouter()
router.register(r'^friends/$', urlpatterns.FriendViewset)
router.register(r'^belongings/$', urlpatterns.BelongingViewset)
router.register(r'^borrowings/$', urlpatterns.BorrowedViewset)