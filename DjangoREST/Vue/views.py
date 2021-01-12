from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['POST'])
def get_gitHub_accessToken(request):
    """获取AccessToken.

    Args:
        code: .
        client_id: 
        client_secret: 

    Returns:
        用户信息

    Raises:
        
    """
    if request.method == 'POST':
        # 获取传递的参数
        code = request.POST.get("code")
        client_id = request.POST.get("client_id")
        client_secret = request.POST.get("client_secret")
        # 组装参数
        payload = {"client_id": client_id,
                    "client_secret": client_secret,
                    "code": code}
        url = "https://github.com/login/oauth/access_token"
        res = requests.post(url=url, data=payload)
        list_re = res.text.split('&')
        if list_re[0] == 'error=bad_verification_code' :
            return Response(data="code过期了！", status=202)
        access_token = list_re[0].split('=')[1]
        return Response(data=access_token, status=200)
    else:
        return Response(data="请使用post发起请求！", status=202)





