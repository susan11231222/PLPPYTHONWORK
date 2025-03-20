my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#the below line eplaces the item in the second index
#my_list[1]=15
#we just want to insert not replace
my_list.insert(1,15)
#creates another list
my_list2=[50,60,70]
#extends the first list with the last list
my_list.extend(my_list2)
#method 1 to remove items from the list

#del my_list[0]
#method2 to remove items from the list
last_item=my_list.pop()
#sorting my list
my_list.sort()
#find item in index of a certain item 
position=my_list.index(30)
print(position)

print(my_list)

