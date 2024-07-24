from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def genrate():
    linkName=nameEntry.get()
    link=genEntry.get()
    fileName = linkName + ".png"
    url=pyqrcode.create(link)
    url.png(fileName, scale=7)
    qrImg=ImageTk.PhotoImage(Image.open(fileName))
    qrImgLbl=Label(image=qrImg)
    qrImgLbl.image=qrImg
    canvas.create_window(200,450,window=qrImgLbl)

# def genrate():
#     linkName = nameEntry.get()
#     link = genEntry.get()
#     fileName = genEntry.get() + ".png"  # Corrected line
#     url = pyqrcode.create(link)
#     url.png(fileName, scale=7)
#     qrImg = ImageTk.PhotoImage(Image.open(fileName))
#     qrImgLbl = Label(image=qrImg)
#     qrImgLbl.image = qrImg
#     canvas.create_window(200, 450, window=qrImgLbl)

root=Tk()

canvas=Canvas(root, width=400, height=600)
canvas.pack()

appLabel = Label(root, text="QR Code Generator", fg='blue', font=('Arial', 30))
canvas.create_window(200,50, window=appLabel)


nameLinkLabel=Label(root, text="Name link:")
genLinkLabel=Label(root, text="Paste link:")
canvas.create_window(200,100, window=nameLinkLabel)
canvas.create_window(200,160,window=genLinkLabel)


nameEntry=Entry(root)
genEntry=Entry(root)
canvas.create_window(200,130, window=nameEntry)
canvas.create_window(200,180,window=genEntry)


btn=Button(text="Genrate QR Code",command=genrate)
canvas.create_window(210,215,window=btn)


root.mainloop()