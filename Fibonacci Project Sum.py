# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:37:27 2023

@author: Acer
"""
from tkinter import*

root=Tk()
root.title("Fibonacci Sum")
root.geometry("400x400")

enter_number = Entry(root)

label_series = Label(root,text = "Fibonacci Series:  ")
label_sum = Label(root,text = "Fibonacci Sum:  ")

def Fibonacci():
    input_number = int(enter_number.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    
while(counter <= input_number):
    
    label_series["text"] +=str(sum)+","
    label_sum["text"] ="Fibonacci Sum"+str(sum2)
    counter = counter + 1
    first_no = second_no
    second_no = sum
    sum = first_no + second_no
    sum2 = sum2 + sum
    
    button_sum = Button(root,text = "Show Fibonacci Series", command = Fibonacci)
    
    button_sum.pack()
    label_series.pack()
    label_sum.pack()
    enter_number.pack()
    
    root.mainloop()