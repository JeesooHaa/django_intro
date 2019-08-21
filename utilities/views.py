from django.shortcuts import render

# templates 를 한 곳에 모아버린다...
# templates name space 를 만들어줘야한다.
# static 도 마찬가지 
def index(request):  
    return render(request, 'utilities/index.html')
