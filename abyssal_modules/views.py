from django.shortcuts import render
from django.views import View
from django.db.models import Min, Max

from abyssal_modules.models import Module, ModuleType, ModuleAttribute


class ModuleList(View):
    def get(self, request):
        return render(
            request,
            'abyssal_modules/list.html',
            {
                'modules': Module.objects.all()
            }
        )


class TypedModuleList(View):
    def get(self, request, type_id):
        module_type = ModuleType.objects.get(id=type_id)

        attribute_ranges = {x['attribute__id']: x for x in ModuleAttribute
            .objects
            .filter(
                module__type__id=type_id,
                attribute__interesting=True
            )
            .values('attribute__id')
            .annotate(min_val=Min('value'), max_val=Max('value'))
        }

        attributes = module_type.attributes.filter(interesting=True).order_by('id').all()

        for a in attributes:
            mult = 0.001 if a.id == 73 else 1.0
            a.max_val = attribute_ranges[a.id]['max_val'] * 1.05 * mult
            a.min_val = attribute_ranges[a.id]['min_val'] * 0.95 * mult

        return render(
            request,
            'abyssal_modules/type_module_list.html',
            {
                'modules': module_type.modules.all(),
                'module_type': module_type,
                'attributes': attributes
            }
        )
