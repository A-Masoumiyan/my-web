from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import homedb, Category
# Register your models here

admin.site.site_header = " صفحه مدیریت "


def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='P')
    modeladmin.message_user(request, ngettext(
        'شما %d مقاله را منتشر کردید.',
        'شما %d عدد از مقالات را منتشر کردید.',
        updated,
    ) % updated, messages.SUCCESS)


make_published.short_description = " منتشر کردن مقالات "


def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='D')
    modeladmin.message_user(request, ngettext(
        'شما %d مقاله را پیش نویس کردید.',
        'شما %d عدد از مقالات را پیش نویس کردید.',
        updated,
    ) % updated, messages.SUCCESS)


make_draft.short_description = " پیش نویس کردن مقالات "


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position", "tittle", "slug", "parent", "status")
    list_filter = ('status',)
    search_fields = ('tittle', 'slug')
    prepopulated_fields = {'slug': ('tittle',)}


admin.site.register(Category, CategoryAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = ("tittle", "photo_tag", "jcreated", "jupdated", "status", 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('tittle', 'document')
    prepopulated_fields = {'slug': ('tittle',)}
    ordering = ['status', '-publish']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return " , ".join([category.tittle for category in obj.category_published()])
    category_to_str.short_description = "دسته بندی"


admin.site.register(homedb, HomeAdmin)
