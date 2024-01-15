from rest_framework.routers import DefaultRouter
from .views import StoreAPIView, ProductAPIView

router = DefaultRouter()
router.register('stores', StoreAPIView)
router.register('products', ProductAPIView)

urlpatterns = [

]
urlpatterns += router.urls
