Model View Controller

controller : 작업하는 부분 (MTV 의 View)



Model Template View

view : 중간관리자 기능 



---


### Django Setting

#### 가상환경

django project 하나당 python env 하나씩 

project 마다 library 랑 version 이 다를수 있기 때문에 

```bash
# 파이썬 버전 확인
# 반드시 3.7.x 버전이 맞는지 확인 후 진행 
$ python -V
Python 3.7.4


# 가상환경 생성
# python -m venv <가상환경 설치경로>
$ python -m venv venv


# 가상환경 적용
$ source venv/Scripts/activate


# 버전확인
(venv)  # <= 가상환경 적용 시 git bash 에서 해당 환경 이름이 표시된다. 
$ python -V
Python 3.7.4


# 설치된 모듈 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.


# pip upgrade
(venv)
$ python -m pip install --upgrade pip


# pip upgrade 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0

```



---


### VS Code 및 기타 세팅

#### VS Code 파이썬 환경 선택

- VS Code Extensions 에서 `pyhon` 과 `django` 설치

- `Ctrl + Shift + P` => `pythons select interpreter` => 방금 생성한 가상환경을 선택(`.\venv\Scripts\python.exe`)

- .vscode/settings.json 파일이 생성되며 터미널에서 자동으로 가상환경 적용된다면 OK

  (.vscode 폴더에서 settings.json 확인 / Ctrl +` terminal 확인) 

- 가상환경에 대한 정보만 기록 / 가상환경은 올리지 않음 



#### Git ignore 세팅

- gitignore.io 에 접속해서 `python, django, windows, vscode` 선택 후 생성
- .gitignore 파일 생성 후 붙여넣기
- .vscode 하위 파일도 리스트에서 지우기 



#### VS Code Django 환경 세팅

```json
{   
    // 파이썬 환경 선택 => 자동으로 해줌 
    "python.pythonPath": "venv\\Scripts\\python.exe",

    // Django 에서 사용되는 파일 타입에 대한 정의 
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    // django-html 에서도 html emmet 을 적용 
    // 자동 완성 만들때 필요 
    "emmet.includeLanguages": {"django-html": "html"},

    // django-html 에서 tab size 를 2칸으로 고정 
    "[django-html]": {
        "editor.tabSize": 2
    },
}
```



---

### Start Django project

```bash
(venv)
$ pip install django
```

- Django 를 설치한 순간부터 `django-admin` 이라는 command를 사용할 수 있게 된다.
- 이 command 를 통해 django project 에 여러가지 명령을 할 수 있다.



#### Start project

```bash
# 프로젝트 시작
(venv)
$ django-admin startproject django_intro .
```

- 현재 디렉토리에서 django_intro 라는 이름으로 프로젝트를 시작하겠다.

- Django project naming

  ​	'-' 캐릭터는 사용될 수 없다.

  ​	python 과 django 에서 이미 사용되는 이름은 사용하지 않는다.

  ​	(django 라는 이름은 django 그 자체와 충돌이 발생하며, test 라는 이름도 django 내부적으로 사용하는 모듈 이름)



#### Run server

```bash
# 서버 시작 
(venv)
$ python manage.py runserver
```

- `Ctrl + c`  커맨드로 종료한다. 
- 기본적으로 `localhost:8000`  에서 실행이 된다 . 



---

`__init__.py`  패키지로 인식시킨다. 안에 뭘 넣을 일은 없다. 

`settings.py`  모든 설정이 들어간다. 

`urls.py`  path 지정, 목차를 작성하는 곳 

`wsgi.py`  web server gateway interface / 배포할 때 사용 

`manage.py`  command 용, 수정할 일은 없다.

`db.sqlite3`  서버 없이 사용 가능한 가벼운 db , 만질 필요는 없다.



#### setting.py 

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



#### app

```bash
# app 만들기
$ python manage.py startapp pages
```

- app 의 단위?

`migrations`  

`admin.py`  관리자 페이지를 커스터마이징 하는 곳 

`apps.py`  app 에 대한 정보가 입력되는 곳, 건드릴 일은 없음 

`models.py`  app 에서 사용할 model 을 정의하는 곳, 저장할 데이터들을 정의 

`tests.py`  test 할 코드들을 적는 곳 

`views.py`  **엄청 중요** (model : db / templates : 사람들에게 보여지는 곳 / view : 작업을 하는 곳 , 함수로 정의)

view 함수 - url 

3대장 ; models.py (저장할 데이터 정의) / views.py (함수가 정의) / urls.py (사용자가 들어올 수 있는 경로 설정)

project : app 집단 



#### 출생신고

```python
# settings.py
# 이렇게 해야 app 사용 가능
INSTALLED_APPS = [
    # Local apps
    'pages',
    
    # Third party apps

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# pages 사용 준비 끝!
```



path도 위에서부터 아래로 인식됨. 그래서 순서가 중요 