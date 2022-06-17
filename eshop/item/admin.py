from django.contrib import admin
from .models import (
    Item,
    ItemFeedback,
    ItemType,
    FeatureType,
    ItemFeature,
)


class ItemFeatureInline(admin.TabularInline):
    model = ItemFeature
    fields = ('feature_type', 'value')
    extra = 0


class ItemFeedbackInline(admin.StackedInline):
    model = ItemFeedback
    fields = ('ranking', 'message')
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Основные параметры',
            {
                'fields': ('name', 'price', ),
            },
        ),
    )
    inlines = (ItemFeatureInline, ItemFeedbackInline, )


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemFeedback)
admin.site.register(ItemType)
admin.site.register(FeatureType)
admin.site.register(ItemFeature)
