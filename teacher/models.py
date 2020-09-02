from django.db import models



class Grade(models.Model):
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.grade


class Message(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    website = models.URLField(max_length=500, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class AddClass(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100, default="school")

    def __str__(self):
        return self.username

class AddClassAsClassTeacher(models.Model):
    grade = models.OneToOneField(Grade, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100, default="school")

    def __str__(self):
        return self.username


        