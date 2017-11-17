from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Subject(models.Model):
    tutor = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    subject_area = models.CharField(max_length=250)
    def get_absolute_url(self):
        return reverse('tutorial:detail',kwargs={'pk': self.pk})
    def __str__(self):
        return 'Tutor- ' + self.tutor + '; Subject- ' + self.subject_name + '; Discipline- ' + self.subject_area
class Note(models.Model):
    note_subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    note_title = models.CharField(max_length=250)
    #note_file = models.FileField()
    #video_link = models.CharField(max_length=10000)
    def __str__(self):
        return self.note_title
