from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from VideoApi.models import Snippet
# from VideoApi.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from VideoApi.myfunction import videoapi


@api_view(['GET'])
def GetVideoUrls(request):
    """
    列出所有的代码 snippet，或创建一个新的 snippet。
    """
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        list_url = videoapi.get_url_list()
        # data = JSONParser().parse(list_url)
        # serializer = SnippetSerializer(snippets, many=True)
        # class Response(data=None, status=None, template_name=None, headers=None, exception=False, content_type=None)
        # return JsonResponse(serializer.data, safe=False)
        return Response(data=list_url)

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