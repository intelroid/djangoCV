from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length = 100, blank =True)
    name = models.CharField(max_length = 100, blank = True)
    created_date = models.DateField(null=True, blank = True)
    mail = models.CharField(max_length=50, blank = True)
    memo = models.TextField()
    hits = models.IntegerField(null = True, blank = True)
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)


#
#class Post(models.Model):
#    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
#    title = models.CharField(max_length = 200)
#    text = models.TextField()
#    pub_date = models.DateTimeField(default = timezone.now)
#    mod_date = models.DateTimeField('MODIFY DATE',auto_now=True)
#    hits = models.IntegerField(null=True, blank = True)

#    class Meta:
#        verbose_name='post'
#        verbose_name_plural='posts'
#        db_table='blog_posts'
#        ordering=('-mod_date',)

#    def __str__(self):
#        return self.title



#    def get_absolute_url(self):
#        return reverse('Post:post_detail',args=(self.id,))

#    def get_previous(self):
#        return self.get_previous_by_mod_date()


#    def get_next(self):
#        return self.get_next_by_mod_date()


    
