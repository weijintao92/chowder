from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from MyApi.models import itellyou,itellyou_detali,itellyou_lang_edition,itellyou_software_message
from MyApi.serializers import itellyouSerializer,itellyou_detaliSerializer,itellyou_lang_editionSerializer,itellyou_software_messageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from MyApi.myfunction import videoapi,itellyou_function

my_key = "wjt123"



        
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
    获取“我告诉你”基础数据
    """
    if request.method == 'GET':  
        serializer = itellyouSerializer(itellyou.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def get_itellyou_detail(request):
    """
    获取“我告诉你“目录明细

    传递的参数是
    itellyou 的key
    """
    fk = request.POST.get("fk")
    if fk is None:
        return Response(data="获取传递参数失败！",status=404)
    if request.method == 'POST':  
        serializer = itellyou_detaliSerializer(itellyou_detali.objects.filter(father_key=fk), many=True)
        return Response(data=serializer.data)

@api_view(['POST'])
def get_itellyou_lang_edition(request):
    """
    获取“我告诉你“软件语言版本信息

    传递的参数是
    itellyou_detali 的key
    """
    fk = request.POST.get("fk")
    if fk is None:
        return Response(data="获取传递参数失败！",status=404)
    if request.method == 'POST':  
        serializer = itellyou_lang_editionSerializer(itellyou_lang_edition.objects.filter(father_key=fk), many=True)
        return Response(data=serializer.data)

@api_view(['POST'])
def get_itellyou_software_message(request):
    """
    获取“我告诉你“软件语言版本信息

    传递的参数是
    itellyou_lang_edition 的key
    """
    fk = request.POST.get("fk")
    if fk is None:
        return Response(data="获取传递参数失败！",status=404)
    if request.method == 'POST':  
        serializer = itellyou_software_messageSerializer(itellyou_software_message.objects.filter(father_key=fk), many=True)
        return Response(data=serializer.data)

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