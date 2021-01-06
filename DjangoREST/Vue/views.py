from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.

@api_view(['POST'])
def get_gitHub_accessToken(request):
    """获取gitHub的AccessToken

    向https://github.com/login/oauth/access_token发起POST请求，传递3个参数client_id、client_secret、code
    得到gitHub的AccessToken

    Args:
        client_id: 
        client_secret: 
        code: 

    Returns:
        AccessToken

    Raises:
    """
    if request.method == 'POST':
        # 获取传递的参数
        code = request.POST.get("code")
        my_type = request.POST.get("my_type")
        # 组装参数
        if my_type==='dev':
            payload  = '{"client_id":"5eeb1fbb5d00630d81d0",
        "client_secret":"56aa7da20ef8fb37fe33989ea0477d89a275ad09",
        "code":code}'
        else:
            payload  = '{"client_id":"dfa7e273d6764be24415",
        "client_secret":"86c6a06bf205a4058f6684173bfff945d4c1a71a",
        "code":code}'
        

        url = "https://github.com/login/oauth/access_token"
        res = requests.post(url=url,data=payload)
        return Response(data=res.text)




