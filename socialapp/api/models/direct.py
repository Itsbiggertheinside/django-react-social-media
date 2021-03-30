from django.db import models
from .profile import Profile


class DirectChannel(models.Model):
    creater = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='directs')
    invited = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='invited_directs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.creater.user.username, self.invited.user.username)


class Message(models.Model):
    room = models.ForeignKey(DirectChannel, on_delete=models.PROTECT, related_name='messages')
    sender = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='senders')
    message = models.CharField(max_length=2400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.sender, self.message)

    class Meta:
        ordering = ('timestamp',)