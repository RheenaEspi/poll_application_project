from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_rigister/', views.login_rigister, name='login_rigister'),

    path('check_the_otp/', views.check_the_otp, name='check_the_otp'),
    path('save_the_user_info/', views.save_the_user_info, name='save_the_user_info'),

    path('logout/', views.logout, name='logout'),
    path('check_login_info/', views.check_login_info, name='check_login_info'),

    path('forget_pass/', views.forget_pass, name='forget_pass'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),

    path('type_reset_pass/', views.type_reset_pass, name='type_reset_pass'),

    path('savereset_pass/', views.savereset_pass, name='savereset_pass'),

    path('go_for_poll/', views.go_for_poll, name='go_for_poll'),
    path('Vice_President_vote/', views.Vice_President_vote, name='Vice_President_vote'),
    path('Vice_President_result/', views.Vice_President_result, name='Vice_President_result'),
    path('President_vote/', views.President_vote, name='President_vote'),
    path('President_result/', views.President_result, name='President_result'),
    path('Senator_vote/', views.Senator_vote, name='Senator_vote'),
    path('Senator_result/', views.Senator_result, name='Senator_result'),

    path('save_the_v_p_v/', views.save_the_v_p_v, name='save_the_v_p_v'),
    path('save_the_president_v/', views.save_the_president_v, name='save_the_president_v'),
    path('save_the_sanetor_v/', views.save_the_sanetor_v, name='save_the_sanetor_v'),

    path('profile/', views.profile, name='profile'),
    path('lets_save/', views.lets_save, name='lets_save'),


]