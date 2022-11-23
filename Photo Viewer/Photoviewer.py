from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()
root.title("Image Viewer")
img1 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Adventure.jpg"))
img2 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Classroom.jpg"))
img3 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Cooking.jpg"))
img4 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Couples.jpg"))
img5 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Detective.jpg"))
img6 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Longing.jpg"))
img7 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Music.jpg"))
img8 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Samurai.jpg"))
img9 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Shed.jpg"))
img10 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Submarine.jpg"))
img11 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Sunrise.jpg"))
img12 = ImageTk.PhotoImage(Image.open("Projects\Photo Viewer\Images\Winter.jpg"))
n = 0
imglist = (img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12)
backward = Button(root, text="<", command=lambda: Move(n-1), pady=10, padx=10)
close = Button(root, text="Exit", command=root.quit, pady=10, padx=10)
forward = Button(root, text=">", command=lambda: Move(n+1), pady=10, padx=10)
backward.grid(row=1, column=0, pady=10)
close.grid(row=1, column=1, pady=10)
forward.grid(row=1, column=2, pady=10)
status = Label(root, bd=3, padx=10, pady=10, anchor=E, relief=SUNKEN)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
def Move(i):
    global n
    n = i
    if i < 1: backward["state"] = DISABLED
    elif i > len(imglist)-2: forward["state"] = DISABLED
    else: 
        backward["state"] = ACTIVE
        forward["state"] = ACTIVE
    img = Label(image=imglist[i], width=800, height=500)
    img.grid(row=0, column=0, columnspan=3)
    status["text"] = "Image "+str(i+1)+" of "+str(len(imglist))
Move(random.randint(0,len(imglist)-1))
root.mainloop()