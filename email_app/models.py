from django.db import models

# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    is_active = models.BooleanField(default=True)
    # add_campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE, related_name="subcriber_adds", default=1)

    def __str__(self) -> str:
        return f'{self.email_id} {self.name}'
    

class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=100)
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField(auto_now=True)
