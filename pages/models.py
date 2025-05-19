from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.SmallIntegerField(default = 0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "page"
        verbose_name_plural = "pages"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

