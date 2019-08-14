from django.shortcuts import render
import random


def index(request):  # 첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보 
    # 요청이 들어오면 'index.html' 을 보여준다. 
    return render(request, 'index.html')  # render 의 첫번째 인자도 반드시 request


def introduce(request): 
    return render(request, 'introduce.html')


# Template Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }

    # Django template 으로 context 전달 
    return render(request, 'dinner.html', context)


def image(request):
    context = {
        'picsum': 'https://picsum.photos/500',
    }
    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)


def name(request, word):
    context = {
        'word': word,
    }
    return render(request, 'word.html', context)


def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'times.html', context)
