from PIL import Image,ImageFilter
from playsound import playsound
while(True):
    name=input("enter the name of that person you want to make the sketch : ")
    
    def sketch(s):
        
        name==s
        img= Image.open(name+'.jpg')
        filterimg=img.filter(ImageFilter.BLUR)  
        filterimg=img.convert('L')
        filterimg.save("grey.png",'png')

        filterimg.show()
        

    if name=="roshan":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
        sketch(name)
    if name=="gang":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
        sketch(name)
    if name=="sunil":
        print("sketch is getting ready wait")
        playsound('beep.mp3')
        sketch(name)

    else:
        print("data not found")
        playsound('notfound.mp3')
