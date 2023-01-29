from django.db import models
import uuid


class Technology(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length=155)
    index = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_index = Technology.objects.all().aggregate(
                largest=models.Max("index")
            )["largest"]
            if last_index is not None:
                self.index = last_index + 1

        super(Technology, self).save(*args, **kwargs)
