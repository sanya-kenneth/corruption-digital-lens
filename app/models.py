from django.db import models


class CorruptionForm(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = "Corruption forms"

    def __str__(self):
        return self.name


class Factor(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    corruption_form = models.ManyToManyField(CorruptionForm, related_name='factors')

    def __str__(self):
        return self.name


class Act(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    notes = models.TextField(null=True)
    interplay = models.TextField(null=True)
    corruption_form = models.ManyToManyField(CorruptionForm, related_name='acts')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def ___str__(self):
        return f"{self.comment[:15]} {self.created_at}"
    

class Incident(models.Model):
    form_of_corruption = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()
    email = models.EmailField()
