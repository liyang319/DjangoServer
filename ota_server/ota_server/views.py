from django.http import JsonResponse


def otacheck(request):
    # 处理请求的逻辑
    # 例如，你可以在这里获取一些数据并返回json response
    data = {
        'status': 'success',
        'message': 'OTA check successful'
    }
    return JsonResponse(data)
