import tkinter as tk
from tkinter import *
import random
import os
from PIL import Image, ImageTk

win = tk.Tk()
win.configure(bg="light blue")
win.geometry("650x550")
win.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,20)
result.set("Guess a number between 1 to 20 ")
chances.set(5)
chances1.set(chances.get())

def fun():
  chances1.set(chances.get())
  if chances.get()>0:

    if choice.get() > 20 or choice.get()<0:
      result.set("You just lost 1 Chance")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    elif no==choice.get():
      result.set("Congratulation YOU WON!!!")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no > choice.get():
      result.set("Your guess was too low: Guess a higher number ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    elif no < choice.get():
      result.set(
          "Your guess was too High: Guess a lower number ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  else:
     result.set(
         "Game Over You Lost")
