import os
import re
import cv2 as cv
import numpy as np
path1="D:\\positive"
import os.path
picList = []
picname = []
surfix = []
#rootdir = "./123"
def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path) 
 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
 
# 定义要创建的目录
mkpath="d:\\product\\"
# 调用函数
mkdir(mkpath)
for lists in os.listdir(path1): 
#如果找到的是图片，则打印出来
    if lists[-3:]=='jpg':
        path = os.path.join(path1, lists) 
        picList.append(path)
        picname.append(lists)
        m=re.findall(r'(.+?)\.',lists)
        surfix.append(m)
        continue
for i in range(len(picList)):
    img = cv.imdecode(np.fromfile(picList[i], dtype=np.uint8), -1)
    for j in range(3):  # [1]column-----------height  [2]column-----------width
            if j == 0:
                newpic = img[0:2048, 0:985]
                cv.imencode('.jpg', newpic)[1].tofile(mkpath+" ".join(surfix[i])+"-1.jpg")
                print(1)
            elif j == 1:
                newpic = img[0:2048, 985:1537]
                cv.imencode('.jpg', newpic)[1].tofile(mkpath+" ".join(surfix[i])+"-2.jpg")
                print(2)
            else:
                newpic = img[0:2048, 1537:2448]   
                cv.imencode('.jpg', newpic)[1].tofile(mkpath+" ".join(surfix[i])+"-3.jpg")
                print(3)