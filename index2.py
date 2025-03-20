#This is alist that promotes user to enter the numbers and then sum up them
numbers=list(map(int,input("enter values sepated by comma:").split(',')))#int(input("enter values sepated by comma:").split())
print(numbers)
total=sum(numbers)
print(total)
#this tuple stores a list of my favourite books and then i use for loop to print each of them 
Book_names=("The lean startup","Deep learning","Atomic Habits","The power of now","The Alchemist")
for i in Book_names:
    print(i)
#collecting information from the user then storing it in a dictionary
Details={}
#NB:You collect use inputs while you are inside the dictionary and then store them in the dictionary
Details["name"]=input("enter your name:")
Details["age"]=input("enter your age:")
Details["favourite_food"]=input("enter your favourite-food:")
print(Details)
#####a set that accept user input 
age1=set(map(int,input("enter values separated by comma:").split(",")))
print(age1)
age2=set(map(int,input("enter values separated by comma:").split(",")))
print(age2)
#prints what is common in two sets 
common_ages=age1.intersection(age2)
print(common_ages)
#******A list that stores words
Words=list(input("enter words separated by comma:").split(","))
print(Words)
odd_count=sum(1 for word in Words if len(word)%2==1)
print(odd_count)