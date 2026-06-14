from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=10, default='📚')

    def __str__(self):
        return self.name

class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership', related_name='study_groups')
    university = models.CharField(max_length=200, blank=True)
    max_members = models.IntegerField(default=10)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")

    def __str__(self):
        return self.name

    @property
    def member_count(self):
        return self.members.count()

    @property
    def is_full(self):
        return self.member_count >= self.max_members

class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=[
        ('member', 'Member'),
        ('admin', 'Admin'),
    ], default='member')

    class Meta:
        unique_together = ('user', 'group')

class Resource(models.Model):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='resources')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='resources/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
