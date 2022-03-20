from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from django.views import View
from web.models import Category
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from django.utils import timezone
from django.http import HttpResponse



@request_mapping("/custcen")
class custcenView(View):

    def index(request):
        question_list = Question.objects.order_by('-create_date')
        context = {'question_list': question_list}
        return HttpResponse("안녕하세요 쇼핑몰에 오신것을 환영합니다.")

    def index(request):
        question_list = Question.objects.order_by('-create_date')
        context = {'question_list': question_list}
        return render(request, 'custcen/question_list.html', context)

    def question_create(request):
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.create_date = timezone.now()
                question.save()
                return redirect('web:index')
        else:
            form = QuestionForm()
        context = {'form': form}
        return render(request, 'custcen/question_form.html', context)

    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        context = {'question':question}
        return render(request, 'custcen/question_detail.html', context)

    def answer_create(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.create_date = timezone.now()
                answer.question = question
                answer.save()
                return redirect('custcen:detail', question_id=question.id)
        else:
            form = AnswerForm()
        context = {'question':question, 'form': form}
        return render(request, 'custcen/question_detail.html', context)

    @request_mapping("/custcen/notice", method="post")
    def notice(request, Post=None):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 15)
        categories = Category.objects.all()
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
            context = {'posts': posts, 'categories': categories}

        return render(request, 'custcen/notice.html', context)


    @request_mapping("/custcen/notice_d", method="get")
    def notice_detail(request, pk, Post=None):
        post = Post.objects.get(pk=pk)
        categories = Category.objects.all()
        context = {"post": post, "categories": categories}

        return render(request, 'custcen/notice_d.html', context)



