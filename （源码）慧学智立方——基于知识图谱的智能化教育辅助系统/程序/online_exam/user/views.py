from django.shortcuts import render
import cv2
from .models import UserTable,Student,Teacher
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from PIL import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import os
import traceback
import json
import time
import requests
import wave
import pyaudio
import shutil
from django.core.files.storage import default_storage
from flask import Flask, request, jsonify
from django.conf import settings
from django.shortcuts import render
from pathlib import Path





UPLOAD_FOLDER = 'D:\\Langchain-Chatchat\\yuwenzuowen'

# from utils.mypage import Pagination

def personal(req):

    username = req.session['username']

    result = UserTable.objects.filter(name=username).first()
    return render(req,'personal.html',locals())


def register(request):
    """
    添加员工
    :return:
    """
    try:
        number = request.POST.get('number_std')
        username = request.POST.get('username_std')
        passwd = request.POST.get('password1')
        phone = request.POST.get('phone')
        user = UserTable.objects.filter(name=username)
        if user:
            return JsonResponse({'message': '用户已存在,请直接登录'}, status=403)
        Student.objects.create(
            number=number,
            name=username,
            password=passwd,
            phone=phone,
            role=1,
        )
        response_data = {'message': '注册成功'}
        return JsonResponse(response_data)
    except Exception as e:
        print(e)
        return JsonResponse({'message': '注册失败'}, status=401)


def get_user(request):
    """
    获取用户列表信息 | 模糊查询
    :param request:
    :return:
    """
    keyword = request.GET.get('name')
    page = request.GET.get("page", '')
    limit = request.GET.get("limit", '')
    role_id = request.GET.get('position', '')
    response_data = {}
    response_data['code'] = 0
    response_data['msg'] = ''
    data = []
    if keyword is None:
        results = Student.objects.all()
        paginator = Paginator(results, limit)
        results = paginator.page(page)
        if results:
            for user in results:
                record = {
                    "id": user.id,
                    'number':user.number,
                    "name": user.name,
                    "password": user.password,
                    "phone": user.phone,
                    'gender':user.gender,
                    "age": user.age,
                }
                data.append(record)
            response_data['count'] = len(Student.objects.all())
            response_data['data'] = data
    else:
        users_all = Student.objects.filter(name__contains=keyword).all()
        paginator = Paginator(users_all, limit)
        results = paginator.page(page)
        if results:
            for user in results:
                record = {
                    "id": user.id,
                    'number': user.number,
                    "name": user.name,
                    "password": user.password,
                    "phone": user.phone,
                    'gender': user.gender,
                    "age": user.age,
                }
                data.append(record)
            response_data['count'] = len(users_all)
            response_data['data'] = data
    print(data)
    return JsonResponse(response_data)


def user(request):
    username = request.session['username']
    role = request.session["role"]
    return render(request, 'user.html', locals())


def login_check(request):
    response_data = {}
    name = request.GET.get('username')
    password = request.GET.get('password')
    role= int(request.GET.get('role'))
    if role==1:
        user = Student.objects.filter(number=name, password=password).first()
        request.session["xuehao"] = user.number
    else:
        user = Teacher.objects.filter(number=name, password=password).first()
    info = {}
    if user:
        # 将用户名存入session中
        request.session["username"] = user.name
        request.session["role"] = user.role
        request.session["user_id"] = user.id
        response_data['message'] = '登录成功'
        return JsonResponse(response_data, status=201)
    else:
        return JsonResponse({'message': '用户名或者密码不正确'}, status=401)
def modify_password(req):
    return render(req,'modify_password.html')

def edit_user(request):
    response_data = {}
    user_id = request.POST.get('id')
    username = request.POST.get('username')
    number = request.POST.get('number')
    phone = request.POST.get('phone')
    age = request.POST.get('age')

    Student.objects.filter(id=user_id).update(
        number=number,
        name=username,
        phone=phone,
        age=age)
    response_data['msg'] = 'success'
    return JsonResponse(response_data, status=201)


def del_user(request):
    user_id = request.POST.get('id')
    print(user_id)
    result = Student.objects.filter(id=user_id).first()
    try:
        if not result:
            response_data = {'error': '删除用户信息失败！', 'message': '找不到id为%s的用户' % user_id}
            return JsonResponse(response_data, status=403)
        result.delete()
        response_data = {'message': '删除成功！'}
        return JsonResponse(response_data, status=201)
    except Exception as e:
        response_data = {'message': '删除失败！'}
        return JsonResponse(response_data, status=403)


def change_password(request):
    # 修改密码
    user = UserTable.objects.filter(name=request.session["username"]).first()
    if user.password == request.POST.get('changePassword'):
        # 修改的密码与原密码重复不予修改
        return JsonResponse({"msg": "修改密码与原密码重复"}), 406
    else:
        # 不重复，予以修改
        UserTable.objects.filter(name=request.session["username"]).update(
            password=request.POST.get('changePassword'))
        # 清除session回到login界面
        del request.session['username']
        return JsonResponse({"msg": "success"})


def login_out(req):
    del req.session['username']
    return HttpResponseRedirect('/')

# ===================================人脸识别==============================================================
class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass

    # 进行sha256加密和base64编码


