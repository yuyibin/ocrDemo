from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect  #导入render模块
import os
import sys
from . import models
import cv2
sys.path.append(os.path.abspath('../'))
import model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]

def index(request):
    name = request.POST.get('name', None)
    password = request.POST.get('password', None)

    # 把用户和密码组装成字典
    data = {'name': name, 'password': password}
    list.append(data)

    return render(request, 'demo.html', {'form': list})

def Upload(request):
    if request.method == "GET":
        return render(request, "upload.html", {"name": "blank.jpg"})
    elif request.method == "POST":
        # 获取普通input标签值，即文件名
        filname = request.POST.get('fileName')
        # 获取file类型的input标签值，即文件内容
        file = request.FILES.get('fileContent')

        # 获取文件后缀名  C:\Program Files (x86)
        postfix = file.name.split('.')[1]
        # 设置本地文件路径
        file_path = os.path.join('D:\\django\\ocrDemo\\demo\\static', filname + '.' + postfix)
        models.image.objects.create(file_Path=file_path)

        # 将上传的文件写入本地目录
        f = open(file_path, "wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        im = cv2.imread(file_path)
        result, tmp, angle = model.model(
            im, model='keras', adjust=False, detectAngle=False)
        ocr_res = []
        print(result)
        i = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        for key in result:
            l = 20*len(str(i))
            if result[key][0][0]-l > 0 :
                left = result[key][0][0]-l
            else:
                left = result[key][0][2]
            cv2.putText(tmp, str(i), (left, result[key][0][5]), font, 1, (0, 0, 255), 3)
            ocr_res.append(str(i) + ": "+result[key][1])
            i = i+1
        cv2.imwrite(file_path, tmp)
        return render(request, "upload.html", {"name": filname + "." + postfix, "result": ocr_res})
