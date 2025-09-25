list1 = ["mumbai", "hyd", "delhi", "dubai", "jaipur", "kolkata", "chennai", "dadar"]
list2 = [50, 40, 30, 20, 100, 350, 280, 200]
my_dict = {}
for i in range(len(list1)):
    my_dict[list1[i]] = list2[i]
print(my_dict)
