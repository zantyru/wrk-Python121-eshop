from django.shortcuts import render
from django.views import generic
from .models import (
    Item,
    ItemType,
)


class CategoriesView(generic.ListView):
    model = ItemType
    template_name = 'item/categories.html'
    context_object_name = 'item_types'

    # def get_queryset(self):
    #     return ItemType.objects.filter().orderby('name')


class ItemAllView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name='item/all.html'
        )


class ItemsInCategoryView(generic.View):

    def get(self, request, category_id, *args, **kwargs):
        items = []
        category_name = ""

        item_type = ItemType.objects.filter(pk=category_id).first()
        if item_type:
            category_name = item_type.name
            items = Item.objects.filter(item_type=item_type)

        return render(
            request,
            template_name='item/category.html',
            context={
                'category_name': category_name,
                'items': items,
            }
        )


class ItemView(generic.DetailView):
    model = Item
    template_name = 'item/detail.html'
