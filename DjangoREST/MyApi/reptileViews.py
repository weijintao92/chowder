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


@api_view(['POST'])
def reptile_itellyou_detail(request, pk):
    """ 
    我告诉你 目录明细获取

    https://msdn.itellyou.cn/Index/GetCategory
    Request Method: POST
    formdata
    id: AFF8A80F-2DEE-4BBA-80EC-611AC56D3849
    """
    #
    if pk != my_key:
        return HttpResponse(status=401)
    if request.method == 'POST':
        if itellyou_function.reptile_itellyou_detail():
            return Response(data='成功！',status=200)
        else:
            return Response(status=404)
        

@api_view(['POST'])
def reptile_itellyou_finaldata(request, pk):
    """ 
    获取：我告诉你 最终数据；

    获取当前语言版本；
    获取软件具体信息
    https://msdn.itellyou.cn/Index/GetLang
    Request Method: POST
    formdata
    id: d15691d5-9208-4a7b-b8f8-b64cf6fb875a


    #根据名称和语言版本获取具体的软件信息
    https://msdn.itellyou.cn/Index/GetList
    Request Method: POST
    formdata
    id: d15691d5-9208-4a7b-b8f8-b64cf6fb875a
    lang: e15db4de-c094-4c50-822a-98ad50daba4f
    filter: true


    """
    #
    if pk != my_key:
        return HttpResponse(status=401)
    if request.method == 'POST':
        if itellyou_function.reptile_itellyou_finaldata():
            return Response(data='成功！',status=200)
        else:
            return Response(status=404)
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