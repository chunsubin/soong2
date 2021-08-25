# 파이카메라로 찍는 사진의 최대 해상도는 2592*1944
# 최대 해상도로 촬영하려면 framerate를 15로 설정

from picamera import Picamera
from time import sleep
cnt=1
camera = PiCamera()
locate = 'home/pi/'
while(cnt<10):
    # camera.resolution = (2592, 1944)
    # camera.framerate = 15
    camera.start_preview()
    sleep(5) # 초점 맞추기 위해서 2초정도는 텀을 두는것이 좋음
    camera.capture('/home/pi/image%s.jpg' % i)
    camera.stop_preview()
    cnt+=1