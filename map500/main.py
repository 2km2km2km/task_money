# coding=utf-8
#插入文件图片
from tkinter  import*
from PIL import Image
#import ImageTk
root = Tk()

frame =Frame(width=500,height=400,bg='red')
frame.grid()
canvas=Canvas(frame,bg='blue')
canvas.grid(padx=10,pady=10)
#image = Image.open("./maps_img/1.png")  
#im = ImageTk.PhotoImage(image)  
im=PhotoImage(file="./maps_img/1.png")
canvas.create_image(300,50,image = im)  

'''
#创建一个标签类, [justify]:对齐方式
textLabel = tk.Label(root,text="你在右边会看到一个图片，\n我在换个行",
justify = tk.LEFT)#左对齐
textLabel.pack(side=tk.LEFT)#自动对齐,side：方位

 

#创建一个图片管理类
photo = tk.PhotoImage(file="./maps_img/1.png")#file：t图片路径
imgLabel = tk.Label(root,image=photo)#把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)#自动对齐
'''

mainloop()