from django.db import models
from django.contrib.auth.models import User
from pets.models import Pet


class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    phone = models.CharField(max_length=20)
    address = models.TextField()
    reason = models.TextField()
    previous_pet_experience = models.BooleanField(default=False)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.pk:
            old = AdoptionRequest.objects.filter(pk=self.pk).first()
            if old and old.status != 'Approved' and self.status == 'Approved':
                self.pet.status = 'Adopted'
                self.pet.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} → {self.pet.name} ({self.status})'
