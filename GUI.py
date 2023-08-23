import tkinter as tk
#from tkinter import tix
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter.font as tkFont
from PIL import ImageTk,Image
import PIL
from gtts import gTTS
import os
import texttospeech
import webbrowser
import convert
import Readrandom
import statistics
import TestLevel
import GameLevel
import KidsCourse

    
  
def Course(name):
    string = "welcome to tutor" + name
    global test
    global course
    global check
    test,course = 0,0
    check = statistics.CheckName(name)
    if check == False:
        statistics.Insert(name)
    else:
        check1 = statistics.GetValues(int(check))
        course,test = check1[0],check1[1]
    texttospeech.speaknow(string)
    master.destroy()
    window = tk.Tk()
    window.geometry("600x500")
    menu_frame = tk.Frame(window,bg = "#c3c3c3")
    window.title("Inflection booster")

    img = tk.PhotoImage(file = '\\users\\tejaswini\\Downloads\\project\\readingicon.png')
    window.iconphoto(False,img)

    
    menu_frame.pack(side = tk.LEFT)
    menu_frame.pack_propagate(False)
    menu_frame.configure(width = 120,height = 500)

    frame = tk.Frame(window)
    frame.pack(side = tk.LEFT)
    frame.pack_propagate(False)
    frame.configure(height = 500 ,width = 480)


    def improve():
        label = tk.Label(frame,text = 'Know the inflection of words',font = ("Times",20,'bold italic'))
        label.place(x = 20,y = 50)
        namelabel = tk.Label(frame,text = 'Enter letter or word ',font = ("Times",12,"italic"))
        namelabel.place(x = 50,y = 110)
        namevalue = tk.StringVar()
        name = tk.Entry(frame,textvariable = namevalue,width = 20,bd = 2,font =20)
        name.place(x = 200,y = 110)

        speakimage = tk.PhotoImage(file = 'C:/users/tejaswini/Downloads/project/speak.png')
        speak = tk.Button(frame,command =  lambda :texttospeech.speaknow(name.get()),image = speakimage)
        speak.image = speakimage
        speak.place(x = 250,y = 150)
        


    def Tutorial():

        ver_label = tk.Label(frame,text = "    Inflection Booster Courses",font = ("Times",20," bold italic"))
        ver_label.place(x = 0,y =  30)



        def kidsSlide():
            content = tk.Frame(frame)
            content.place(x = 0,y = 200)
            content.pack_propagate(False)
            content.configure(height = 400 ,width = 480)

            title = tk.Label(content,text = "Courses",font = ("Times",14," bold italic"))
            title.place(x = 150,y =  10)

            lesson_image = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/kidsAlphabet.jpg'))
            lesson_label = tk.Button(content,image = lesson_image,command = KidsCourse.KidWords)
            lesson_label.image = lesson_image
            lesson_label.place(x = 250,y =  60)

            lesson1_image = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/Alpabet.png'))
            lesson1_label = tk.Button(content,image = lesson1_image,command = KidsCourse.KidAlphabet)
            lesson1_label.image = lesson1_image
            lesson1_label.place(x = 50,y =  60)
            


        def studentsSlide():
            content1 = tk.Frame(frame)
            content1.place(x = 0,y = 200)
            content1.pack_propagate(False)
            content1.configure(height = 400 ,width = 480)
            title1 = tk.Label(content1,text = "Courses",font = ("Times",20," bold italic"))
            title1.place(x = 150,y =  10)

            def select():
                global course
                global check
                if click.get() == "Phonetics":
                    my_link1 = tk.Button(content1,text = " click here ",command = lambda :webbrowser.open_new("https://youtube.com/playlist?list=PL2IkMHFHWdEpVXEVB3PzzNIDBQt6SwziE"),font = ('Times',15,'bold italic'))
                    my_link1.place(x = 200,y = 200)
                    course += 1
                elif click.get() == "Basics":
                    my_link1 = tk.Button(content1,text = " click here ",command = lambda :webbrowser.open_new("https://youtu.be/EeToarNceeM"),font = ('Times',15,'bold italic'))
                    my_link1.place(x = 200,y = 200)
                    course += 1
                else:
                    my_link1 = tk.Button(content1,text = " click here ",command = lambda :webbrowser.open_new("https://youtu.be/8oJzRdqstkA"),font = ('Times',15,'bold italic'))
                    my_link1.place(x = 200,y = 200)
                    course += 1
                if(check == False):
                    check = statistics.CheckName(name)
                    statistics.UpdateCourseSheet(check,course)
                statistics.UpdateCourseSheet(check,course)
                
                    

            optionslist = ["Basics","Phonetics","Other Concepts"]
            click = tk.StringVar()
            click.set(options[0])

            optionslist_label = tk.Label(content1,text = "Choose topic",font = ("Times",15," italic"))
            optionslist_label.place(x = 20,y =  100)

            dropmenu = tk.OptionMenu(content1,click,*optionslist)
            dropmenu.place(x = 180,y = 100)

            submitButton = tk.Button(content1,text = " Submit",command = lambda :select(),font = ("Times",12," bold italic"))
            submitButton.place(x = 200,y = 150)

            

        def chooseSlide():
            content1 = tk.Frame(frame)
            content1.place(x = 0,y = 200)
            content1.pack_propagate(False)
            content1.configure(height = 400 ,width = 480)
            title1 = tk.Label(content1,text = "why are you waiting for....",font = ("Times",20," bold italic"))
            title1.place(x = 90,y =  40)
            title2 = tk.Label(content1,text = "Choose something",font = ("Times",20," bold italic"))
            title2.place(x = 130,y =  90)

        def selected():
            if clicked.get() == "kids":
                kidsSlide()
            elif clicked.get() == "students":
                studentsSlide()
            else:
                chooseSlide()
        
        options = ["choose","kids","students"]
        clicked = tk.StringVar()
        clicked.set(options[0])

        option_label = tk.Label(frame,text = "Choose category",font = ("Times",15," italic"))
        option_label.place(x = 20,y =  100)

        drop = tk.OptionMenu(frame,clicked,*options)
        drop.place(x = 180,y = 100)

        submitButton = tk.Button(frame,text = " Submit",command = lambda :selected(),font = ("Times",12," bold italic"))
        submitButton.place(x = 200,y = 150)


    def Test_page():
        global test
        global check
        def Increment(level):
            global test
            global check
            test += 1
            if(check == False):
                    check = statistics.CheckName(name)
                    statistics.UpdateTestSheet(check,test)
            statistics.UpdateTestSheet(check,test)
            level()
            

        lowimage = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/lowlevel.jpg'))
        low_label = tk.Button(frame,image = lowimage,command = lambda:Increment(TestLevel.GetStarted),height = 450,width = 150)
        low_label.image = lowimage
        low_label.place(x = 0,y =  50)

        normalimage = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/mediumlevel.jpg'))
        normal_label = tk.Button(frame,image = normalimage,command = lambda: Increment(TestLevel.GetStarted1),height = 450,width = 150)
        normal_label.image = normalimage
        normal_label.place(x = 160,y =  50)

        highimage = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/highlevel.jpg'))
        high_label = tk.Button(frame,image = highimage,command = lambda: Increment(TestLevel.GetStarted2),height = 450,width = 150)
        high_label.image = highimage
        high_label.place(x = 320,y =  50)


    def game():

        ballimage = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/Ball_Background.png'))
        ball = tk.Button(frame,image = ballimage,command =  None,height = 500,width = 150,text = "Bubbles",font = ("times",12,"bold italic"))
        ball.image = ballimage
        ball.place(x = 0,y = 0)


        circleimage = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/circle.png'))
        circle = tk.Button(frame,image = circleimage,command = None,height = 500,width = 150)
        circle.image = circleimage
        circle.place(x = 160,y =  0)

        cloudimage = ImageTk.PhotoImage(Image.open(r'C:/users/tejaswini/Downloads/project/cloud.png'))
        cloud = tk.Button(frame,image = cloudimage,command = None)
        cloud.image = cloudimage
        cloud.place(x = 300,y =  0)


    def Statistics():
        name_label = tk.Label(frame,text = "User     : ",font = ("Times",18," bold italic"))
        name_label.place(x = 20,y =  70)

        user_label = tk.Label(frame,text = name ,font = ("Times",18," italic"))
        user_label.place(x = 200,y =  70)

        course_label = tk.Label(frame,text = "Course :" ,font = ("Times",18," bold italic"))
        course_label.place(x = 20,y =  130)

        comple_label = tk.Label(frame,text = course ,font = ("Times",18," italic"))
        comple_label.place(x = 200,y =  130)

        test_label = tk.Label(frame,text = "Test     :" ,font = ("Times",18," bold italic"))
        test_label.place(x = 20,y =  200)

        test_label = tk.Label(frame,text = test ,font = ("Times",18,"  italic"))
        test_label.place(x = 200,y =  200)


    def information_page():


        def display():
            text = tk.Text(frame,height = 3,width = 40,bg= "#c3c3c3")
            text.place(x = 130,y = 200)
            text.insert(tk.END,information)

        information = "It helps to improve your inflection skills. There are related tutorial for improving skills. The courses menu helps you to know how the words are inflected."
        infor_label = tk.Label(frame,text = "Information",font = ("Times",18," bold italic"))
        infor_label.place(x = 100,y =  30)

        versi_label = tk.Label(frame,text = "version",font = ("Times",15," bold italic"))
        versi_label.place(x = 130,y =  60)

        ver_label = tk.Label(frame,text = "1.000",font = ("Times",15,"italic"))
        ver_label.place(x = 250,y =  60)

        lic_label = tk.Label(frame,text = "License",font = ("Times",15,"bold italic"))
        lic_label.place(x = 130,y =  90)

        license_label = tk.Label(frame,text = "No Yet Issued",font = ("Times",15,"italic"))
        license_label.place(x = 250,y =  90)

        copy_label = tk.Label(frame,text = "Copy Rights",font = ("Times",15,"bold italic"))
        copy_label.place(x = 130,y =  150)

        right_label = tk.Label(frame,text = "Sai Prasanna",font = ("Times",15,"italic"))
        right_label.place(x = 250,y =  150)

        moreinfor_label = tk.Button(frame,text = " More Information",command = lambda :display(),font = ("Times",15," bold italic"))
        moreinfor_label.place(x = 130,y =  200)
        

    def delete_pages():
        for frame1 in frame.winfo_children():
            frame1.destroy()

            
    def hidelabel():
        course_indicate.configure(bg = "#c3c3c3")
        tut_indicate.configure(bg = "#c3c3c3")
        test_indicate.configure(bg = "#c3c3c3")
        game_indicate.configure(bg = "#c3c3c3")
        statistics_indicate.configure(bg = "#c3c3c3")
        information_indicate.configure(bg = "#c3c3c3")


    def indicate(lb,page):
        hidelabel()
        lb.configure(bg = '#158aff')
        delete_pages()
        page()


    #tutorial button
    course_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "GetToKnow",command = lambda: indicate(course_indicate,improve),fg = "Black",bd = 0,bg = "#c3c3c3")
    course_button.place(x = 10,y = 50)

    course_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    course_indicate.place(x = 2,y = 50,width = 5,height = 40)


    
    #tutorial button
    tut_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Tutorial",command = lambda: indicate(tut_indicate,Tutorial),fg = "Black",bd = 0,bg = "#c3c3c3")
    tut_button.place(x = 10,y = 100)

    tut_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    tut_indicate.place(x = 2,y = 100,width = 5,height = 40)
    

    #test button
    test_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Inflection Test",command = lambda : indicate(test_indicate,Test_page),fg = "Black",bd = 0,bg = "#c3c3c3")
    test_button.place(x = 10,y = 150)

    test_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    test_indicate.place(x = 2,y = 150,width = 5,height = 40)


    #Games button
    game_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Games",command = lambda: indicate(game_indicate,game),fg = "Black",bd = 0,bg = "#c3c3c3")
    game_button.place(x = 10,y =200)

    game_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    game_indicate.place(x = 2,y = 200,width = 5,height = 40)


    #statistics button
    statistics_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Statistics",command = lambda:indicate(statistics_indicate,Statistics),fg = "Black",bd = 0,bg = "#c3c3c3")
    statistics_button.place(x = 10,y =250)

    statistics_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    statistics_indicate.place(x = 2,y = 250,width = 5,height = 40)


    #information button
    information_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Information",command = lambda: indicate(information_indicate,information_page),fg = "Black",bd = 0,bg = "#c3c3c3")
    information_button.place(x = 10,y = 300)

    information_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    information_indicate.place(x = 2,y = 300,width = 5,height = 40)
    

    
