import os
import subprocess
import random
os.system('tput setaf 5 | zenity --info title="welcome" --no-wrap --text="welcome to my menu"')

def story_xyz():
    print("hello reader")

    readername = input("what is your name?")

    print("hello" + readername)

    sentence_starter = ['once upon a time' , 'about a 100 years ago' , 'today at the   evening' , 'few days back', 'around 20BC ago']

    charecter = ['there lived a man named tatya vinchuk' , 'there lived a queen' , 'there lived a farmer' , 'there lived aking']

    time = ['at night' , 'at the morning' , 'around 6 pm' , 'one day' , 'at full moon']

    story_plot = ['he was passing by' , 'going on a date' , 'was attending a meeting' , ' was going for a picnic']

    place = [ 'to a hotel' , 'to the hills' , 'to a garden' , 'to a office']

    second_charecter = ['he saw a kid', 'he saw an old man passing by' , ' he saw his mother and her friend passing by']

    age = ['who seemed around 80' , 'who seemed in her 20s' , 'who was around 6-7 years old']

    work = ['cleaning the sewers' , 'digging a well on roadside' , ' playing football' , 'searching for something']

    print(random.choice(sentence_starter) + random.choice(charecter) + random.choice(time) +random.choice(story_plot) + random.choice(place) + random.choice(second_charecter) + random.choice(age) + random.choice(work))



def fibo_123():
    n = int(input("enter your number:"))
    a = 0
    b = 1
    c = 0
    while(c<=n):
     print(c)
    a = b
    b = c
    c = a+b



while True:
        x = subprocess.getstatusoutput('zenity --entry --title="enetr your choice" --text="enter 1 : to story_xyz()\nenter 2 : to fibo_123()\nenter 3 : to exit" 2>/dev/null')
        x1 = int(x[1])
        ch = x1
        if int(ch) ==1:
                 os.system('zenity --info --no-wrap --text="$(story)" --title=story')
        elif int(ch) ==2:
                 os.system('zenity --info --no-wrap --text="$(Fibonacci series)" --title=Fibonacci series')
        elif int(ch) ==3:
                  exit()
        else:
                 prnit("not supported")
               
        input("enter to cont...")
        os.system("clear")
