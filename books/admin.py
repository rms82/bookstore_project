from django.contrib import admin

from .models import Book, Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'text', 'datetime_created']
    ordering = ('-datetime_created', )


admin.site.register(Book)

