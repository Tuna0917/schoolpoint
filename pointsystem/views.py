from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import *
from .models import *
# Create your views here.

#Create Room
'''
어떻게 만들어야 잘 만들었다고 소문이 날까
줄 갯수 입력하고 좌석 갯수 정하면 될려나
'''
def home(request):
    context = {
        'total_room' : Room.objects.count(),
        'total_seat' : Seat.objects.count()
    }


    return render(request, 'home.html', context=context)


def create_room(request):
    if request.method == 'POST':
        if Room.objects.filter(grade=request.POST['grade'],num=request.POST['num']):
            print('이미있음')
            return redirect('home')

        new_room = Room.objects.create(grade=request.POST['grade'],num=request.POST['num'],line=request.POST['line'])
        for i in range(int(request.POST['seats'])):
            Seat.objects.create(room=new_room)
        return redirect('home')
    else:
        return render(request, 'create_room.html')

class RoomListView(ListView):
    model = Room

class RoomDetailView(DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['seats'] = Seat.objects.filter(room=context['object']).all()
        return context