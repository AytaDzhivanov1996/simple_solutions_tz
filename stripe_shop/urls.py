from django.urls import path

from stripe_shop.views import CancelView, ItemDetailView, SessionCreateAPIView, SuccessView

app_name = "items"

urlpatterns = [
    path('buy/<int:pk>/', SessionCreateAPIView.as_view(), name="create-checkout-session"),
    path('item/<int:pk>/', ItemDetailView.as_view()),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]