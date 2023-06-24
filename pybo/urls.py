from django.urls import path
from . import views

app_name = 'pybo'
# 네임스페이스 추가 위해 app_name 변수에 네임스페이스 이름으로 'pybo' 저장

urlpatterns = [
    path('', views.index, name='index'),  # /pybo/에 index라는 URL 별칭 붙임.
    # config/urls.py 파일에서 pybo/에 대한 처리를 한 상태에서 pybo/urls.py가 실행되므로 첫 번째 매개변수에 pybo/가 아닌 빈 문자열을 인자로 넘겨줌. (어차피 여긴 pybo/를 처리하는 것이므로)
    path('<int:question_id>/', views.detail, name='detail'),  # /pybo/question_id에 detail라는 URL 별칭 붙임.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create')
]
