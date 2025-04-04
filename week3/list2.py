def print_list(elements):
    for i in range(limit):
        print (elements)
        
        
        
    
elements=[]
limit=int(input("enter the length of the list"))
for i in range(limit):
    temp=int(input(f"enter the number{i+1}:"))
    elements.append(temp)
print_list(elements)
