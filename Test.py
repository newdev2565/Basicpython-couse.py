import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงรางเป็นเต่า
def Rectangle():
    '''ฟังชั่้นนี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(90):
        tao.left(25)
        tao.forward(250)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Go(50,50)
Rectangle()
