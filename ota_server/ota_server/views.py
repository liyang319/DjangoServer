from django.http import JsonResponse
from django.conf import settings
import os
import json


def compare_version(version1, version2):
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        return 0


def get_ota_info():
    # 读取服务器本地文件内容
    file_name = 'version_info'
    file_path = os.path.join(settings.OTA_ROOT, file_name)
    print('-----filepath-----' + file_path)
    if os.path.exists(file_path):  # 判断文件是否存在
        with open(file_path, 'r') as file:  # 打开文件
            file_content = file.read()  # 读取文件内容
    else:
        file_content = ''  # 文件不存在时返回提示信息
    return file_content

def otacheck(request):
    # 处理请求的逻辑
    # print(request.body)  # 打印请求的原始数据
    # print(request.GET)  # 打印GET参数

    # 解析request中的参数
    cmd = request.GET.get('cmd')  # 获取GET参数
    currentVer = request.GET.get('version')  # 获取GET参数
    sn = request.GET.get('sn')  # 获取POST参数

    print('cmd=' + cmd + '-----ver=' + currentVer + '------sn=' + sn)
    otaInfo = get_ota_info()
    print('otaInfo = ' + otaInfo)
    json_ota_data = json.loads(otaInfo)

    newVer = json_ota_data['version']
    checkVer = compare_version(currentVer, newVer)
    # hasNewVer = False;
    # if checkVer < 0:
    #     hasNewVer = True

    data = {
        'status': 'success',
        'needUpdate': 'true' if checkVer < 0 else 'false',
        'newVer': newVer,
        'url': json_ota_data['url'],
        'md5': json_ota_data['md5']
    }
    return JsonResponse(data)


# 文件上传处理函数
def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        print('----filename-----' + (settings.UPLOAD_DIR + file_name))
        with open(settings.UPLOAD_DIR + file_name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    else:
        return JsonResponse({'error': 'No file provided'}, status=400)