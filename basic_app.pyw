from tkinter import *
root = Tk()
root.title("INFIX TO PREFIX AND POSTFIX CALCULATOR")
root.geometry("770x300+100+100")
root.configure(bg="lightblue")
photo=PhotoImage(file="C:\\Users\\BARNEEL RAY\\Desktop\\python practise\\desktop apps\\DSA_Logo.png")
root.iconphoto(False,photo)
input_view=Entry(root,width=40,borderwidth=7)
#input_view.pack()
input_view.grid(row=0,column=1,padx=3,pady=2)
Operators = set(['+', '-', '*', '/', '(', ')', '^']) 
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
def button_click(a):
    input_view.get()
    input_view.insert(END, str(a))

def clear_text():
    input_view.delete(0,END)
def prefix(expression):
    expression="".join(reversed(str(expression)))
    stack=[]
    output=""
    i=0
    while i in range(0,len(expression)):
        if expression[i].isalpha():
            output+=expression[i]
        elif expression[i]==")" or expression[i]=="}" or expression[i]=="]":
            stack.append(expression[i])
        elif expression [i]=="(" or expression[i]=="[" or expression[i]=="{":
            if expression[i] == '(':
                while stack[-1] != ')':
                    output += stack.pop()
                stack.pop()
            if expression[i] == '[':
                while stack[-1] != ']':
                   output += stack.pop()
                stack.pop()
 
            if expression[i] == '{':
                while stack[-1] != '}':
                    output += stack.pop()
                stack.pop()
        else:
            if len(stack)==0:
                stack.append(expression[i])
            else:
                if Priority[expression[i]]>=Priority[stack[-1]]:
                    stack.extend(expression[i])
                elif Priority[expression[i]] < Priority[stack[-1]]:
                    output += stack.pop()
                    position = len(stack) - 1
                    while position >= 0 and Priority[stack[position]] >Priority[expression[i]]:
                        output += stack.pop()
                        position -= 1
                        if position < 0:
                            break
 
                    stack.extend(expression[i])
 
        # increment the value of i
        i += 1
    while len(stack) != 0:
        output += stack.pop()
       
    # reverse the string before output 
    # return the result
    input_view.delete(0,END)
    input_view.insert(END,output[::-1])
def postfix(expression):
    stack = [] 
    output = '' 
    for character in expression:
        if character not in Operators: 
            output+= character
        elif character=='(':
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    
    input_view.delete(0,END)
    input_view.insert(END, output)
def backspace():
    input_view.delete(input_view.index("end") - 1)
output_button0=Button(root,text="a",command=lambda:button_click("a"),padx=100,pady=10,bg="pink",activebackground="yellow",fg="white",activeforeground="blue")
output_button1=Button(root,text="b",command=lambda:button_click("b"),padx=100,pady=10,bg="pink",activebackground="yellow",fg="white",activeforeground="blue")
output_button2=Button(root,text="c",command=lambda:button_click("c"),padx=100,pady=10,bg="pink",activebackground="yellow",fg="white",activeforeground="blue")
output_button3=Button(root,text="d",command=lambda:button_click("d"),padx=100,pady=10,bg="pink",activebackground="yellow",fg="white",activeforeground="blue")
output_button4=Button(root,text="e",command=lambda:button_click("e"),padx=100,pady=10,bg="pink",activebackground="yellow",fg="white",activeforeground="blue")
output_button5=Button(root,text="+",command=lambda:button_click("+"),padx=100,pady=10,bg="red",activebackground="yellow",fg="white",activeforeground="blue")
output_button6=Button(root,text="-",command=lambda:button_click("-"),padx=100,pady=10,bg="red",activebackground="yellow",fg="white",activeforeground="blue")
output_button7=Button(root,text="x",command=lambda:button_click("*"),padx=100,pady=10,bg="red",activebackground="yellow",fg="white",activeforeground="blue")
output_button8=Button(root,text="^",command=lambda:button_click("^"),padx=100,pady=10,bg="red",activebackground="yellow",fg="white",activeforeground="blue")
output_button9=Button(root,text="/",command=lambda:button_click("/"),padx=100,pady=10,bg="red",activebackground="yellow",fg="white",activeforeground="blue")
output_button10=Button(root,text="clear",command=clear_text,padx=100,pady=10,bg="pink",activebackground="yellow",fg="white",activeforeground="blue")
output_button11=Button(root,text="prefix",command=lambda:prefix(input_view.get()),padx=100,pady=10,bg="orange",activebackground="blue",fg="black",activeforeground="yellow")
output_button12=Button(root,text="postfix",command=lambda:postfix(input_view.get()),padx=100,pady=10,bg="orange",activebackground="blue",fg="black",activeforeground="yellow")
output_button13=Button(root,text="del",command=backspace,padx=100,pady=10,bg="orange",activebackground="blue",fg="black",activeforeground="yellow")
output_button0.grid(row=1,column=0)
output_button1.grid(row=1,column=1)
output_button2.grid(row=1,column=2)
output_button3.grid(row=2,column=0)
output_button4.grid(row=2,column=1)
output_button5.grid(row=2,column=2)
output_button6.grid(row=3,column=0)
output_button7.grid(row=3,column=1)
output_button8.grid(row=3,column=2)
output_button9.grid(row=4,column=0)
output_button10.grid(row=5,column=1)
output_button11.grid(row=6,column=0)
output_button13.grid(row=6,column=1)
output_button12.grid(row=6,column=2)
root.mainloop()