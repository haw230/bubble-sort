def solved_bubble_sort(ls):
    sort_done = False #Assume False so the while look will run
    while (not sort_done): #While it's not done
        sort_done = True #Assume list is sorted
        for i in range(len(ls) - 1): 
            if (ls[i] > ls[i + 1]): #If current index is greater than next
                swap(ls, i) #swap the two
                sort_done = False #List isn't sorted
    return ls
    
def swap(ls, i):
    temp = ls[i] #set ls[i] to temporary variable
    ls[i] = ls[i + 1] #set ls[i] to ls[i + 1] (ls[i] is only available through temp now)
    ls[i + 1] = temp #set ls[i + 1] to temp (temp stores the original ls[i])