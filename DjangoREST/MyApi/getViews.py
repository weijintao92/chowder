from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from MyApi.models import itellyou 
from MyApi.serializers import itellyouSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from MyApi.myfunction import videoapi,itellyou_function

my_key = "wjt123"

@api_view(['GET'])
def reptile_itellyou_base(request, pk):
    """ 
    我告诉你 网页基础分析
    """
    if pk != my_key:
        return HttpResponse(status=401)
    if request.method == 'GET':
        if itellyou_function.reptile_itellyou_base():
            return Response(data='成功！',status=200)
        else:
            return Response(status=404)

        
@api_view(['GET'])
def GetVideoUrls(request):
    """
    获取视频解析接口地址
    """
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        list_url = videoapi.get_url_list()
        # data = JSONParser().parse(list_url)
        # serializer = SnippetSerializer(snippets, many=True)
        # class Response(data=None, status=None, template_name=None, headers=None, exception=False, content_type=None)
        # return JsonResponse(serializer.data, safe=False)
        return Response(data=list_url)

@api_view(['GET'])
def get_itellyou_base(request):
    """
    获取基础基础数据
    """
    if request.method == 'GET':  
        serializer = itellyouSerializer(itellyou.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     获取，更新或删除一个代码 snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)