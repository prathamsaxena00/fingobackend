from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers  import JSONParser
from django.http.response import JsonResponse
from books.models import Booksbase
from books.serializers import BookSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def bookApi(request,id=0):
    if request.method=='GET':
        books=Booksbase.objects.all()
        book_serializer=BookSerializer(books,many=True)
        return JsonResponse(book_serializer.data,safe=False)
    elif request.method=='POST':
        books_data=JSONParser().parse(request)
        book_serializer=BookSerializer(data=books_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added succesfully",safe=False)
        return JsonResponse("failed to add",safe=False)
    elif request.method =='PUT':
        book_data=JSONParser().parse(request)
        book =Booksbase.objects.get(BookId=book_data['BookId'])
        book_serializer=BookSerializer(book,data=book_data)   
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':         
        book=Booksbase.objects.get(BookId=id) 
        book.delete()
        return JsonResponse("Delete Successfully", safe=False)    

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)