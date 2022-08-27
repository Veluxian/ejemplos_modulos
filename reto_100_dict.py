def run ():
    my_dict = {}

    for i in range(1, 101):
        if i%3 != 0:
            my_dict[i] = round(i ** 3)
    print(my_dict)

    my_dict2 = {i: round(i**3, 2) for i in range(1,101) if i % 3 != 0}
    print(my_dict2)

    my_dict3 = {}
    
    for i in range(1, 101):
        my_dict3[i] = round(i ** 0.5, 2)
    print(my_dict3)

    my_dict4 = {i: round(i**0.5, 2) for i in range(1, 101)}
    print(my_dict4)


if __name__ == '__main__':
    run()