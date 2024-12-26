from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('login/', views.user_login, name='login'),

#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', views.pagelogout, name='logout'),

#     path('password-change/', auth_views.PasswordChangeView.as_view(),
#          name='password_change'),
#     path('password-change/done/',
#          auth_views.PasswordChangeDoneView.as_view(),
#          name='password_change_done'),

#      path('password-reset/',
#           auth_views.PasswordResetView.as_view(),
#           name='password_reset'),
#      path('password-reset/done/',
#           auth_views.PasswordResetDoneView.as_view(),
#           name='password_reset_done'),
#      path('password-reset/<uidb64>/<token>/',
#           auth_views.PasswordResetConfirmView.as_view(),
#           name='password_reset_confirm'),
#      path('password-reset/complete/',
#           auth_views.PasswordResetCompleteView.as_view(),
#           name='password_reset_complete'),

     path('', include('django.contrib.auth.urls')),
     path('', views.dashboard, name='dashboard'),
     path('refister/', views.register, name='register'),
     path('edit/', views.edit, name='edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)