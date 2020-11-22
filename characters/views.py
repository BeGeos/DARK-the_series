from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def characters(request):
    if request.method == 'POST':
        form = SearchCharacter(request.POST)
        if form.is_valid():
            name = form.cleaned_data['fullname']
            query = Characters.objects.filter(fullname__contains=name)
            # print(len(query))
            if len(query) == 1:
                return redirect('/characters/details/' + query.get().fullname)
    else:
        form = SearchCharacter()
    obj = Characters.objects.all()
    context = {
        'obj': obj,
        'form': form
    }
    return render(request, 'characters.html', context)


def characters_details(request, name):
    database = Characters.objects.all()
    obj = Characters.objects.get(fullname=name)
    try:
        image = CharPictures.objects.get(character=obj.id)
    except:
        image = 'Not Found'
    # print(image.image)
    if obj.id - 1 > 0:
        previous = Characters.objects.get(id=(obj.id - 1))
    else:
        previous = None
    if (obj.id + 1) < len(database):
        nexts = Characters.objects.get(id=(obj.id + 1))
    else:
        nexts = None
    context = {
        'obj': obj,
        'image': image,
        'previous': previous,
        'next': nexts,
        'all': database
    }
    return render(request, 'char-details.html', context)


def summary_view(request):
    return render(request, 'summary.html')


def does_exist(queryset1, queryset2):
    if queryset1.id != queryset2.id:
        if queryset1.status and queryset2.status:
            if queryset1.gender != queryset2.gender:
                return True
    return False


def game_view(request):
    form = PlayGameForm()
    # print(request.GET['first'])
    return render(request, 'game.html', {'form': form})


def game_play_view(request):
    form = PlayGameForm()
    if request.method == 'GET':
        first = request.GET['first']
        second = request.GET['second']
        try:
            first_query = Characters.objects.get(fullname__contains=first)
            second_query = Characters.objects.get(fullname__contains=second)
            first_pic = CharPictures.objects.get(character=first_query.id)
            second_pic = CharPictures.objects.get(character=second_query.id)

            if first_query.id == second_query.id:
                result = 'AH AH nice try!'
            elif first_query.gender == second_query.gender:
                result = "I don't have anything against it, but 2 people of the same gender cannot naturally reproduce"
            elif does_exist(first_query, second_query):
                result = f'Yep, {first_query.fullname} and {second_query.fullname} would generate a real offspring'
            else:
                result = f'Nope, {first_query.fullname} and {second_query.fullname} would not generate a real offspring'
        except:
            return render(request, 'game.html', {'form': form})
    context = {
        'first_img': first_pic,
        'second_img': second_pic,
        'result': result,
        'form': form
    }

    return render(request, 'game-play.html', context)

