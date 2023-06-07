from django.shortcuts import  HttpResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *



class user_opration(APIView):
    def get(self,request):
        user_data = user.objects.all()
        serializer = userserializers(user_data , many = True)
        return Response({'status':200 , 'payload':serializer.data })
    

    def post(self , request):
        serializer = userserializers(data= request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403 ,'error': serializer.errors,'message':'data is not valid' }  ) 
        serializer.save()
        return Response({'status':200,'payload':serializer.data , 'userstatus':'register successfully'})
    

    def patch(self,request):
        id = request.data.get("user_id")
        try:
            user_obj=  user.objects.get(user_id = id)
            serializer = userserializers(user_obj ,data= request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status':403 ,'message':'data is not valid' }  ) 
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response ({'status':403 ,'error': serializer.errors,'message':'data is not valid' })
        
    def delete(self,request):
        id = request.data.get("user_id")
        user_obj=user.objects.get(user_id=id)
        user_obj.delete()
        return Response({'status':200})

class content(APIView):
    def post(self , request):
        data= request.data
        print(data["owner"])
        input_status=(data["is_public"])
        inputdata=(data)
        objpost= Post_blog.objects.all()
        id1=[]
        owner=[]
        for i in objpost:
            owner.append(i.id)
            id1.append(int(i.owner))
        dict1=(dict(zip(owner,id1)))
        my_dict = dict1
        checkid = list(my_dict.keys())
        inputid=(inputdata["id"])
        ownerid=(inputdata["owner"])
        checked_id=(dict1[inputid])
        public = Post_blog.objects.values("is_public")
        for item in public:
            is_public = item['is_public']
            if is_public == False or input_status == False:
                if inputid in checkid:
                    if checked_id == ownerid:
                        posts = Post_blog.objects.filter(is_public=False,owner=ownerid)
                        serializer = postserializers(posts , many = True)
                        return Response({'status':200 , 'payload':serializer.data})
                    else:
                        return Response ({'status':403 ,'message':'data is not valid' })
                else:
                    return Response ({'status':403 ,'message':'data is not valid' })
                    
            else:
                return Response ({'status':403 ,'message':'data is not valid' })
  
    


class Post_blog_opration(APIView):
    def get(self,request):
        public = Post_blog.objects.values("is_public")
        for item in public:
            is_public = item['is_public']
            if is_public == True:
                posts = Post_blog.objects.filter(is_public=True)
                serializer = postserializers(posts , many = True)
            else:
               pass

        return Response({'status':200 , 'payload':serializer.data, "message": "for show a private content please post owner_id endpoint is /content"})
    

            
    def post(self , request):
        serializer = postserializers(data= request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403 ,'error': serializer.errors,'message':'data is not valid' }  ) 
        serializer.save()
        return Response({'status':200,'payload':serializer.data})
    

    def patch(self,request):
        id = request.data.get("id")
        data= request.data
        inputdata=(data)
        objpost= Post_blog.objects.all()
        id1=[]
        owner=[]
        for i in objpost:
            owner.append(i.id)
            id1.append(int(i.owner))
        dict1=(dict(zip(owner,id1)))
        my_dict = dict1
        checkid = list(my_dict.keys())
        inputid=(inputdata["id"])
        ownerid=(inputdata["owner"])
        checked_id=(dict1[inputid])
        print(checked_id)
        print(ownerid)
        if inputid in checkid:
            if checked_id == ownerid:
                try:
                    user_obj=  Post_blog.objects.get(id = id)
                    serializer = postserializers(user_obj ,data= request.data, partial=True)
                    if not serializer.is_valid():
                        return Response({'status':403 ,'message':'data is not valid' }  ) 
                    serializer.save()
                    return Response({'status':200,'payload':serializer.data})
                except Exception as e:
                    return Response ({'status':403 ,'error': serializer.errors,'message':'data is not valid' })
            else:
                return Response ({'status':403 ,'message':'data is not valid' })
        else:
            return Response ({'status':403 ,'message':'data is not valid' })

        
      
            
       
        
    def delete(self,request):
        id = request.data.get("id")
        data= request.data
        inputdata=(data)
        print(inputdata)
        objpost= Post_blog.objects.all()
        print(objpost)
        id1=[]
        owner=[]
        for i in objpost:
            owner.append(i.id)
            id1.append(int(i.owner))
    
        dict1=(dict(zip(owner,id1)))
        my_dict = dict1
        checkid = list(my_dict.keys())
        print(dict1)
        inputid=(inputdata["id"])
        ownerid=(inputdata["owner"])
        checked_id=(dict1[inputid])
        print(checked_id)
        print(ownerid)
        if inputid in checkid:
            if checked_id == ownerid:
                user_obj=Post_blog.objects.get(id=id)
                user_obj.delete()
            else:
                return Response ({'status':403 ,'message':'data is not valid' })
        else:
            return Response ({'status':403 ,'message':'data is not valid' })
        return Response ({'status':200 ,'message':'Data Deleted' })
       


####I know about viewsetall method but I use this crude costume because some times we need costume.

class Likes(APIView):
    def get(self,request):
        user_data = Like.objects.all()
        serializer = Likeserializers(user_data , many = True)
        return Response({'status':200 , 'payload':serializer.data})
    

    def post(self , request):
        serializer = Likeserializers(data= request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403 ,'error': serializer.errors,'message':'data is not valid' }  ) 
        serializer.save()
        return Response({'status':200,'payload':serializer.data})
    

    def patch(self,request):
        id = request.data.get("owner")
        try:
            user_obj=  Like.objects.get(owner = id)
            serializer = Likeserializers(user_obj ,data= request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status':403 ,'message':'data is not valid' }  ) 
            serializer.save()
            return Response({'status':200,'payload':serializer.data})
        except Exception as e:
            return Response ({'status':403 ,'error': serializer.errors,'message':'data is not valid' })
        
    def delete(self,request):
        id = request.data.get("user_id")
        user_obj=Like.objects.get(user_id=id)
        user_obj.delete()
        return Response({'status':200})
    





class Likecounts(APIView):
    def get(self, request):
        post_blogs = Post_blog.objects.filter(likes__isnull=False,is_public= True).select_related('owner').prefetch_related('likes')
        postid1=[]
        for i in post_blogs:
            postid1.append(i.id)
        data = postid1
        id_counts = {}
        for id in data:
            id_str = "post id " + str(id)
            if id_str in id_counts:
                id_counts[id_str] += 1
            else:
                id_counts[id_str] = 1
        #result = {f"{key}: likes {value}" for key, value in id_counts.items()}
        print(dict(id_counts))
        return Response(id_counts)
    
#6. The GET all post/blog API should also return the number of likes for each post/blog.


class postblogwithlike(APIView):
    def get(self,request):
        posts = Post_blog.objects.all()
        serializer = postserializers(posts , many = True)
        post_blogs = Post_blog.objects.filter(likes__isnull=False).select_related('owner').prefetch_related('likes')
        postid1=[]
        for i in post_blogs:
            postid1.append(i.id)
        data = postid1
        id_counts = {}
        for id in data:
            id_str = "post id " + str(id)
            if id_str in id_counts:
                id_counts[id_str] += 1
            else:
                id_counts[id_str] = 1
        #result = {f"{key}: likes {value}" for key, value in id_counts.items()}
        print(dict(id_counts))
        return Response({'status':200 , 'payload':serializer.data,"likes": id_counts})