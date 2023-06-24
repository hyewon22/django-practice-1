from django.shortcuts import render, get_object_or_404, redirect #  get_object_or_404는 존재하지 않는 페이지 접속 시 오류 대신 404 출력 위해 임포트
from django.http import HttpResponse  # HttpResponse는 페이지 요청에 대한 응답을 위해 사용하는 장고 클래스
from .models import Question  # Question 모델 데이터를 다뤄야 하므로
from django.utils import timezone

# Create your views here.

def index(request) :  # request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date')  # Question 모델 데이터를 작성한 날짜의 역순으로 조회하기 위해 order_by() 함수 사용. order_by() 함수는 조회한 데이터를 특정 속성으로 정렬하고, '-create_date'는 -기호가 앞에 붙어 있으므로 작성일시의 역순을 의미함.
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)  # render함수는 context에 있는 Question 모델 데이터 question_list를 pybo/question_list.html 파일에 적용해서 HTML코드로 변환함. request는 response하기 위해 받는 필수 인자. 장고에서는 pybo/question_list.html 이런 파일을 템플릿이라고 부름. 템플릿은 장고의 태그를 추가로 사용할 수 있는 HTML파일이라 생각하면 됨.
    # return HttpResponse("Welcome to the pybo !")

def detail(request, question_id) :
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id) 이 코드 말고 존재하지 않는 페이지 접속하면 오류 대신 404 페이지 출력하게 하기 위해서 아래 코드로.
    question = get_object_or_404(Question, pk=question_id) # pk(기본키)에 해당하는 건 없으면 오류 대신 404 출력.
    context = {'question' : question} # context는 딕셔너리 형태로.
    return render(request, 'pybo/question_detail.html', context) # context는 pybo/question_detail.html에 전달됨.

def answer_create(request, question_id) :
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)