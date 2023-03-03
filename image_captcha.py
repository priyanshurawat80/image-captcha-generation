from PIL import Image,ImageDraw,ImageFont
import random

cap_alpha=[]
sml_alpha=[]
num=[]
captcha=[cap_alpha,sml_alpha,num]
i=[]

for i in range(65,91):
    if chr(i)!='O':
        cap_alpha.append(chr(i))

for j in range(97,123):
     if chr(i)!='o':
        sml_alpha.append(chr(j))

for k in range(49,58):
    num.append(chr(k))

n=1
shift=0
o=Image.open('d:/captcha.jpg')
space=[115,120,130,135]
f1=ImageFont.truetype("arial.ttf",250)
f2=ImageFont.truetype("C:\Windows\Fonts\LHANDW.ttf",250)
f3=ImageFont.truetype("C:\Windows\Fonts\segoepr.ttf",300)
f4=ImageFont.truetype("C:\Windows\Fonts\FREESCPT.ttf",300)
font=[f1,f2,f3,f4,]
while n<=6:
    r=random.choice(captcha)
    i=random.choice(r)
    draw=ImageDraw.Draw(o)
    draw.text((100+shift,100),i,"black",font=random.choice(font),spacing=4)
    n+=1
    shift+=random.choice(space)

o.show()

