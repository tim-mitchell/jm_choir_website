from django import http, shortcuts
from django.views import generic

from . import models


def render(request, name, context):
    return shortcuts.render(request, ns_template(name), context)


def ns_template(name):
    return 'member_resources/{}'.format(name)


# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})


def song_list_view(request):
    songs = models.Song.objects.order_by('name')
    context = {'song_list': songs}
    return render(request, 'song_list.html', context)


def choir_member_list_view(request):
    choir_members = models.ChoirMember.objects.order_by('name')
    context = {'choir_member_list': choir_members}
    return render(request, 'choir_member_list.html', context)


def choir_member_view(request, choir_member_id):
    choir_member = shortcuts.get_object_or_404(models.ChoirMember, pk=choir_member_id)
    song_part_recording_list = models.SongPartRecording.objects.filter(song_part__part_id=choir_member.part.id)
    song_part_list = models.SongPart.objects.filter(pk=choir_member.part.id)
    context = {'choir_member': choir_member,
               'song_part_recording_list': song_part_recording_list,
               'song_part_list': song_part_list}
    return render(request, 'choir_member.html', context)


class SongListView(generic.ListView):
    model = models.Song

    def get_queryset(self):
        return models.Song.objects.order_by('name')


class SongView(generic.DetailView):
    model = models.Song
