from django.db import models

class State(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=255
    )
    state = models.ForeignKey(
        State, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name




