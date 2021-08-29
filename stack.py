def stack(num):
    my_data = []
    for i in range(num):
        numb = int(input("Enter entries:-->"))
        my_data.append(numb)
    if len(my_data) == 1:
        return my_data
    else:
        return my_data
        


number = int(input("Enter number of Stack:-"))
my_data_1 = stack(number)
for i in range(len(my_data_1),0,-1):
    print(my_data_1[i-1])