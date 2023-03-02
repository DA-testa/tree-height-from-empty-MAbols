# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    
    x=parents
    for i in range(len(x)):
        x[i]=int(x[i])
    print(x)
    max_height = 0
    # Your code here
    root_num=0
    for i in range(len(x)):
        if x[i]==-1:
            root_num=i
            break
    for i in range(n):
        for j in range(n):
            if i==root_num:
                break
            else:
                max_height+=1
                i=x[i]
                continue

        
    print(max_height)

    return max_height


def main():
    # implement input form keyboard and from files
    text=input()
    if "I"in text:
        n=input()
        parents=input().split(" ")
        parents=map(int,parents)
        parents=list(parents)
        compute_height(int(n),parents)
    elif "F"in text:
        path_sakums=".github/test/"
        faila_nosaukums=input()
        if "a" or"A" in faila_nosaukums:
            print("error")
            
        else:
            pilnais_path=path_sakums+faila_nosaukums
            fails=open(pilnais_path)
            n=fails.readline()
            n=int(n)
            parents=fails.readline()
            parents=parents.split(" ")
            parents=map(int,parents)
            parents=list(parents)
            compute_height(n,parents)
            fails.close()


            

        
    
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
