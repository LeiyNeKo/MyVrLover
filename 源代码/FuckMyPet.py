import time
import requests
import keyboard

gap = 100 # ”时间差“
gaps = [] # ”时间差“集
gap_time = 0 # 上次结束长按的时间
press = False

while True:
    if keyboard.is_pressed('space') and press == False:
        press = True
        press_time = time.time() # 获取按下的时间
    elif not keyboard.is_pressed('space') and press == True:
        press = False
        gap = time.time() - press_time # 计算按下到抬起的“时间差”
        gap_time = time.time() # 更新结束长按的时间
        requests.get('http://127.0.0.1/set_gap?gap='+str(gap)) # 将“时间差”传给服务器
        gaps += [str(gap)]
        print('本次时间差:' + str(gap))
    elif keyboard.is_pressed('enter'): # 按回车生成统计数据
        f = open("时间差统计.txt", "w")
        f.write('\n'.join(gaps))
        f.close()
    if time.time() - gap_time > gap + 1: # 长时间未”运动“的情况
        requests.get('http://127.0.0.1/set_gap?gap=100')