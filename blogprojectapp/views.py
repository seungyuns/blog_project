from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs=Blog.objects #쿼리셋

    blog_list = Blog.objects.all() #모든 블로그글 불러오기.
    paginator = Paginator(blog_list, 3) #객체 세 개를 한 페이지로 자르기.
    page = request.GET.get('page') #요청된 사전형 객체의 key값이 page인 값을 할당.(페이지 번호 할당) 
    posts = paginator.get_page(page) # 위에서 할당한 page 번호의 페이지를 불러와 posts변수에 담는다.
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts}) # 페이지 인자 return 해주기.

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'sss': details})

def new(request):
    return render(request, 'new.html')

def create(request): # 입력받은 내용 데이터베이스에 넣어주기
    blog = Blog()  
    blog.title = request.GET['title'] #폼에 입력했던 name이 title 정보를 끌어온다.
    blog.body = request.GET['body']  #폼에 입력했던 name이 body 정보를 끌어온다.
    blog.pub_date = timezone.datetime.now() # 작성 시간 출력해주는 함수, 상단에 임포트 해와야 함.
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    # 기능 1, 입력된 내용 처리하는 기능 -> POST
    # 기능 2, 빈 페이지를 띄워주는 기능 -> GET
    if request.method=='POST':
        form = BlogPost(request.POST)
        if form.is_valid(): #입력된 값이 옳바르게 모두 입력되었는지 검증해주는 함수.
            post = form.save(commit=False) # save는 하되 아직 모델에 저장은 하지 않는다.
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})