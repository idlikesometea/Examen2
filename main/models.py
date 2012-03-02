from django.db import models


class Zombie(models.Model):
    name = models.CharField(max_length=20)
    cemetery = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class Twit(models.Model):
    status = models.CharField(max_length=140)
    zombie = models.ForeignKey('Zombie', related_name='twits')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.status
