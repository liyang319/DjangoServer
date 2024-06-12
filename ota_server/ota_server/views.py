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


def get_ota_status(data, sn):
    for device in data['devices']:
        if device['sn'] == sn and device['ota'] == 'update':
            return 'update'
    return "none"


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
    checkVer = -1
    if currentVer == 'none':
        checkVer = 0
    else:
        checkVer = compare_version(currentVer, newVer)
    print('checkVer=' + str(checkVer))
    # hasNewVer = False;
    # if checkVer < 0:
    #     hasNewVer = True
    # aaa = get_ota_status(json_ota_data, sn)
    # print('------' + aaa)

    data = {
        'status': 'success',
        'needUpdate': 'true' if checkVer < 0 and get_ota_status(json_ota_data, sn) == 'update' else 'false',
        'newVer': newVer,
        'url': json_ota_data['url'],
        'md5': json_ota_data['md5']
    }
    return JsonResponse(data)


# 文件上传处理函数
def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # 每个设备号新建一个文件夹
        device_sn = request.POST.get('deviceSN')
        # print('---device_sn---' + device_sn)
        log_dir = settings.UPLOAD_DIR + device_sn;
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        dest_name = settings.UPLOAD_DIR + device_sn + '/' + file_name
        # print('----filename-----' + (settings.UPLOAD_DIR + device_sn + '/' + file_name))
        with open(dest_name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    else:
        return JsonResponse({'error': 'No file provided'}, status=400)


def device_log_check(request):
    print(request.GET)  # 打印GET参数
    device_sn = request.GET.get('sn')  # 获取GET参数
    # device_sn = "4854604D7765A027"
    with open(settings.LOG_CONFIG_PATH + 'device_log_config', 'r') as file:
        json_data = json.load(file)
    print(json_data)
    log_status, log_date = get_log_status(json_data, device_sn)

    data = {
        'status': 'success',
        'log': log_status,
        'date': log_date,
        'path': settings.UPLOAD_DIR
    }
    return JsonResponse(data)


def get_log_status(data, sn):
    for device in data['devices']:
        if device['sn'] == sn:
            return device['log'], device['date']
    return "none", "none"

