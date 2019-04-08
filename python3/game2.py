import easygui as g

t = g.msgbox('hello world')

image = "python_and_check_logo.gif"
msg = "Do you like this picture?"
choices = ["Yes","No","No opinion"]
reply = g.buttonbox(msg, image=image, choices=choices)
print(t,reply)