from tkinter import *

from zmq import HELLO_MSG

# GUI
root = Tk()
root.title("Nyla")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()
	hello = ["hello", "hi", "hiiii", "hii", "hiii", "hola"]
	how_are_you = ["how are you", "how is your day", "how have you been"]
	userR = ["fine",  "i am good", "i am doing good" ]
	userR2 = [ "thanks", "thank you", "now its my time"]
	items = ["what do you sell", "what kinds of items are there", "have you something good"]
	joke = ["tell me a joke", "tell me something funny", "crack a funny line" ]
	goodbye = [ "goodbye", "see you later", "see yaa" ]
	
	print(hello)
	print(user)
	
	for x in [hello, how_are_you, userR, userR2, items, joke, goodbye]: 
		if (x == user):
			txt.insert(END, "\n" + "NYLA -> Hi there, how can I help?")

		if (x == user):
			txt.insert(END, "\n" + "NYLA -> fine! and you")
	
		if (x == user):
			txt.insert(END, "\n" + "NYLA -> Great! how can I help you.")
	
		if (x == user):
			txt.insert(END, "\n" + "NYLA -> My pleasure !")
	
		if (x == user):
			txt.insert(END, "\n" + "NYLA -> We have coffee and tea")
	
		if (x == user):
			txt.insert(END, "\n" + "NYLA -> What did the buffalo say when his son left for college? Bison.! ")
    

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
