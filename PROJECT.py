#It will import all pre built functions

from tkinter import *
global result
proj=Tk()
v=IntVar()
x=IntVar()
proj.title("CONVERSION SYSTEM")
proj.geometry("500x500")
proj.configure(bg="lightblue")
def Dconvert(binary): 
	binary1 = binary 
	decimal, i, n = 0, 0, 0
	while(binary != 0): 
		dec = binary % 10
		decimal = decimal + dec * pow(2, i) 
		binary = binary//10
		i += 1
	return decimal

def Octconvert(octal):
        octal1 = octal
        decimal = 0 
        base = 1
        temp = octal1
        while (temp):
                last_digit = temp % 10
                temp = int(temp / 10)
                decimal += last_digit * base
                base = base * 8
        return decimal

def Hexconvert(hexdec):
        decimal = int(hexdec, 16)
        return decimal

    

def dtob():
    fr=v.get() 
    to=x.get()
    num=enum.get()
    if fr != 4:
            num_1 = int(num)
        

    if len(num)==0:
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="ENTER THE NUMBER",font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==to:
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="FROM AND TO SHOULD NOT BE SAME",font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)


# from here it is binary to other types of conversions        

    elif fr==1 and to==2:
        num_1=Dconvert(num_1)
        num_1=oct(num_1).replace("0o","")
        num_1 = str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==1 and to==3:
        num_1=Dconvert(num_1)
        num_1 = str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==1 and to==4:
        num_1=Dconvert(num_1)
        num_1=hex(num_1).replace("0x","")
        num_1=str(num_1).upper()
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)


# from here it is octal to other types of conversions

    elif fr==2 and to==1:
        num_1 = int(num)
        num_1=Octconvert(num_1)
        num_1=bin(num_1).replace("0b","")
        num_1 = str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==2 and to==3:
        num_1=Octconvert(num_1)
        num_1 = str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==2 and to==4:
        num_1=Octconvert(num_1)
        num_1=hex(num_1).replace("0x","")
        num_1=str(num_1).upper()
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)


# from here it is decimal to other types of conversions

    elif fr==3 and to==1:
        num_1=int(num)
        num_1=bin(num_1).replace("0b","")
        num_1=str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==3 and to==2:
        num_1=int(num)
        num_1=oct(num_1).replace("0o","")
        num_1=str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==3 and to==4:
        num_1=int(num)
        num_1=hex(num_1).replace("0x","")
        num_1=str(num_1).upper()
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")














        e_label.place(x=150,y=100)


# from here it is hexadecimal to other types of conversions

    elif fr==4 and to==1:
        num_1=Hexconvert(num)
        num_1=bin(num_1).replace("0b","")
        num_1 = str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==4 and to==2:
        num_1=Hexconvert(num)
        num_1=oct(num_1).replace("0o","")
        num_1 = str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    elif fr==4 and to==3:
        num_1=Hexconvert(num)
        num_1= str(num_1)
        frame= Frame(proj,height=200,width=500)
        frame.place(x=0,y=300)
        frame["bg"]="lightblue"
        e_label=Label(frame,text="Result :   "+ num_1,font=("MONOSPACE",10),fg="red",bg="lightblue")
        e_label.place(x=150,y=100)

    



# FOR LABELLING

label0=Label(proj,text="CONVERSION OF ONE SYSTEM TO ANOTHER SYSTEM",fg="red",bg="lightblue").place(x=90,y=10)
label1=Label(proj,text="Enter a Number",fg="green",bg="lightblue").place(x=50,y=50)
label2=Label(proj,text="Number to be Converted into",fg="green",bg="lightblue").place(x=250,y=50)

#FOR ENTRIES

enum=Entry(proj, width="10")
enum.place(x=150,y=50)

#FOR RADIO BUTTONS

radio1=Radiobutton(proj,text="Binary", value=1, variable=v, bg="lightblue").place(x=50,y=100)
radio2=Radiobutton(proj,text="Octal", value=2, variable=v, bg="lightblue").place(x=50,y=130)
radio3=Radiobutton(proj,text="Decimal", value=3, variable=v, bg="lightblue").place(x=50,y=160)
radio4=Radiobutton(proj,text="Hexadecimal", value=4, variable=v, bg="lightblue").place(x=50,y=190)

radio1=Radiobutton(proj,text="Binary", value=1, variable=x, bg="lightblue").place(x=250,y=100)
radio2=Radiobutton(proj,text="Octal", value=2, variable=x, bg="lightblue").place(x=250,y=130)
radio3=Radiobutton(proj,text="Decimal", value=3, variable=x, bg="lightblue").place(x=250,y=160)
radio4=Radiobutton(proj,text="Hexadecimal", value=4, variable=x, bg="lightblue").place(x=250,y=190)

#FOR BUTTON

button1=Button(proj,text="Result",width="20",fg="blue",command=dtob).place(x=120,y=250)

proj.mainloop()




