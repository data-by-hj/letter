from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .models import Room, RoomMember, Letter, Comment


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        #로그인 처리
        username = request.POST.get('username')
        password  = request.POST.get('password')

        #사용자 확인
        user = authenticate(request, username= username, password=password)

        #로그인 이후
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 틀렸습니다'})
    else:
        return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def signup_view(request):
    if request.method =='POST':
        name = request.POST.get('lastname')
        username = request.POST.get('username')
        password  = request.POST.get('password')
        
        user = User.objects.create_user(last_name= name, username= username, password=password)

        return redirect('login')

@login_required  #로그인 필수
def home(request):
    my_rooms = RoomMember.objects.filter(user=request.user)
    rooms = [member.room for member in my_rooms]

    return render(request, 'home.html', {'rooms': rooms})

@login_required 
def setting(request):
    if request.method == "POST":
        name = request.POST.get('lastname')
        password  = request.POST.get('password')

        request.user.last_name = name
        request.user.set_password(password)
        request.user.save()
        update_session_auth_hash(request, request.user) 

        return redirect('home')
    
@login_required 
def add_room(request):
    if request.method == "POST":
        room_name = request.POST.get('room_name')
        room = Room.objects.create(name = room_name, created_by=request.user)
        RoomMember.objects.create(room_id = room, user_id= request.user)
        
        return redirect('home')

@login_required
def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    letters = Letter.objects.filter(room=room)
        
    return render(request, 'room_detail.html', {'letters':letters, 'room': room})

@login_required
def letter_write(request, room_id):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        anniversary = request.POST.get("anniversary")
        image = request.FILES.get("image")
        room = Room.objects.get(id= room_id)
        Letter.objects.create(room = room, 
                              title = title, content= content, 
                              anniversary= anniversary, image= image, 
                              author= request.user)
        return redirect('room_detail', room_id=room_id)
    else : #GET일때
        return render(request, 'letter_write.html', {'room_id': room_id})
