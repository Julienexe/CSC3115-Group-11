from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Program(models.Model):
    """
    Program model with common fields.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Optional: Add user relationship
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='program_created')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program:program-detail', kwargs={'pk': self.pk})
