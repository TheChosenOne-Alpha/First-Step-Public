def bubble_sort(list):

    #loop until all list value checked
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                sorted = False

        if sorted == False:
            for i in range(len(list) - 1):
                print(i)
                if list[i] > list[i + 1]:

                    #swap
                    list[i], list[i + 1] = list[i + 1], list[i]
                    print(list)
    
    print("Final:", list)
    return list



a = [5,1,2,6,0,3] #change this list to see other number sorting well
bubble_sort(a)