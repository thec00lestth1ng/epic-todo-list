import json
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
inadd = []
try:
 with open("datalist", "r") as f:
  inadd = json.load(f)
except:
 pass
def add():
   inadd.append(addwhat)
   with open("datalist", "w") as f:
    json.dump(inadd, f) 
def remove():
   global whatremove
   inadd.pop(whatremove)
   with open("datalist", "w") as f:
    json.dump(inadd, f)
def change():
   inadd[numchange] = whatchange
   with open("datalist", "w") as f:
    json.dump(inadd, f)
def quit():
 exit()
def open_todo_list():
 global whatremove
 global numchange
 global whatchange
 global addwhat
 whatremove = 0 
 numchange = 0
 while True:
  try:
   clear_screen()
   print("--- YOUR TASKS ---")
   for index, task in enumerate(inadd):
    print(f"{index}: {task}")
   print("------------------")
  except:
   pass
  removewhile = 0
  global addwhat
  print("hello there")
  print("welcome to the todo_list")
  print("what do you want do to (type by number):")
  print("1: add")
  print("2: remove")
  print("3: change")
  print("4: quit")
  chose = input(":")
  if chose.isdigit() == True:
   chose = int(chose)
   if chose == 1:
    addwhat = input("what do you want to add:")
    add()
   elif chose == 2:
    while removewhile == 0:
     whatremove = input("which one (type by number):")
     if whatremove.isdigit() == True:
      if int(whatremove) >= len(inadd):
       print("number higher than expected, try again")
      else:
       whatremove = int(whatremove)
       remove()
       removewhile = 1
     else:
      print("try again")
   elif chose == 3:
    numchange = input("what do you want to change (type by number):")
    if numchange.isdigit() == True:
     numchange = int(numchange)
     if int(numchange) >= len(inadd):
      print("number higher than expected, try again")
     else:
      whatchange = input("what do you what to change it to?:")
      change()
    else:
     print("not a number try again")
   elif chose == 4:
    print("bye bye :)")
    quit()
   else:
    print("number higher than expected")
  else:
   print("not a number try again") 
open_todo_list()
