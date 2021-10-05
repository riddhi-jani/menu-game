import os
import subprocess
import random
os.system('tput setaf 5 | zenity --info title="welcome" --no-wrap --text="welcome to my menu"')

def story_xyz():

    #readername = input("what is your name?")
    readername=subprocess.getoutput('zenity --entry --text="enter your name" 2>/dev/null')

    #print("hello" + readername)

    sentence_starter = ['Once upon a time' , 'About a 100 years ago' , 'Today at the evening' , 'Few days back', 'Around 20BC ago']

    charecter = ['there lived a man named tatya vinchuk' , 'there lived a queen' , 'there lived a farmer' , 'there lived a king']

    time = ['At night' , 'At the morning' , 'Around 6 pm' , 'One day' , 'At full moon']

    story_plot = ['he was passing by' , 'he was going on a date' , 'he was attending a meeting' , 'he was going for a picnic']

    place = [ 'to a hotel.' , 'to the hills.' , 'to a garden.' , 'to a office.']

    second_charecter = ['he saw a kid', 'he saw an old man passing by' , ' he saw his mother and her friend passing by']

    age = ['who seemed around 80' , 'who seemed in her 20s' , 'who was around 6-7 years old']

    work = ['cleaning the sewers' , 'digging a well on roadside' , ' playing football' , 'searching for something']
	
    os.system('zenity --info --title="story" --text="hello {}"'.format(readername))
    os.system('zenity --info --title="story" --ok-label="continue" --no-wrap --text=" {} {} "'.format(random.choice(sentence_starter) ,random.choice(charecter)  ))
    os.system('zenity --info --title="story" --no-wrap  --ok-label="finish" --text=" {} {} {} \n{} {} {}"'.format(random.choice(time), random.choice(story_plot) , random.choice(place) , random.choice(second_charecter) , random.choice(age) , random.choice(work)))



def fib():
	x=subprocess.getstatusoutput('zenity --entry --text="enter number" 2>/dev/null')
	n=int(x[1])
	print(n)
	seq=[0,1]
	for i in range(2,n+1):
		next_num = seq[i-1] +seq[i-2]
		seq.append(next_num)
	return seq
	



while True:
	x = subprocess.getstatusoutput('zenity --entry --title="enetr your choice" --text="enter 1 : to story_xyz()\nenter 2 : to fibo_123()\nenter 3 : to exit" 2>/dev/null')
	x1 = int(x[1])
	ch = x1
	if  ch ==1:
		os.system('zenity --info --no-wrap --text={} --title="story" 2>dev/null'.format(story_xyz()))
	elif ch ==2:
		
		os.system('zenity --info --no-wrap --text={} --title="Fibonacci series"  2>/dev/null'.format(fib()))
	elif ch==3:
		exit()
	else:
		print("not supported")
               
	input("enter to cont...")
	os.system("clear")
