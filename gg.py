pp_maze = []

pp_size = int(input("enter size of pp_maze: "))

def checker(arr,maze,posi, posj,w,a,s,d):

    
    if posi>=len(maze) or posi<0 or posj >= len(maze) or posj < 0:
        arr.pop(-1)
        return
    
    if posi==posj==len(maze)-1:
        print("gg bitch" , arr)
        exit(1)
    
    if maze[posi][posj] == 1 :
        arr.pop(-1)
        return
    if w==1:
        arr.append((posi-1 , posj))
        checker(arr,maze,posi-1 , posj,1,0,0,0)
        arr.append((posi , posj-1))
        checker(arr,maze,posi, posj-1,0,1,0,0)
        arr.append((posi , posj+1))
        checker(arr,maze,posi, posj+1,0,0,0,1)
    elif a==1:
        arr.append((posi-1 , posj))
        checker(arr,maze,posi-1 , posj,1,0,0,0)
        arr.append((posi , posj-1))
        checker(arr,maze,posi, posj-1,0,1,0,0)
        arr.append((posi+1 , posj))
        checker(arr,maze,posi+1, posj,0,0,1,0)
    elif s==1:
        arr.append((posi , posj-1))
        checker(arr,maze,posi, posj-1,0,1,0,0)
        arr.append((posi+1 , posj))
        checker(arr,maze,posi+1, posj,0,0,1,0)
        arr.append((posi , posj+1))
        checker(arr,maze,posi, posj+1,0,0,0,1)
    elif d==1:
        arr.append((posi-1 , posj))
        checker(arr,maze,posi-1 , posj,1,0,0,0)
        arr.append((posi+1 , posj))
        checker(arr,maze,posi+1, posj,0,0,1,0)
        arr.append((posi , posj+1))
        checker(arr,maze,posi, posj+1,0,0,0,1)
    else:
        arr.append((posi-1 , posj))
        checker(arr,maze,posi-1 , posj,1,0,0,0)
        arr.append((posi , posj-1))
        checker(arr,maze,posi, posj-1,0,1,0,0)
        arr.append((posi+1 , posj))
        checker(arr,maze,posi+1, posj,0,0,1,0)
        arr.append((posi , posj+1))
        checker(arr,maze,posi, posj+1,0,0,0,1)
    
    

def main():
    for i in range(pp_size):
        temp_pp = []
        for j in range(pp_size):
            t = int(input("pp_block: "))
            temp_pp.append(t)
        pp_maze.append(temp_pp)
    
    k = [[0 , 1 , 1 , 1] , 
 [ 0 , 0 , 0 , 1] , 
 [ 1 , 1 , 0 , 1],
 [1 , 1 , 0 , 0 ] ]


    # checker(pp_maze , 0 , 0,0,0,0,0)
    checker([(0,0)] , k , 0 , 0,0,0,0,0)
    


if __name__ == "__main__":
    main()