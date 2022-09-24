from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Person


def index(request):
    latest_person_list = Person.objects.order_by('id')[:5]
    context = {'latest_person_list': latest_person_list}
    return render(request, 'asigm_1_app/index.html', context)

def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'asigm_1_app/detail.html', {'person': person})