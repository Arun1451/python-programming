def list_swapping(my_list):
   size_of_list = len(my_list)

   temp = my_list[0]
   my_list[0] = my_list[size_of_list - 1]
   my_list[size_of_list - 1] = temp

   return my_list

my_list = [23,45,22,48,99]
print("The list is :")
print(my_list)
print("The function to swap the first and last elements is swapped")
print(list_swapping(my_list))
