from watchlist_app.models import WatchList,StreamingPlatform,Review
from watchlist_app.api.serializers import WatchSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies=Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data,status=200)
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method=='GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
        
    
#     if request.method=='PUT': # In put we rewrite every field but in patch we edit only one or selected feilds
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=202)
#         return Response(serializer.errors,status=400)
#     if request.method=='DELETE':
        # movie=Movie.objects.get(pk=pk)
        # movie.delete()
        # content={'This content is deleted'}
        # return Response(content,status=status.HTTP_204_NO_CONTENT)
    


class WatchListAV(APIView):
    
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchSerializer(movies,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer=WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class WatchDetailAV(APIView):
    def get(self,request,pk):
        if request.method=='GET':
            try:
                movie=WatchList.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_204_NO_CONTENT)
            serializer = WatchSerializer(movie)
            return Response(serializer.data)
        
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors,status=400)
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        content={'error':"Content Not present"}
        return Response(content,status=status.HTTP_204_NO_CONTENT)
    
    
class StreamingListAV(APIView):
    def get(self,request):
        platform=StreamingPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
class StreamingDetailAV(APIView):
    def get(self,request,pk):
        if request.method=='GET':
            try:
                platform=StreamingPlatform.objects.get(pk=pk)
                
            except :
                return Response(status=status.HTTP_204_NO_CONTENT)
            serializer=StreamPlatformSerializer(platform)
            return Response(serializer.data,status=200)
        
    def put(self,request,pk):
        platform=StreamingPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=400)
    
    def delete(self,request,pk):
        platform=StreamingPlatform.objects.get(pk=pk)
        platform.delete()
        content={"Deleted ":"The content has been deleted"}
        return Response(content,status=status.HTTP_204_NO_CONTENT)
                
class ReviewListAV(generics.ListCreateAPIView):
    #queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(Watchlist=pk)
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
