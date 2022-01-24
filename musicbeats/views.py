from django.shortcuts import render
from .models import Singer , Playlist , Song, Hesohal,Album



# Create your views here.

def playLists(request):
    playlists=Playlist.objects.all()
    context={
        'playlists':playlists
    }
    return render(request,'musicbeats/playlist.html',context)


def singers(request):
    singers = Singer.objects.all()
    context ={
        'singers':singers
    }
    return render(request,'musicbeats/archive-singer.html',context)

def singer(request,pk):
    singerObj = Singer.objects.get(id=pk)
    context={'singer':singerObj}
    return render(request,'musicbeats/single-singer.html',context)
def play(request,pk):
    songObj=Song.objects.get(id=pk)


    context={
        'song':songObj
    }
    return render(request,'musicbeats/player.html',context)

def single_hesohal(request,pk):
    hesohalObj= Hesohal.objects.get(id=pk)
    songs = Song.objects.all()
    albums = Album.objects.all()

    context ={
        'hesohal':hesohalObj,
        'songs':songs,
        'albums':albums
    }
    return render(request,'musicbeats/single-hesohal.html',context)

