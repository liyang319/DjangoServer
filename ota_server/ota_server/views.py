from django.http import JsonResponse


def otacheck(request):
    # 处理请求的逻辑
    print(request.body)  # 打印请求的原始数据
    print(request.GET)  # 打印GET参数

    # 解析request中的参数
    cmd = request.GET.get('cmd')  # 获取GET参数
    ver = request.GET.get('version')  # 获取GET参数
    sn = request.GET.get('sn')  # 获取POST参数

    print('cmd=' + cmd + '-----ver=' + ver + '------sn=' + sn)

    # 例如，你可以在这里获取一些数据并返回json response
    data = {
        'status': 'success',
        'newVer': 'true',
        'url': 'http://192.168.80.235:8000/ota/good.zip',
        'md5': 'aaaaaaaaaaaaaaaaa'
    }
    return JsonResponse(data)
