def run():
    list1 = []

    for i in range(1, 11):
        if i % 3 != 0:
            list1.append(i**2)
    print(list1) 

    list2 = [i**2 for i in range(1, 11) if i %3 != 0]
    print(list2)

    list3 = [i**2 for i in range(1,11) if i %4 == 0 and i %9 and i %6]
    print(list3)

    list4 = []
    
    for i in range(1,11):
        if i %4 == 0 and i %5 and i %6:
            list4.append(i**2)
    print(list4)

 

if __name__ == '__main__':
    run()