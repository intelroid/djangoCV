from django.contrib import admin
from Post.models import Post



admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'mod_date')
    list_filter = ('mod_date',)
    searcj_dielfs = ('title', 'text')
