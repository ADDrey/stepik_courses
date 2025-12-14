from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import PersonForm


# Получение данных из БД
def index(request):
    form = PersonForm()
    people = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'people': people})


# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')


# Изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)
        return render(request, 'edit.html', {'form': form})


# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

    person.delete()
    return HttpResponseRedirect('/')


from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main_app.models import User


def sort_users(request, field='id', dir='up'):
    sort_fields = {
        'up_id': 'id',
        'up_name': 'name',
        'up_age': 'age',
        'dn_id': '-id',
        'dn_name': '-name',
        'dn_age': '-age',
    }
    sort_fields_name = {'id': 'id', 'name': 'имени', 'age': 'возрасту'}
    sort_dirs_name = {'up': 'возрастание', 'dn': 'убывание'}

    validete_field = sort_fields.get(str(dir, '_', field), None)
    if validete_field is not None:
        user_data = User.objects.all().order_by(validete_field)
        sort_field = sort_fields_name.get(field)
        sort_dir = sort_dirs_name.get(dir)
    else:
        user_data = User.objects.all().order_by(sort_fields.get('up_id'))
        sort_field = sort_fields_name.get('id')
        sort_dir = sort_dirs_name.get('up')
    form_context = {
        'user_data': user_data,
        'sort_field': sort_field,
        'sort_dir': sort_dir,
    }
    return render(request, 'sort_users.html', context=form_context)