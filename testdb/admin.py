from django.contrib import admin
from .models import Teacher, Subject, Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book

class BookInLineAdmin(admin.TabularInline):
    model = Book
    extra = 1

class SubjectAdmin(admin.ModelAdmin):
    model = Subject

class TeacherAdmin(admin.ModelAdmin):
    #model = Teacher
    inlines = (BookInLineAdmin, )


admin.site.register(Book, BookAdmin)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
