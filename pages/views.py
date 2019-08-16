from django.shortcuts import render
from datetime import datetime
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


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request, month, day):
    # today = datetime.now()
    # if today.month == 10 and today.day == 15:
    #     result = '예'
    # else:
    #     result = '아니오'

    if len(month) == 1:
        month = '0' + month
    context = {
        'month': month,
        'day': day,
        # 'result': result
    }
    return render(request, 'isitbirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    # lottos = sorted(list(random.sample(range(1, 46), 6)))
    lottos = []
    ran_num = random.randint(1, 45)

    for i in range(6):
        while ran_num in lottos:
            ran_num = random.randint(1, 45)
        lottos.append(ran_num)
    lottos.sort()

    context = {
        'real_lotto': real_lotto,
        'lottos': lottos,
    }
    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')


# 중요 !!
def result(request):
    category = request.GET.get('category')
    query = request.GET.get('query')
    context = {
        'category': category,
        'query': query,
    }
    return render(request, 'result.html', context)


def lotto_pick(request):
    return render(request, 'lotto_pick.html')


def lotto_result(request):
    pick_numbers = request.GET.get('numbers')
    pick_lists = sorted(list(map(int, pick_numbers.split())))
    # [int for number in numbers.split()]
    lotto_numbers = [21, 25, 30, 32, 40, 42]
    # 등수 조건문 작성 
    context = {
        'pick_numbers': pick_numbers,
        'pick_lists': pick_lists,
        'lotto_numbers': lotto_numbers,
    }
    if len(set(pick_lists)) != 6:
        return render(request, 'lotto_error.html')
    else:
        return render(request, 'lotto_result.html', context)


def lotto_error(request):
    return render(request, 'lotto_error.html')


def static_example(request):
    return render(request, 'static_example.html')


def num_push(request):
    return render(request, 'num_push.html')


def num_pull(request):
    push_number = request.GET.get('number')
    context = {
        'push_number': push_number
    }
    return render(request, 'num_pull.html', context)
