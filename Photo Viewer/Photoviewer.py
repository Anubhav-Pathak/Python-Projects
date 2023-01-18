from tkinter import *
from PIL import ImageTk, Image
import random, os, re
dir = os.path.dirname(__file__)
images = os.listdir(os.path.join(dir,"Images"))
images = [image for image in images if re.search(r"(.jpg)|(.png)|(.jpeg)", image)]
root = Tk()
root.title("Image Viewer")
backward = Button(root, text="<", command=lambda: Move(n-1), pady=10, padx=10)
close = Button(root, text="Exit", command=root.quit, pady=10, padx=10)
forward = Button(root, text=">", command=lambda: Move(n+1), pady=10, padx=10)
backward.grid(row=1, column=0, pady=10)
close.grid(row=1, column=1, pady=10)
forward.grid(row=1, column=2, pady=10)
status = Label(root, bd=3, padx=10, pady=10, anchor=E, relief=SUNKEN)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
n = 0
def Move(i):
    global n
    n = i
    global image 
    image = ImageTk.PhotoImage(Image.open(os.path.join(dir,"Images",images[n])))
    if i < 1: backward["state"] = DISABLED
    elif i > len(images)-2: forward["state"] = DISABLED
    else: 
        backward["state"] = ACTIVE
        forward["state"] = ACTIVE
    img = Label(image=image, width=800, height=500)
    img.grid(row=0, column=0, columnspan=3)
    status["text"] = "Image "+str(i+1)+" of "+str(len(images))
Move(random.randint(0,len(images)-1))
root.mainloop()