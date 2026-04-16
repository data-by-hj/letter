from django.urls import path
from . import views

urlpatterns = [
    # 인증
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    
    # 홈/방 관리
    path('home/', views.home, name='home'),
    path('home/setting/', views.setting, name='setting'),
    path('home/add_room/', views.add_room, name='add_room'),
    
    # 방/편지
    path('home/<int:room_id>/', views.room_detail, name='room_detail'),
    path('home/<int:room_id>/write/', views.letter_write, name='letter_write'),
    path('home/<int:room_id>/<int:letter_id>/', views.letter_detail, name='letter_detail'),
    path('home/<int:room_id>/<int:letter_id>/update/', views.letter_update, name='letter_update'),
    path('home/<int:room_id>/<int:letter_id>/delete/', views.letter_delete, name='letter_delete'),
    
    # 댓글
    path('home/<int:room_id>/<int:letter_id>/comment/add/', views.comment_add, name='comment_add'),
    path('home/<int:room_id>/<int:letter_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]