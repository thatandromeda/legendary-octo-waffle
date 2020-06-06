from django.db import models

class Action(models.Model):
    call_to_action  = models.CharField(max_length=100)
    link            = models.URLField()
    description     = models.TextField()
    citation        = models.URLField(blank=True)

    def __str__(self):
        return self.call_to_action
