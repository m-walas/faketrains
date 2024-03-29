from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Bilety_i_pociagi.views import (
    TicketList,
    city_search_view,
    user_profile,
    logout_view,
    user_status,
    register_view,
    receive_selected_route,
    get_train_seats_with_availability,
    ReserveTicketView,
    confirm_reservation,
    stripe_webhook,
    update_ticket_status,
    cancel_reservation_status,
    CreateStripeSessionView,
    ListAPIEndpoints,
    index,
    SignUpView,
    search_trains,
)

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),

    # django login and logout
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name="logout"),

    # admin panel
    path('admin/', admin.site.urls),

    # API Endpoints
    path('endpoints/', ListAPIEndpoints.as_view(), name='endpoints'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tickets/', TicketList.as_view(), name='ticket-list'),
    path('api/cities/', city_search_view, name='city-search'),
    path('api/search_trains/', search_trains, name='search_trains'),

    # user auth
    path('api/user/register', register_view, name='register'),
    path('api/user/logout', logout_view, name='logout'),
    path('api/user/status', user_status, name='user_status'),
    path('api/user/profile/', user_profile),

    # reservation process 
    path('api/receive_route', receive_selected_route, name='receive_selected_route'),
    path('api/get_train_seats_with_availability/<str:train_id>/<str:departure_date>/<str:departure_time>/', get_train_seats_with_availability, name='get_train_seats_with_availability'),
    path('api/reserve_seats/', ReserveTicketView.as_view(), name='reserve_seats'),
    path('api/confirm_reservation/', confirm_reservation, name='confirm_reservation'),

    # Stripe payment
    path('api/create_stripe_session/', CreateStripeSessionView.as_view(), name='create_stripe_session'),
    path('stripe/update_ticket_status/', update_ticket_status, name='update_ticket_status'),
    path('stripe/cancel_reservation_status/', cancel_reservation_status, name='cancel_reservation_status'),
    path('wh/stripe_webhook/', stripe_webhook, name='stripe_webhook'),
]
