from django.contrib import admin
from .models import (
    Item,
    ItemFeedback,
    ItemType,
    FeatureType,
    ItemFeature,
)


admin.site.register(Item)
admin.site.register(ItemFeedback)
admin.site.register(ItemType)
admin.site.register(FeatureType)
admin.site.register(ItemFeature)
