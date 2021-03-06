from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic
from django.http import JsonResponse
from . import helpers


Item = apps.get_model('item', 'Item')
ItemFeature = apps.get_model('item', 'ItemFeature')


class ItemsView(generic.View):
    """
    Формат запроса:
    -отсутствует (потому что GET-запрос)-

    Формат ответа:
    {
        "itemsCount": 424,
        "items" : [
            {
                "id": 123,
                "name": "...",
                "price": "...",
                "features": [
                    {
                        "featureType": "..1",
                        "value": "...",
                    },
                    {
                        "featureType": "..2",
                        "value": "...",
                    },
                    ...
                ],
            },
            ...
        ]
    }
    """

    def get(self, request, *args, **kwargs):

        response = {}

        if request.content_type != 'application/json':
            response = {'error': 'Wrong request.'}

        else:
            data = helpers.from_json(request.body)
            # TODO задействовать data

            items = Item.objects.filter()

            response = {
                'itemsCount': Item.objects.count(),
                'items': []
            }

            for item in items:
                item_dict = {
                    'id': item.pk,
                    'name': item.name,
                    'price': item.price,
                    'features': [],
                }

                for feature in item.features.all():
                    item_dict['features'].append(
                        {
                            'featureType': feature.feature_type.name,
                            'value': feature.value,
                        }
                    )

                response['items'].append(item_dict)

        return JsonResponse(response)
