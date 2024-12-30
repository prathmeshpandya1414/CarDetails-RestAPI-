from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('car', views.Car_ViewSet)
router.register('showroom', views.Showroom_ViewSet, basename='Showroom_View')
# router.register('review', views.Review_ViewSet)



urlpatterns = [
    path('list', views.car_list, name='car_list'),
    path('<int:pk>', views.car_detail_view, name='car_detail'),
    path('', include(router.urls)),
    # path('showroom', views.Showroom_View.as_view(), name='showroom_View'),
    # path('showroom/<int:pk>', views.Showroom_detail.as_view(), name='showroom_details'),
    # path('review', views.ReviewList.as_view(), name='review_list'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('showroom/<int:pk>/review-create', views.ReviewCreate.as_view(), name='review_create'),
    path('showroom/<int:pk>/review', views.ReviewList.as_view(), name='review_list'),
    path('showroom/review/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
]