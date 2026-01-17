'''1. Print the highest and lowest marks. 
2. Print the average marks. 
3. Print all marks above 75 (distinction). 
4. Add a new mark 95 to the list. 
5. Remove a mark 55 from the list. 
6. Sorting of the marks 
'''



marks = [78, 10,74,85, 62, 90, 55, 88,50] 

High_Mark = max(marks)
print("Highest mark is",High_Mark)

Low_mark = min(marks)
print("Minimum mark is",Low_mark)
avg_mark = sum(marks)/len(marks)
print("Average mark is",avg_mark)


new_List=[x for x in marks if x >= 75]
print("List only with distiction",new_List)
marks.append(95)
print("New marks list" , marks)

marks.pop(4)
print("New marks list after deleting" , marks)

marks.sort
print(marks)


