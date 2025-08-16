from django.shortcuts import redirect , render , get_object_or_404
from django.urls import reverse

from news.models import New , Category
from news.forms import AddNewsForm

# Create your views here.

def news_list_view(request):
    news = New.objects.all().order_by('-id')
    categories = Category.objects.all()

    context = {
        'latest_news':news ,
        'categories':categories ,
    }
    return render(request , 'index.html' , context)

def news_detail_view(request , pk):
    news = get_object_or_404( New , id=pk )
    categories = Category.objects.all()
    context = {
        'news':news ,
        'categories':categories,
    }
    if request.method == "POST":
        news.category = Category.objects.get(id = request.POST.get('category'))
        news.title = request.POST.get('title')
        news.content = request.POST.get('content')
        if request.FILES.get('image'):
            news.image = request.FILES.get('image')
        news.save()

    return render(request , 'news_detail.html' ,context)

def add_news_view(request):
    if request.method == 'GET':
        news_form = AddNewsForm()
        categories = Category.objects.all()
        date = {
            'categories': categories,
            'news_form': news_form,
        }
        return render(request , 'add_news.html' , date)
    elif request.method == "POST" :
        form = AddNewsForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(f"{error}" for error in form.errors )

        return redirect(reverse('home'))
        # category = Category.objects.get(id = request.POST.get('category'))
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # image = request.FILES.get('image')
        # news = New.objects.create(title=title,
        #                           category=category,
        #                           content=content,
        #                           image=image,
        #                           )
        # return redirect(reverse('news_detail', kwargs={'pk': news.id}))

        
def delete_news_view(request,pk):
    news = New.objects.get(id=pk )
    news.delete()
    return render(request , 'news_deleted.html')