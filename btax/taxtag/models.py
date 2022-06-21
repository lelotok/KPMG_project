from django.db import models

# Create your models here.

class Article(models.Model):
    date = models.DateField()
    numac = models.CharField(max_length=15)
    link=models.CharField(max_length=150)
    nl_text=models.TextField()
    nl_sum=models.TextField()
    nl_tags=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.numac}  -  {self.date}'
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['-date' , 'numac']


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    level=models.SmallIntegerField(null=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.tag
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['tag']