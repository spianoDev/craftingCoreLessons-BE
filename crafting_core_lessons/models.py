from django.db import models

# model for the lesson template:
class Lesson(models.Model):
    name = models.CharField(max_length=180)
    grade = models.CharField(max_length=20)
    topic = models.CharField(max_length=180)
    materials = models.CharField(max_length=300)
    vocab = models.TextField()
    description = models.TextField()
    activities = models.TextField()
    accommodations = models.TextField()

    def __str__(self):
        return self.name

class Standard(models.Model):
    heading = models.CharField(max_length=100)
    anchor_number = models.IntegerField()
    anchor_text = models.TextField()
    title = models.CharField(max_length=20)
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='standards')

    def __str__(self):
        return self.heading
