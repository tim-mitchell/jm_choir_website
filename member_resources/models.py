from django.db import models

# Create your models here.


class ArrangedPart(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Version(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ChoirMember(models.Model):
    name = models.CharField(max_length=200)
    part = models.ForeignKey(ArrangedPart, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        part = self.part
        if part is not None:
            return '{} (sings {})'.format(self.name, part)
        else:
            return self.name


class SongPart(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    part = models.ForeignKey(ArrangedPart, on_delete=models.CASCADE)
    score = models.FileField(upload_to='scores', blank=True)

    class Meta:
        unique_together = ('song', 'part')

    def __str__(self):
        return '{}: {}'.format(self.song.name, self.part.name)


class SongPartRecording(models.Model):
    song_part = models.ForeignKey(SongPart, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    filename = models.FileField(upload_to='recordings')

    class Meta:
        unique_together = ('song_part', 'version')

    def __str__(self):
        return '{}: {}'.format(self.song_part, self.version.name)


class SongPartSungBy(models.Model):
    song_part = models.ForeignKey(SongPart, on_delete=models.CASCADE)
    choir_member = models.ForeignKey(ChoirMember, on_delete=models.CASCADE)

    def __str__(self):
        return '{} sung by {}'.format(self.song_part, self.choir_member.name)
