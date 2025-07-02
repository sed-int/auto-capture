#!/opt/homebrew/bin/python3

import sys
import os
import time
import pyautogui

if len(sys.argv) != 6:
    print('USAGE: ./autopy [x1] [y1] [x2] [y2] [pages]')
    sys.exit(1)
## 숫자 745를 2로 나눈 이유는 2 Page를 한 화면으로 캡처하기 위함.
maxPage = int(sys.argv[5])

time.sleep(5)

for idx in range(maxPage):
    ## 숫자 110,170,1785,1205는 캡처할 화면의 위치에 대한 X-Y 좌표 값이다.
    ## 캡처할 때마다 이 숫자를 조정해서 사용해야 한다.
    
    x1, y1, x2, y2 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    w, h = x2-x1, y2-y1
    my_cmd = f'screencapture -R{x1},{y1},{w},{h} p_%04d.png' % idx
    # my_cmd = "screencapture p_%04d.png" % idx
   #  print("cmd:", my_cmd)
    os.system(my_cmd)

    # Print progress on the same line
    print(f"Progress: {idx + 1}/{maxPage} ({((idx + 1) / maxPage) * 100:.1f}%)", end="\r", flush=True)

    ## 오른쪽 화살표 키를 누르면서 한 화면씩 캡처하기.
    pyautogui.press('right')
    time.sleep(0.2)

print("Capture Completed!")
dir_name = 'book'
os.system(f'mv *.png {dir_name}')
