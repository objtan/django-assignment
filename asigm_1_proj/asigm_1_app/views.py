from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .forms import AddUserForm
from .models import Person
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    latest_person_list = Person.objects.all().values()
    context = {'latest_person_list': latest_person_list}
    return render(request, 'asigm_1_app/index.html', context)

def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'asigm_1_app/detail.html', {'person': person})

def adduser(request):
    form = AddUserForm
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your user has been added!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        # else: # form not valid so display message and retain the data entered
        #         form = AddUserForm(request.POST)
        #         messages.success(request, 'Error in creating your user, the form is not valid!')
        #         return render(request, 'asigm_1_app/adduser.html', {'form':form})
    # else: #the form has no data
    #     form = AddUserForm() #produce a blank form
    #     return render(request, 'asigm_1_app/adduser.html', {'form':form})
    context = {'form':form}
    return render(request, 'asigm_1_app/adduser.html', context)


def delete(request, person_id):
  person = Person.objects.get(pk=person_id)
  person.delete()
  return HttpResponseRedirect(request.META['HTTP_REFERER'])

