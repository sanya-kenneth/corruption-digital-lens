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
    notes = models.TextField(null=True, blank=True)
    interplay = models.TextField(null=True)
    corruption_form = models.ManyToManyField(CorruptionForm, related_name='acts')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    act = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='act', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def ___str__(self):
        return f"{self.comment[:15]} {self.created_at}"
    

class Incident(models.Model):
    form_of_corruption = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()
    email = models.EmailField()

    
class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        (0, "Bug Report"),
        (1, "Feature Request"),
        (2, "General Feedback"),
        (3, "Compliment"),
        (4, "Complaint")
        ]
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    feedback_type = models.SmallIntegerField(choices=FEEDBACK_CHOICES, default=2)
    message = models.TextField()
    
    def __str__(self):
        _type = "Bug report" if self.feedback_type == 0 else "Feature request" if\
            self.feedback_type == 1 else "General Feedback" if self.feedback_type == 2 else\
                "General Feedback" if self.feedback_type == 2 else "Compliment" if self.feedback_type == 3 else "Complaint"
        return f"{self.name}_{_type}_{self.message[:30]}"
