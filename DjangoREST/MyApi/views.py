from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from MyApi.models import Snippet
# from MyApi.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from MyApi.myfunction import videoapi,itellyou

my_pk = "1"

@csrf_exempt
def reptile_itellyou_base(request):
    """
    '我告诉你'爬虫基础
    """
    print(pk)
    if int(pk) != my_key:
        return HttpResponse(status=404)
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # list_url = videoapi.get_url_list()
        # data = JSONParser().parse(list_url)
        # serializer = SnippetSerializer(snippets, many=True)
        # class Response(data=None, status=None, template_name=None, headers=None, exception=False, content_type=None)
        # return JsonResponse(serializer.data, safe=False)
        return Response(data='333')


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
def itellyou_base(request):
    """
    我告诉你基础数据
    """
    if request.method == 'GET':
        itellyou.itellyou_base()
        return Response(data='22')

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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