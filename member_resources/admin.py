from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ArrangedPart)
admin.site.register(models.ChoirMember)
admin.site.register(models.Version)
admin.site.register(models.Song)
admin.site.register(models.SongPart)
admin.site.register(models.SongPartSungBy)
admin.site.register(models.SongPartRecording)
