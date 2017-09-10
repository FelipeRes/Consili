from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from .forms import CategoryForm

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Risk)
admin.site.register(Purchase)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    icon = '<i class="material-icons">widgets</i>'
    list_display = ('id', 'get_name', 'color', 'get_colored_rect',)

    def get_name(self, obj):
        return mark_safe('<span style="color: %s"> %s </span>' % (obj.color, obj.name))

    def get_colored_rect(self, obj):
        rect = mark_safe('<div style="width:40px; height:30px;background: %s;"></div>' % obj.color)
        return rect


