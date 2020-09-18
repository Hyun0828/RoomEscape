
from bangtal import *
# pip install bangtal

scene1=Scene('장면1', 'Images/배경-1.png')

def scene1_onEnter():
    showMessage('단서를 찾아 제한시간내에 탈출하세요!')
scene1.onEnter=scene1_onEnter

door1=Object('Images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()

keypad3=Object('Images/키패드.png')
keypad3.locate(scene1, 450, 700)
keypad3.show()

books=Object('Images/책장.png')
books.locate(scene1, 140, 240)
books.setScale(0.8)
books.show()

air=Object('Images/에어컨.png')
air.locate(scene1, 1050, 150)
air.show()

L=Object('Images/8.png')
L.locate(scene1, 0, 130)
L.setScale(0.3)

I=Object('Images/8.png')
I.locate(scene1, 450, 350)
I.setScale(0.3)

G=Object('Images/8.png')
G.locate(scene1, 400, 575)
G.setScale(0.3)

Ja1=Object('Images/액자.png')
Ja1.locate(scene1, 350, 375)
Ja1.show()

Ja2=Object('Images/액자.png')
Ja2.locate(scene1, 365, 575)
Ja2.show()

switch0=Object('Images/스위치.png')
switch0.locate(scene1, 500, 700)
switch0.show()

key=Object('Images/열쇠.png')
key.setScale(0.2)
key.locate(scene1, 400, 150)

flowerpot=Object('Images/화분.png')
flowerpot.locate(scene1, 0, 130)
flowerpot.show()

flowerpot1=Object('Images/화분.png')
flowerpot1.locate(scene1, 620, 300)
flowerpot1.show()

flowerpot2=Object('Images/화분.png')
flowerpot2.locate(scene1, 700, 0)
flowerpot2.show()

scene2=Scene('장면2', 'Images/배경-2.png')

boxclo=Object('Images/금고닫힘.png')
boxclo.locate(scene2, 520, 310 )
boxclo.setScale(0.4)
boxclo.show()

keypad0=Object('Images/키패드.png')
keypad0.locate(scene2, 590, 420)
keypad0.show()

hint=Object('Images/힌트.png')
hint.locate(scene2, 330, 610)
hint.setScale(0.5)

paper=Object('Images/종이.png')
paper.locate(scene2, 585, 460)
paper.setScale(0.05)

Hint=Object('Images/금고힌트.png')
Hint.locate(scene2, 700, 540)
Hint.setScale(0.25)

door2=Object('Images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()

digital=Object('Images/숫자.png')
digital.locate(scene2, 330, 60)

door3=Object('Images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.show()

keypad=Object('Images/키패드.png')
keypad.locate(scene2, 885, 420)
keypad.show()

switch=Object('Images/스위치.png')
switch.locate(scene2, 880, 440)
switch.show()

scene3=Scene('장면3', 'Images/어두운방문.png')
scene4=Scene('장면4', 'Images/어두운방입장.png')
scene5=Scene('장면5', 'Images/탈출성공.png')

door4=Object('Images/방문닫힘.png')
door4.locate(scene3, 550, 195)
door4.show()

wifi=Object('Images/와이파이.png')
wifi.locate(scene3, 440, 420)
wifi.setScale(0.29)
wifi.show()

mirror=Object('Images/원형 거울.png')
mirror.locate(scene3, 750, 420)
mirror.setScale(0.45)
mirror.show()

keypad2=Object('Images/키패드.png')
keypad2.locate(scene3, 500, 370)
keypad2.show()

one=Object('Images/원주율.png')
one.locate(scene3,410,30)
one.setScale(0.6)

arrow=Object('Images/화살표.png')
arrow.locate(scene4, 620, 480)
arrow.setScale(0.1)
arrow.show()

end=Object('Images/끝.png')
end.locate(scene5, 900, 0)
end.show()

timer1=Timer(300)
showTimer(timer1)
timer1.start()

def timer1_onTimeout():
        showMessage('탈출에 실패하였습니다!')
timer1.onTimeout=timer1_onTimeout

door1.closed=True
def door1_onMouseAction(x,y,action):
    if door1.closed==True:
        if key.inHand()==True:
            door1.setImage('Images/문-오른쪽-열림.png')
            door1.closed=False
        else:
            showMessage('열쇠가 필요합니다')
    else:
        scene2.enter()
door1.onMouseAction=door1_onMouseAction

def key_onMouseAction(x,y,action):
    key.pick()
key.onMouseAction=key_onMouseAction

def Ja1_onMouseAction(x,y,action):
    I.show()
Ja1.onMouseAction=Ja1_onMouseAction

def Ja2_onMouseAction(x,y,action):
    G.show()
Ja2.onMouseAction=Ja2_onMouseAction

switch0.lighted=True
def switch0_onMouseAction(x,y,action):
    switch0.lighted = not switch0.lighted
    if switch0.lighted:
        scene1.setLight(0.25)
        key.show()
    else:
        scene1.setLight(1)
        key.hide()
switch0.onMouseAction=switch0_onMouseAction

flowerpot.moved=False
def flowerpot_onMouseAction(x,y,action):
    if flowerpot.moved==False:
        if action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 50, 130)
            flowerpot.moved=True
            L.show()
flowerpot.onMouseAction=flowerpot_onMouseAction

flowerpot1.moved=False
def flowerpot1_onMouseAction(x,y,action):
    if flowerpot1.moved==False:
        if action == MouseAction.DRAG_RIGHT:
            flowerpot1.locate(scene1, 670, 300)
            flowerpot1.moved=True
        elif action == MouseAction.DRAG_LEFT:
            flowerpot1.locate(scene1, 570, 300)
            flowerpot1.moved=True
flowerpot1.onMouseAction=flowerpot1_onMouseAction

flowerpot2.moved=False
def flowerpot2_onMouseAction(x,y,action):
    if flowerpot2.moved==False:
        if action == MouseAction.DRAG_RIGHT:
            flowerpot2.locate(scene1, 800, 0)
            flowerpot2.moved=True
        elif action == MouseAction.DRAG_LEFT:
            flowerpot2.locate(scene1, 500, 0)
            flowerpot2.moved=True
flowerpot2.onMouseAction=flowerpot2_onMouseAction

air.moved=False
def air_onMouseAction(x,y,action):
    if air.moved==False:
        if action == MouseAction.DRAG_RIGHT:
            air.locate(scene1, 1100, 0)
            air.moved=True
        elif action == MouseAction.DRAG_LEFT:
            air.locate(scene1, 1000, 0)
            air.moved=True
air.onMouseAction=air_onMouseAction

def door2_onMouseAction(x,y,action):
    scene1.enter()
door2.onMouseAction=door2_onMouseAction

switch0.locked=True
switch0.lighted=True
def switch0_onMouseAction(x,y,action):
    if switch0.locked:
        showMessage('스위치가 눌리지 않는다, 키패드를 눌러보자')
    else:
        switch0.lighted = not switch0.lighted
        if switch0.lighted:
            scene1.setLight(0.35)
            key.show()
        else:
            scene1.setLight(1)
switch0.onMouseAction=switch0_onMouseAction


def switch0_onKeypad():
    switch0.locked=False
    showMessage('스위치를 눌러보자')
switch0.onKeypad=switch0_onKeypad

def keypad3_onMouseAction(x,y,action):
    showKeypad('888', switch0)
keypad3.onMouseAction=keypad3_onMouseAction

def keypad0_onMouseAction(x,y,action):
    showKeypad('101', boxclo)
    Hint.show()
keypad0.onMouseAction=keypad0_onMouseAction

def boxclo_onKeypad():
    boxclo.locked=False
    showMessage('금고가 열렸다!!')
boxclo.onKeypad=boxclo_onKeypad

boxclo.locked=True
boxclo.closed=True
def boxclo_onMouseAction(x,y,action):
    if boxclo.locked:
         showMessage('금고가 잠겨있다!!')
    elif boxclo.closed:
         boxclo.setImage('Images/금고열림.png')
         paper.show()
         keypad0.hide()
         boxclo.closed=False
    else:
         hint.show()
boxclo.onMouseAction=boxclo_onMouseAction

def paper_onMouseAction(x,y,action):
    hint.show()
paper.onMouseAction=paper_onMouseAction


door3.locked=True
door3.closed=True
def door3_onMouseAction(x,y,action):
    if door3.locked:
         showMessage('문이 잠겨있다!!')
    elif door3.closed:
         door3.setImage('Images/문-오른쪽-열림.png')
         door3.closed=False
    else:
         scene3.enter()
door3.onMouseAction=door3_onMouseAction

def door3_onKeypad():
    door3.locked=False
    showMessage('문이 열렸다!!')
door3.onKeypad=door3_onKeypad 

door4.locked=True
door4.closed=True
def door4_onMouseAction(x,y,action):
    if door4.locked:
         showMessage('문이 잠겨있다!!')
    elif door4.closed:
         scene4.enter()
         door4.closed=False
door4.onMouseAction=door4_onMouseAction

def door4_onKeypad():
    door4.locked=False
    showMessage('문이 열렸다!!')
door4.onKeypad=door4_onKeypad

def keypad_onMouseAction(x,y,action):
    showKeypad('191', door3)
keypad.onMouseAction=keypad_onMouseAction

def keypad2_onMouseAction(x,y,action):
    one.show()
    showKeypad('006', door4)
keypad2.onMouseAction=keypad2_onMouseAction

switch.lighted=True
def switch_onMouseAction(x,y,action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(0.25)
        digital.show()
    else:
        scene2.setLight(1)
        digital.hide()
switch.onMouseAction=switch_onMouseAction

def arrow_onMouseAction(x,y,action):
    scene5.enter()
arrow.onMouseAction=arrow_onMouseAction

def scene5_onEnter():
    showMessage('탈출 성공!')
scene5.onEnter=scene5_onEnter

def end_onMouseAction(x,y,action):
    endGame()
end.onMouseAction=end_onMouseAction

startGame(scene1)