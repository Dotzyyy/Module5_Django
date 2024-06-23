from django.db import models

from django.contrib.auth.models import User



class PrivateMessage(models.Model):
    
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    cc = models.ManyToManyField(User, related_name='cc_messages', blank=True)
    subject = models.CharField(max_length=260)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.author} to {self.recipient}'