def OpenWindow():


    master.geometry("600x400")
    master.title("Inflection booster")

    frame1 = tk.Frame(master)
    frame1.grid(row = 0,column = 0,sticky = "nsew")
    frame1.place(x = 0,y = 0)
    frame1.configure(height = 100,width = 600)
    
    frame = tk.Frame(master)
    frame.grid(row = 1,column = 1,sticky = "nsew")
    frame.place(x = 125,y = 100)
    frame.pack_propagate(False)
    frame.configure(height = 400,width = 400)


    img = tk.PhotoImage(file = '\\users\\tejaswini\\Downloads\\project\\readingicon.png')
    master.iconphoto(False,img)

    img1 = tk.PhotoImage(file = 'C:/users/tejaswini/Downloads/project/homepage.png')
    imglabel = tk.Label(frame1)
    imglabel.config(image = img1)
    imglabel.image = img1
    imglabel.place(x= 150,y = 0)


    title = tk.Label(frame1,font = ("Times", "24", "bold italic"),text = "Inflection Booster")
    title.place(x = 250,y = 0)

    subtitle = tk.Label(frame1,font = ("Times", "12", "italic"),text = "Pronunication tutor")
    subtitle.place(x = 310,y = 35)

    
    #label
    label = tk.Label(frame,font = ("Times", "22", "italic"),text = "Welcome to Inflection Booster")
    label.place(x = 30,y = 50)

    namelabel = tk.Label(frame,text = 'Enter Your Name ',font = ("Times",12,"italic"))
    namelabel.place(x = 50,y = 110)
    namevalue = tk.StringVar()
    name = tk.Entry(frame,textvariable = namevalue,width = 20,bd = 2,font =20)
    name.place(x = 200,y = 110)

    button = tk.Button(frame,font = ("Times",10,"italic"),text = 'start',command = lambda :Course(name.get()),width = 15)
    button.place(x = 120,y = 160)



master = tk.Tk()
OpenWindow()

