from django.db import models
from .profile import Profile


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='receiver')
    message = models.CharField(max_length=2400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.sender, self.message)

    class Meta:
        ordering = ('timestamp',)