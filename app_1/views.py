from django.shortcuts import render, redirect,get_object_or_404
from .models import Book ,Category
from .forms import book_form,cata_form

# Create your views here.
def index (request):
    if request.method == 'POST':
        if 'title' in request.POST:
            form=book_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                
        if 'name' in request.POST:
            form2=cata_form(request.POST)
            if form2.is_valid():
                form2.save()
        return redirect('/')
    send={
     'books':Book.objects.all(),
     'catas':Category.objects.all(),
     'form':book_form(),
     'form2':cata_form(),
     'book_count':Book.objects.filter(active=True).count(),
     'sold':Book.objects.filter(status='sold').count(),
     'availble':Book.objects.filter(status='availble').count(),
     'rented':Book.objects.filter(status='rented').count()
    }
    return render(request,'app_1/page/page1.html',send)

def books(request):
    books= Book.objects.all()
    cata= Category.objects.all()
    return render(request,'app_1/page/books.html',{'books':books,'catas':cata})

def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method=='POST':
        book_save=book_form(request.POST,request.FILES,instance=book_id)  
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=book_form(instance=book_id)
            
    return render(request,'app_1/page/update.html',{'book':book_save})
def delet(request,id):
    book=get_object_or_404(Book,id=id)
    if request.method=='POST':
        book.delete()
        return redirect('/')
    return render(request,'app_1/page/delete.html',{'type':'التصنيف'})
def delet_cata(request,id):
    cata=get_object_or_404(Category,id=id)
    if request.method=='POST':
        cata.delete()
        return redirect('/')
    return render(request,'app_1/page/delete.html',{'type':'التصنيف'})