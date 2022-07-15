from django.urls import path
from .views import connexion, deconnexion, inscription, user_profile, edit_user, phone_verification, token_validation, verified


app_name = "parametres"

urlpatterns = [
    path('connexion/', connexion, name="connexion"),
    path('inscription/', inscription, name="inscription"),
    path('profile/<str:pk>/', user_profile, name='user_profile'),
    path('edit_profile/', edit_user, name='edit_user'),
    path('deconnexion/', deconnexion, name="deconnexion"),

    path('verification/', phone_verification, name='phone_verification'),  # noqa: E501
    path('verification/token/', token_validation, name='token_validation'),  # noqa: E501
    path('verified/', verified, name='verified'),
]