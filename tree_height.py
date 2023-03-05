# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    
    x=np.array(parents)
    
    max_height = 0
    max_height_check=0
    node_mh={}
    # Your code here
    j=0
  
    for i in range(n):
        j=i
        while True:
            if x[i]==-1:
                #max_height=0
                j=i
                break
            else:
                max_height+=1
                #node_mh[x[i]]=max_height
                #j=i
                i=x[i]
                #node_mh[x[i]]=max_height
                if i in node_mh.keys():
                    #update
                    
                    max_height=max_height+node_mh.get(i)
                    node_mh[j]=max_height
                    j=i
                    break
                else:
                    node_mh[j]=max_height

                 #pievienot x[i] ka key un max height ka value un pec tam jataisa if parbaude un japieskaita max height ja pie sada elementa jau ir bijis
                #j=i
                #i=x[i]
                
                
        if max_height_check<max_height:
            max_height_check=max_height
        max_height=0

        
    

    return max_height_check+1


def main():
    # implement input form keyboard and from files
    text=input()
    if "I"in text:
        n=input()
        parents=input().split(" ")
        parents=map(int,parents)
        parents=list(parents)
        print(compute_height(int(n),parents))
    elif "F"in text:
        
        faila_nosaukums=input()
        if "a" in faila_nosaukums:
            print("error")
            
        else:
            
            fails=open("./test/"+faila_nosaukums)
            n=fails.readline()
            n=int(n)
            parents=fails.readline()
            parents=parents.split(" ")
            parents=map(int,parents)
            parents=list(parents)
            print(compute_height(n,parents))
            fails.close()


            

        pass
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
