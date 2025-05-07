from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from .models import Student

@receiver(post_save, sender=Student)
def promote_student(sender, instance, created, **kwargs):
    """
    This signal checks the date and promotes students on the 30th of September each year.
    """
    today = date.today()

    # Check if it's the 30th of September
    if today.month == 9 and today.day == 30:
        if not instance.grade == 'graduated':  # Don't promote already graduated students
            instance.promote()
