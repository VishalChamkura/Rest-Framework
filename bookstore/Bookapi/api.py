from rest_framework import serializers
from rest_framework.response import Response
from .models import BookModel
from rest_framework.decorators import api_view


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

    def validate(self,data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError("Price value connot be negative")
        return data
    

@api_view(["GET"])
def BookListApi(request):
    books = BookModel.objects.all()

    serializer = BookModelSerializers(books,many=True)

    return Response(serializer.data)


@api_view(["POST"])    
def BookCreateApi(request):
    data = request.data

    serializer = BookModelSerializers(data = data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "massage":"Book Created"
        })
    return Response(serializer.errors)
@api_view(["PUT"])
def BookUpdateApi(request,id):
    data = request.data

    book = BookModel.objects.get(id=id)

    serializer = BookModelSerializers(instance=book,data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "massage":"Book Updated"
        })
    return Response({
        "massage":"Book not updated"
    })

@api_view(["DELETE"])
def BookDeleteApi(request,id):
    data = request.data

    book = BookModel.objects.get(id=id)
    book.delete()

    return Response({
        "massage":"Book deleted"
    })
