from tkinter import *
import tkinter as tk

n=0
gui3=Tk()
#gui=Tk()
gui2=0
def menu():
    #global gui3
    gui3.destroy()
    #gui2.destroy()
    gui=Tk()
    gui.configure(background="light green")
    gui.title("IP PROJECT")
    gui.geometry("250x230")
    T=Text(gui,height=5,width=52)
    l=Label(gui,text="FROG JUMP")
    l.config(font=("Courier",14))
    Fact="let's jump and roll"


    #tk.mainloop()

    ##button1=Button(gui, text='PLAY', fg='black', bg='red',
    ##                                       command=game(gui),height=1, width=7)
    ##button1.grid(row=2, column=0)
    def instructvia1():
        gui.destroy()
        global gui3
        gui3=Tk()
        gui3.configure(background="light green")
        gui3.title("IP PROJECT")
        gui3.geometry("350x300")
        a='''1.The frog(shaped as turtle) will already be jumping and cars will be moving
2.Press Up arrow to leap(you can jump over the cars)
3.You have to go till the end to secure 100 points'''
        T3=Text(gui3,height=10,width=75)
        l3=Label(gui3,text="FROG JUMP")
        l3.config(font=("Courier",14))
        Fact3=a
        button5=Button(gui3, text='BACK', fg='black', bg='red',command=menu)
        #button5.grid(row=7, column=1)
        l3.pack()
        T3.pack()
        button5.pack()
        T3.insert(tk.END,Fact3)
        tk.mainloop()
        
    def instructvia2():
        global gui2
        gui2.destroy()
        global gui3
        gui3=Tk()
        gui3.configure(background="light green")
        gui3.title("IP PROJECT")
        gui3.geometry("350x300")
        a='''1.The frog(shaped as turtle) will already be jumping and cars will be moving
2.Press Up arrow to leap(you can jump over the cars)
3.You have to go till the end to secure 100 points'''
        T3=Text(gui3,height=10,width=75)
        l3=Label(gui3,text="FROG JUMP")
        l3.config(font=("Courier",14))
        Fact3=a
        button5=Button(gui3, text='BACK', fg='black', bg='red',command=menu)
        #button5.grid(row=7, column=1)
        l3.pack()
        T3.pack()
        button5.pack()
        T3.insert(tk.END,Fact3)
        tk.mainloop()
              
    def exit1():
        gui.destroy()

    def nogame():
        game(gui)

    def game(t):
        import turtle
        from turtle import TurtleScreen 
        TurtleScreen._RUNNING=True
        t.destroy()
        turtle.bgcolor("yellow")

        wn=turtle.Screen()
        wn.setup(width=700,height=700)


        ball=turtle.Turtle()
        ball.seth(90)
        ball.pu()
        ball.setpos(x=0,y=-305)
        ball.pensize(4)
        ball.speed(0)
        ball.shape("turtle")

        l=turtle.Turtle()
        l.pu()
        l.speed(0)
        l.setpos(x=305,y=0)
        l.seth(90)
        l.pd()
        l.fd(305)
        l.lt(90)
        l.fd(610)
        l.lt(90)
        l.fd(610)
        l.lt(90)
        l.fd(610)
        l.lt(90)
        l.fd(305)
        l.hideturtle()


        p1=turtle.Turtle()
        p1.pu()
        p1.speed(0)
        p1.setpos(x=305,y=60)
        p1.seth(180)
        p1c=turtle.Turtle()
        p1c.pu()
        p1c.speed(0)
        p1c.setpos(x=-305,y=60)
        #p1c.seth(180)
        p2=turtle.Turtle()
        p2.pu()
        p2.speed(0)
        p2.setpos(x=305,y=120)
        p2.seth(180)
        p2c=turtle.Turtle()
        p2c.pu()
        p2c.speed(0)
        p2c.setpos(x=150,y=120)
        p2c.seth(180)
        p3=turtle.Turtle()
        p3.pu()
        p3.speed(0)
        p3.setpos(x=-305,y=180)
        p4=turtle.Turtle()
        p4.pu()
        p4.speed(0)
        p4.setpos(x=305,y=240)
        p4.seth(180)
        p4c=turtle.Turtle()
        p4c.pu()
        p4c.speed(0)
        p4c.setpos(x=270,y=240)
        p4c.seth(180)
        p5=turtle.Turtle()
        p5.pu()
        p5.speed(0)
        p5.setpos(x=-305,y=300)
        p6=turtle.Turtle()
        p6.pu()
        p6.speed(0)
        p6.setpos(x=-305,y=-60)
        p6c=turtle.Turtle()
        p6c.pu()
        p6c.speed(0)
        p6c.setpos(x=-305,y=-60)
        p7=turtle.Turtle()
        p7.pu()
        p7.speed(0)
        p7.setpos(x=-305,y=-120)
        p8=turtle.Turtle()
        p8.pu()
        p8.speed(0)
        p8.setpos(x=305,y=-180)
        p8.seth(180)
        p8c=turtle.Turtle()
        p8c.pu()
        p8c.speed(0)
        p8c.setpos(x=-305,y=-180)
        p9=turtle.Turtle()
        p9.pu()
        p9.speed(0)
        p9.setpos(x=-305,y=-240)
        p9c=turtle.Turtle()
        p9c.pu()
        p9c.speed(0)
        p9c.setpos(x=-260,y=-240)
        p10=turtle.Turtle()
        p10.pu()
        p10.speed(0)
        p10.setpos(x=305,y=-300)
        p10.seth(180)


        def move():
            ball.forward(40)
        while 1<2:
            global n
            ball.forward(13)
            p1.fd(10)
            p1c.fd(13)
            p2.fd(12)
            p2c.fd(12)
            p3.fd(9)
            p4.fd(17)
            p4c.fd(17)
            p5.fd(21)
            p6.fd(25)
            p6c.fd(20)
            p7.fd(26)
            p8.fd(19)
            p8c.fd(23)
            p9.fd(15)
            p9c.fd(15)
            p10.fd(17)
            y=round(ball.ycor())

            if round(ball.ycor())>=305:
                n=n+1
                ball.hideturtle()
                ball.goto(0,-305)
                ball.showturtle()
            elif round(p1.xcor())<=-305:
                p1.hideturtle()
                p1.goto(305,60)
                p1.showturtle()
            elif round(p1c.xcor())>=305:
                p1c.hideturtle()
                p1c.goto(-305,60)
                p1c.showturtle()
            elif round(p2.xcor())<=-305:
                p2.hideturtle()
                p2.goto(305,120)
                p2.showturtle()
            elif round(p2c.xcor())<=-305:
                p2c.hideturtle()
                p2c.goto(150,120)
                p2c.showturtle()
            elif round(p3.xcor())>=305:
                p3.hideturtle()
                p3.goto(-305,180)
                p3.showturtle()
            elif round(p4.xcor())<=-305:
                p4.hideturtle()
                p4.goto(305,240)
                p4.showturtle()
            elif round(p4c.xcor())<=-305:
                p4c.hideturtle()
                p4c.goto(270,240)
                p4c.showturtle()
            elif round(p5.xcor())>=305:
                p5.hideturtle()
                p5.goto(-305,300)
                p5.showturtle()
            elif round(p6.xcor())>=305:
                p6.hideturtle()
                p6.goto(-305,-60)
                p6.showturtle()
            elif round(p6c.xcor())>=305:
                p6c.hideturtle()
                p6c.goto(-305,-60)
                p6c.showturtle()
            elif round(p7.xcor())>=305:
                p7.hideturtle()
                p7.goto(-305,-120)
                p7.showturtle()
            elif round(p8.xcor())<=-305:
                p8.hideturtle()
                p8.goto(305,-180)
                p8.showturtle()
            elif round(p8c.xcor())>=305:
                p8c.hideturtle()
                p8c.goto(-305,-180)
                p8c.showturtle()
            elif round(p9.xcor())>=305:
                p9.hideturtle()
                p9.goto(-305,-240)
                p9.showturtle()
            elif round(p9c.xcor())>=305:
                p9c.hideturtle()
                p9c.goto(-260,-240)
                p9c.showturtle()
            elif round(p10.xcor())<=-305:
                p10.hideturtle()
                p10.goto(305,-300)
                p10.showturtle()
            elif -15<p1.xcor()<15 and y-15<p1.ycor()<y+15:
                break
            elif -15<p1c.xcor()<15 and y-15<p1c.ycor()<y+15:
                break
            elif -15<p2.xcor()<15 and y-15<p2.ycor()<y+15:
                break
            elif -15<p2c.xcor()<15 and y-15<p2c.ycor()<y+15:
                break
            elif -15<p3.xcor()<15 and y-15<p3.ycor()<y+15:
                break
            elif -15<p4.xcor()<15 and y-15<p4.ycor()<y+15:
                break
            elif -15<p4c.xcor()<15 and y-15<p4c.ycor()<y+15:
                break
            elif -15<p5.xcor()<15 and y-15<p5.ycor()<y+15:
                break
            elif -15<p6.xcor()<15 and y-15<p6.ycor()<y+15:
                break
            elif -15<p6c.xcor()<15 and y-15<p6c.ycor()<y+15:
                break
            elif -15<p7.xcor()<15 and y-15<p7.ycor()<y+15:
                break
            elif -15<p8.xcor()<15 and y-15<p8.ycor()<y+15:
                break
            elif -15<p8c.xcor()<15 and y-15<p8c.ycor()<y+15:
                break
            elif -15<p9.xcor()<15 and y-15<p9.ycor()<y+15:
                break
            elif -15<p9c.xcor()<15 and y-15<p9c.ycor()<y+15:
                break
            elif -15<p10.xcor()<15 and y-15<p10.ycor()<y+15:
                break
            
            turtle.listen()
            turtle.onkey(move,"Up")
        wn.bye()
        def nogame2():
            global n
            n=0
            game(gui2)
        def exit2():
            gui2.destroy()
        global gui2  
        gui2=Tk()
        gui2.configure(background="light green") 
        gui2.title("IP PROJECT")
        gui2.geometry("250x200")
        T2=Text(gui2,height=5,width=52)
        l2=Label(gui2,text="FROG JUMP")
        l2.config(font=("Courier",14))
        Fact2=" score:"+str(n*100)+'''
                                         let's roll again'''

        button2=Button(gui2, text='PLAY AGAIN', fg='black', bg='red',
                                           command=nogame2)#height=1, width=7)
        #button2.grid(row=2, column=0)

        button3=Button(gui2, text='EXIT', fg='black', bg='red',
                                           command=exit2)#height=1, width=7)
        #button3.grid(row=2, column=1)
        button6=Button(gui2, text='INSTRUCTIONS', fg='black', bg='red',command=instructvia2)
        l2.pack()
        T2.pack()
        button2.pack()
        button3.pack()
        button6.pack()
        T2.insert(tk.END,Fact2)
        tk.mainloop()
        

    button1=Button(gui, text='PLAY', fg='black', bg='red',
                                           command=nogame)#height=1, width=7)
    ##button1.grid(row=7, column=0)

    button4=Button(gui, text='INSTRUCTIONS', fg='black', bg='red',
                                           command=instructvia1)#height=1, width=7)
    button5=Button(gui, text='EXIT', fg='black', bg='red',
                                           command=exit1)#height=1, width=7)
    ##button4.grid(row=7, column=1)
    l.pack()
    T.pack()
    button1.pack()
    button4.pack()
    button5.pack()
    T.insert(tk.END,Fact)
    tk.mainloop()
menu()






























































































