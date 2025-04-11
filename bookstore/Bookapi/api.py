from rest_framework import serializers
from rest_framework.response import Response
from .models import BookModel
from rest_framework.decorators import api_view
from rest_framework import viewsets


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

    def validate(self,data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError("Price value connot be negative")
        return data
    

# @api_view(["GET"])
# def BookListApi(request):
#     books = BookModel.objects.all()

#     serializer = BookModelSerializers(books,many=True)

#     return Response(serializer.data)


# @api_view(["POST"])    
# def BookCreateApi(request):
#     data = request.data

#     serializer = BookModelSerializers(data = data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             "massage":"Book Created"
#         })
#     return Response(serializer.errors)
# @api_view(["PUT"])
# def BookUpdateApi(request,id):
#     data = request.data

#     book = BookModel.objects.get(id=id)

#     serializer = BookModelSerializers(instance=book,data=data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             "massage":"Book Updated"
#         })
#     return Response({
#         "massage":"Book not updated"
#     })

# @api_view(["DELETE"])
# def BookDeleteApi(request,id):
#     data = request.data

#     book = BookModel.objects.get(id=id)
#     book.delete()

#     return Response({
#         "massage":"Book deleted"
#     })

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializers


    def list(self,request):
        if not request.user.is_authenticated:
            return Response({
                "massage":"Please Login"
            })
        user = request.user
        books = BookModel.objects.filter(author=user)
        serializer = self.get_serializer(books,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        
        if not request.user.is_authenticated:
            return Response({
                "massage":"Please Login"
            })
        user = request.user
        data = request.data

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save(author = user)

            return Response({
                "massage":"Book created"
            })
        
    def update(self,request,pk):
        if not request.user.is_authenticated:
            return Response({
                "massage":"Please Login"
            })
        book = BookModel.objects.get(id=pk)

        if book.author == request.user:
           data = request.data 
           serializer = self.get_serializer(instance=book,data=data)
           if serializer.is_valid():
               serializer.save()
               return Response({
                   "massage":"Book Updated"
               })
        return Response({
             "massage":"You are the not owner of this book"
         })  
    
    def destroy(self,request,pk):
        if not request.user.is_authenticated:
            return Response({
                "massage":"Please Login"
            })
        book = BookModel.objects.get(id=pk)

        if request.user == book.author:
            book.delete()

            return Response({
                "massage":"Book Deleted"
            })
        return Response({
            "massage":"You are the not owner of this book"
        })