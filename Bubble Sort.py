def bubble_sort(list):
    sorted = 0
    #loop until all list value checked
    for i in range(len(list) - 1):
        for i in range(len(list) - 1 - sorted):
            print(i)
            if list[i] > list[i + 1]:

                #swap
                list[i], list[i + 1] = list[i + 1], list[i]
                print(list)
        sorted += 1



a = [5,1,2,6,0,3,8,3] #change this list to see other number sorting well
bubble_sort(a)
