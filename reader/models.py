from django.db import models


class PDF(models.Model):
    course_title = models.CharField(max_length=50)
    description = models.TextField()
    pdf = models.FileField(upload_to="static")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.course_title)