def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    u = Url(host, path, schema)
    return u


def assemble_ws_auth_url(requset_url, method="GET", api_key="", api_secret=""):
    u = parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date = format_date_time(mktime(now.timetuple()))
    print(date)
    # date = "Thu, 12 Dec 2019 01:57:27 GMT"
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    print(signature_origin)
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    print(authorization_origin)
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }

    return requset_url + "?" + urlencode(values)


def gen_body(appid, img1_path, img2_path, server_id):
    with open(img1_path, 'rb') as f:
        img1_data = f.read()
    with open(img2_path, 'rb') as f:
        img2_data = f.read()
    body = {
        "header": {
            "app_id": appid,
            "status": 3
        },
        "parameter": {
            server_id: {
                "service_kind": "face_compare",
                "face_compare_result": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "json"
                }
            }
        },
        "payload": {
            "input1": {
                "encoding": "jpg",
                "status": 3,
                "image": str(base64.b64encode(img1_data), 'utf-8')
            },
            "input2": {
                "encoding": "jpg",
                "status": 3,
                "image": str(base64.b64encode(img2_data), 'utf-8')
            }
        }
    }
    return json.dumps(body)


def run(appid, apikey, apisecret, img1_path, img2_path, server_id='s67c9c78c'):
    url = 'http://api.xf-yun.com/v1/private/{}'.format(server_id)
    request_url = assemble_ws_auth_url(url, "POST", apikey, apisecret)
    headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': appid}
    print(request_url)
    response = requests.post(request_url, data=gen_body(appid, img1_path, img2_path, server_id),
                             headers=headers)
    resp_data = json.loads(response.content.decode('utf-8'))

    a = base64.b64decode(resp_data['payload']['face_compare_result']['text']).decode()
    # 使用 json.loads() 将字符串转换为字典
    dict_data = json.loads(a)
    face_score = dict_data["score"]
    print('照片比对相似度：', face_score)
    if (face_score >= 0.666):
        return 1
    else:
        return 0
# =========================================人脸识别2=============================================================
def student_face_login(request):
    # 获取POST请求中的'action'参数
    action = request.POST.get('action')
    if int(action) == 1:
        camera = cv2.VideoCapture(0)
        # 拍照
        ret, frame = camera.read()
        # 确保图片读取成功
        if not ret:
            return JsonResponse({'error': 'Failed to capture image'}, status=500)
        # 将图片从 OpenCV 格式转换为 PIL 格式
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        timestamp = str(int(time.time()))
        save_dir = Path(settings.MEDIA_ROOT) / 'facephoto'

        # 定义保存图片的路径
        photo_path = os.path.join(save_dir, f"captured_face_{timestamp}.jpg")
        # 保存图片
        img.save(photo_path)
        # 释放摄像头资源
        camera.release()
    # ============================================================================================
        result_sorce=run(
            appid='4626a4ce',
            apisecret='OTg0Y2E3MTIwOWU4MDc1YzQ1ZTE5MTgz',
            apikey='f7a10584a7234e3de1cfcf49f76b1054',
            img1_path=save_dir/'ok.jpg',
            img2_path=photo_path,
        )
        if result_sorce==1:
            print('人脸识别通过！')
            return JsonResponse({'result': 'pass'}, status=200)
        else:print('人脸识别不通过！请本人或稍后重试')
        return render(request, 'login.html', {'message': '登录成功'})

# =======================================声纹登录================================================================


CHUNK = 1024  # 录音块大小
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 单声道
RATE = 44100  # 采样率
RECORD_SECONDS = 4  # 录音时间（秒）
WAVE_OUTPUT_FILENAME = "output.wav"  # 输出文件名

def record_audio():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # 保存录音
    save_audio(frames)

def save_audio(frames):
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # 移动文件到指定目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_filename = f"output_{timestamp}.mp3"
    new_file_path = os.path.join("D:\\Langchain-Chatchat\\sounds", unique_filename)

    shutil.move(WAVE_OUTPUT_FILENAME, new_file_path)

def student_sound_login(request):
    action = request.POST.get('action')
    if int(action) == 1:
        record_audio()

        return JsonResponse({'result': 'pass'}, status=200)
    else:
        return JsonResponse({"status": "failure"})
# =========================================================================================================
# def uphomework(request):
#     if request.method == 'POST':
#         file = request.FILES.get('file')
#         if file:
#             # 保存文件到指定路径
#             file_path = default_storage.save('Langchain-Chatchat/homework_photos/' + file.name, file)
#             return JsonResponse({"status": "2"})
#         else:
#             return JsonResponse({"status": "error"}, status=400)
#     return JsonResponse({"status": "error"}, status=405)

def upload_zuowen_photo(request):
    if request.method == 'POST':
        if 'photo' not in request.FILES:
            return JsonResponse({'error': '没有文件部分'}, status=400)
        file = request.FILES['photo']
        if not file.name:
            return JsonResponse({'error': '没有选择文件'}, status=400)

        # 确保上传目录存在
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file_path = os.path.join(UPLOAD_FOLDER, file.name)

        # 将文件保存到指定目录
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return JsonResponse({'message': 'ok'})
    else:
        return JsonResponse({'error': '无效的请求方法'}, status=405)









