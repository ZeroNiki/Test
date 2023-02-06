from tkinter import *
import random, time

def throw():
	x = random.choice(['reference/b1.png', 'reference/b2.png', 'reference/b3.png',
					   'reference/b4.png', 'reference/b5.png', 'reference/b6.png'])

	return x

def img(event):
	global b1, b2
	for i in range(18):
		b1 = PhotoImage(file = throw())
		b2 = PhotoImage(file = throw())
		lab1['image'] = b1
		lab2['image'] = b2
		root.update()
		time.sleep(0.12)


#Interface
root = Tk()
root.geometry('400x200')
root.title('Игра в кости')
root.resizable(height = False, width = False)

#Icon
photo = PhotoImage(file = r"reference\ico.png")
root.iconphoto(False, photo)

#BG
font = PhotoImage(file= r"reference\background.png")
Label(root, image=font).pack()

#bones 1
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

#bones 2
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

#Button
root.bind('<1>', img)
img('event')

#End
root.mainloop()

