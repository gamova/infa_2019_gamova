from graph import *

penColor(0, 0, 0)
brushColor('yellow') # face
circle(250,300,150)

brushColor('red') # left eye
circle(200,250,30)
brushColor('black')
circle(200,250,10)

brushColor('red') # right eye
circle(300,250,20)
brushColor('black')
circle(300,250,10)

rectangle(200,400, 300,420) #mouth

penSize(10)
moveTo(100,170) # left brow
lineTo(240,230)

moveTo(280,230)
lineTo(390,200)




'''point(1,1)
point(100,100)
point(200,200)
point(300,300)
moveTo(400,400)
lineTo(500,500)'''


run()
