from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        room = request.POST.get('room', 'general').strip()
        if not username:
            return render(request, 'chat/index.html', {'error': 'Ism kiriting!'})
        return redirect(f'/chat/{room}/?username={username}')
    return render(request, 'chat/index.html')


def room(request, room_name):
    username = request.GET.get('username', 'Anonim')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': username,
    })
