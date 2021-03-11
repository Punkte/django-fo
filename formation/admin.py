from django.contrib import admin
from .models import Post, Contact, CV, Skill
from .forms import CvForm

class TermInlineAdmin(admin.TabularInline):
    model = CV.skills.through

class CVAdmin(admin.ModelAdmin):
  fieldsets = (
      (None, {
          'fields': ('name', 'description', 'experiences')
      }),
  )
  inlines = (TermInlineAdmin,)
# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(CV, CVAdmin)
admin.site.register(Skill)
