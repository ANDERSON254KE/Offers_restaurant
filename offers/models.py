from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import Restaurant

class Offer(models.Model):
    """
    Model representing restaurant offers/deals.
    """
    restaurant = models.ForeignKey(
        Restaurant, 
        on_delete=models.CASCADE,
        related_name='offers'
    )
    
    title = models.CharField(
        max_length=200,
        help_text="Title of the offer"
    )
    
    description = models.TextField(
        help_text="Detailed description of the offer"
    )
    
    discount_percentage = models.IntegerField(
        null=True, 
        blank=True,
        help_text="Percentage discount for this offer",
        validators=[
            models.MinValueValidator(0),
            models.MaxValueValidator(100)
        ]
    )
    
    start_date = models.DateTimeField(
        help_text="When the offer becomes active"
    )
    
    end_date = models.DateTimeField(
        help_text="When the offer expires"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this offer is currently active"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.restaurant.name} - {self.title}"
    
    def clean(self):
        """Validate the offer dates."""
        if self.end_date <= self.start_date:
            raise ValidationError({
                'end_date': 'End date must be after start date.'
            })
        
        if self.start_date < timezone.now():
            raise ValidationError({
                'start_date': 'Start date cannot be in the past.'
            })
    
    @property
    def is_expired(self):
        """Check if the offer has expired."""
        return timezone.now() > self.end_date
    
    @property
    def is_upcoming(self):
        """Check if the offer hasn't started yet."""
        return timezone.now() < self.start_date
    
    def save(self, *args, **kwargs):
        """Override save to perform full_clean."""
        self.full_clean()
        super().save(*args, **kwargs)