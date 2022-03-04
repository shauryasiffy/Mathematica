# the problem is to find that will the array have a pattern, 
# pattern being list to be divide into 2 sub lists, 1st strictly decreasing 
# and 2nd strictly increasing

get_elements=input("Enter the numbers -->\n").split()
arrae=[]
for element in get_elements:
    element=int(element)
    arrae.append(element)

def wireframe(array):
    if array[0]>array[1]:    
        set_array=set(array)
        a=[y for x, y in enumerate(array)
                if ((x == 0) or (array[x - 1] >= y))
                and ((x == len(array) - 1) or (y < array[x+1]))]        
        if len(a)==1:
            print("TRUE")
        else:
            print("FALSE1")
    else:
        print("FALSE3")

print(wireframe(arrae))