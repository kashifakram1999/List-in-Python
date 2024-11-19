# 1. Write a Python program to sum all the items in a list.
# expense=[22,23,26,21,25]

# j=0
# for i in expense:
#     j +=i
# print(j)


# 2. Write a Python program to multiply all the items in a list.

# expense=[22,23,26,21,25]

# j=1
# for i in expense:
#     j=j*i
# print(j)

# 3. Write a Python program to get the largest number from a list.
# def find_largest(list):
#     largest=list[0]
#     for i in list:
#         if i>largest:
#             largest=i
#     return largest

# print(find_largest([12,15,25,33]))

# 4. Write a Python program to get the smallest number from a list.
# def find_smallest(list):
#     smallest=list[0]
#     for i in list:
#         if i<smallest:
#             smallest=i
#     return smallest

# print(find_smallest([12,15,25,22]))
        
# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# list=['abc', 'xyz', 'aba', '1221','a']
# count=0
# for i in list:
#     if i[0]==i[-1] and len(i)>=2:
#         count +=1
# print(count)

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# expense=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# empty_list=[]

# while expense:
#     smallest_tuple=expense[0]
#     smallest_value=expense[0][1]
#     for i,x in enumerate(expense):
#         if expense[i][1]< smallest_value:
#             smallest_tuple = x
#             smallest_value = x[1]
            
#     empty_list.append(smallest_tuple)
#     expense.remove(smallest_tuple)

# print(empty_list)


# Write a Python program to remove duplicates from a list.
# def remove_duplicates(list):
#     unique=[]
#     for i in list:
#         if i not in unique:
#             unique.append(i)
#     return unique

# list=[12,25,26,12,25,67]  
# print(remove_duplicates(list))      


# Write a Python program to check if a list is empty or not.
# def check_list(list):
#     if len(list)==0:
#         return True
#     else:
#         return False    
        
# list=[]  
# print("Is the given list empty: ",check_list(list))


# Write a Python program to clone or copy a list.

# list=[12,12,25,63]
# new_list = list.copy()

# print("Original list: ",list)
# print("Copied list: ",new_list)


# Write a Python program to find the list of words that are longer than n from a given list of words.
# def get_words_longer(list, n):
#     print("These are that are longer than the given length:")
#     for i in list:
#         if len(i)>n:
#             print(i)
        
           
# word_len =int(input("enter the length of word: "))
# get_words_longer(["apple", "banana", "peaches","furit"],word_len)  


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# def find_common_in_two_list(list1, list2):
#     for i in list1:
#         for x in list2:
#             if i==x:
#                 print(x,i)
#                 return True
#     return False

# list1 =input("Enter first list: ")
# list1=list(map(str.strip,list1.split(",")))
# list2 =input("Enter first list: ")
# list2=list(map(str.strip,list2.split(",")))


# print(find_common_in_two_list((list1),(list2)))

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# def remove_specfic_slement(list):
#     for index in [5,4,0]:
#         del list[index]
#     return list
        
# list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']       
# print(remove_specfic_slement(list))
# ////////////// 2nd attempt///////////////
# def remove_specfic_slement(list):
#     for i in range(len(list) -1,-1,-1):
#         if i == 5 or i == 4 or i ==0:
#             list.remove(list[i])
            
#     return list
            
# list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']       
# print(remove_specfic_slement(list))
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
# array = []
# steric_array= []
# storing_four_array= []
# a =0
# while a < 6:
#     steric_array.append("*")
#     a+=1
# c=0
# while c < 4:
#     storing_four_array.append(steric_array)
#     c+=1
# b =0
# while b < 3:
#     array.append(storing_four_array)
#     b+= 1
# print(array)

# array =[]
# for i in range(3):
#     storing_four_array= []
#     for x in range(4):
#         steric_array = []
#         for z in range(6):
#             steric_array.append("*")
#         storing_four_array.append(steric_array)
#     array.append(storing_four_array)
# print(array)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# def remove_even(list):
#     for index,i in enumerate(list):
#         if i % 2 ==0:
#             list.remove(i)
#             if index != -1:
#                 remove_even(list)
#     return list

# list=[23,34,45,7612,12,75]
# print(remove_even(list))
# /////////////////gpt anser///////////////////////
# def remove_even(lst):
#     # Iterate in reverse to avoid index shifting issues
#     for i in range(len(lst) - 1, -1, -1):
#         if lst[i] % 2 == 0:
#             lst.remove(lst[i])
#     return lst

# # Input list
# my_list = [23, 34, 45, 7612, 12, 75]
# # Print the result of removing even numbers
# print(remove_even(my_list))


# 15. Write a Python program to shuffle and print a specified list.
# import random

# original_list = [1, 2, 3, 4, 5, 6]
# shuffled_list = original_list.copy()  # Create a copy
# random.shuffle(shuffled_list)          # Shuffle the copy

# print("Original List:", original_list)
# print("Shuffled List:", shuffled_list)


# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# list=[]
# count=1

# while count:
#     if count <= 30:
#         list.append(count**2)
#         count +=1
#     else:
#         break
    
# for index, i in enumerate(list):
#     if index<5:
#         print(i)
#     else:
#         break

# for x in range(len(list) -1, len(list)-6,-1):
#     print(list[x])

# ////////alternative method////////////////

# print(list[:5])
# print(list[-5:])

# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# def is_prime(n):
#     for i in n:
#         count=2
#         if i<count:
#             return False
#         while count<i:
#             if i%count==0:
#                 return False
#             else:
#                 count+=1
#     return True

# n=[3,7,5,13,12]
# print(is_prime(n))


# 18. Write a Python program to generate all permutations of a list in Python.
# import itertools

# valuse=[1,2,3]
# prem_list=itertools.permutations(valuse,3)
# print(list(prem_list))

# 19. Write a Python program to calculate the difference between the two lists.
# def diff_btw_two_lists(list1, list2):
#     result=[]
#     if len(list1)==len(list2):
#         i=0
#         while i < len(list1):
#             diff = list1[i] - list2[i]
#             i +=1
#             result.append(diff)
#         return result
#     else:
#         return "length of lists are not equal hence they can't be calculated"
        
# list1=[23,76,12]
# list2=[1,2,24]
# print(diff_btw_two_lists(list1,list2))

# ////////// actual answer/////////////
# list1 = [1, 3, 5, 7, 9]

# # Define another list 'list2' containing different numbers
# list2 = [1, 2, 4, 6, 7, 8]

# # Calculate the difference between 'list1' and 'list2' by converting them to sets and subtracting the sets
# diff_list1_list2 = list(set(list1) - set(list2))

# 20. Write a Python program to access the index of a list.
# def index_of_list(list):
#     for index,value in enumerate(list):
#         print(f"index of value ({value}) is: {index}")

# list=[23,34,65,23]
# index_of_list(list)


# 21. Write a Python program to convert a list of characters into a string.
# def chr_to_str(character):
#     string=""
#     for i in character:
#         string += i
#     return string

# character=["a","h","m","a","r"]
# print(chr_to_str(character))

# 22. Write a Python program to find the index of an item in a specified list.
# def find_index(list, item):
#     for index,value in enumerate(list):
#         if value==item:
#             return index
#     return "Item was not found in the list"
        
# list = ["apple","banana","jackfruit"]
# item = "peach"
# print(find_index(list,item))
        

# 23. Write a Python program to flatten a shallow list.
# list=[[1, 2], [3, 4], [5, 6]]
# flatten_list=[]
# for list_value in list:
#     for value in list_value:
#         flatten_list.append(value)
        
# print(flatten_list)

# //////////////Alternative method///////////////////////
# # Import the 'itertools' module, which provides various functions for working with iterators
# import itertools

# #'original_list' containing nested sublists
# original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# # Use 'itertools.chain' and the unpacking operator (*) to merge the sublists into a single flat list
# new_merged_list = list(itertools.chain(*original_list))

# print(new_merged_list)


# 24. Write a Python program to append a list to the second list.
# list1=[1,2,2,3]
# list2=[9,8,7,6,5,4]
# list1.extend(list2)

# print(list1)


# 25. Write a Python program to select an item randomly from a list.
# import random

# list=[1,2,3,4,5,6,7,8,9]
# print(random.choice(list))

# 26. Write a Python program to check whether two lists are circularly identical.
# a=[3,5,8,9,11,12]
# b=[9,11,3,5,8]


# ///////////////First Try/////////////////
# def check_if_circular(list1,list2):
#     list3=list1+list1
#     count=0
#     if len(list1)!= len(list2):
#         print("Lists are not circular")
#     else:
#         for i in list3:
#             for index2,x in enumerate(list2):
#                 if index2==count and x==i:
#                     count+=1
#                     if count==len(list2):
#                         print("both list are circular")
#                         return  
#         print("Lists are not circular")

# ////////////Alternative methon//////////////
# def check_if_circular(list1, list2):
#     list3 = list1 + list1
    
#     if len(list1) != len(list2):
#         print("Lists are not circular")
#         return

#     for i in range(len(list1)):
#         if list3[i:i + len(list2)] == list2:
#             print("Both lists are circular")
#             return

#     print("Lists are not circular")

# check_if_circular(a, b)



#27&28. Write a Python program to find the second smallest number and second largest number in a list.
# a=[3,5,8,9,11,12]
# a.sort()
# print("Second smallest in the list is:", a[1])
# print("Second largest in the list is:", a[-2])


# 29. Write a Python program to get unique values from a list.

# def unique_values(list):
#     unique=[]
#     for i in list:
#         if i not in unique:
#             unique.append(i)
#     return unique

# list=[12,25,26,12,25,72]  
# print(unique_values(list)) 

# /////Alternative method////////////

# Define a list 'my_list' containing multiple numbers, including duplicates
# my_list = [10, 20, 30, 40, 20, 50, 60, 40]

# # Print the original list 'my_list'
# print("Original List : ", my_list)

# # Convert the 'my_list' to a set 'my_set' to eliminate duplicates and keep unique elements
# my_set = set(my_list)

# # Convert the 'my_set' back to a list 'my_new_list' to obtain a list of unique numbers
# my_new_list = list(my_set)

# # Print the list of unique numbers stored in 'my_new_list'
# print("List of unique numbers : ", my_new_list)


# 30. Write a Python program to get the frequency of elements in a list.
# def feq_of_elm(list):
    # uniq_list=unique_values(list)
    # for i in uniq_list:
#         count = 0
#         for x in list:
#             if i == x:
#                 count+= 1
#         print(f"frequency of {i} is {count}")

# my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# feq_of_elm(my_list)

# # //////////////////////Alternate Method///////////////////
# # Import the 'collections' module, which provides specialized container data types
# import collections

# # Define a list 'my_list' containing multiple numbers, including duplicates
# my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# # Print the original list 'my_list'
# print("Original List : ", my_list)

# # Use the 'collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'ctr'
# ctr = collections.Counter(my_list)

# # Print the frequency of the elements in the list, as provided by the 'ctr' object
# print("Frequency of the elements in the List : ", ctr) 

# 31. Write a Python program to count the number of elements in a list within a specified range.
# def count_number_elements(list, start, end):
#     elements=[]
#     for index, i in enumerate(list):
#         if start<= i <=end:
#             if i not in elements:
#                 elements.append(i)
#     return len(elements)

# list=[1,2,5,6,8,9,36,45,55,6,8,2,3]  
# start=1
# end=11

# list2 = ['a', 'b', 'c', 'd', 'e', 'f']
# inital="a"
# ending="d"

# print(count_number_elements(list2,inital,ending))
# print(count_number_elements(list,start,end))

      

# 32. Write a Python program to check whether a list contains a sublist.      

# def check_sublist(list1, list2):
#     index = 0
#     for index,i in enumerate(list1):
#         if i == list2[0]:
#             count=1
#             while(count < len(list2)) and (list1[index + count] == list2[count]):
#                 count +=1
                
#             if count == len(list2):
#                 return True 
#     return False

# list1=[1,2,4,3,7,2]
# list2=[3,2,2,3,4,5,5]
# print(check_sublist(list1,list2))

# 33. Write a Python program to generate all sublists of a list.
# from itertools import combinations
# def sublists(lst):
#     result = []
#     for rang in range(len(lst) + 1):
#         result.extend(combinations(lst, rang))
#     return result

# list1 = [1,2,3]
# print(f"original list: {list1}")
# print(f"sublists: {sublists(list1)}")


# 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# def compute_prime(n):
#     prime_num=[]
#     non_prime_num=[]
#     for i in range(2,n+1):
#         if i not in non_prime_num:
#             prime_num.append(i)
#             for j in range(i*i,n+1,i):
#                 non_prime_num.append(j)
#     print(prime_num,"\n",non_prime_num)
            
                
# n=20
# print(compute_prime(n))


# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# def concatenate_list_in_range(list,n):
#     empty_list=[]
#     for i in range(1,n+1):
#         for j in list:
#             empty_list.append(j+str(i))
#     return empty_list

# list=["a","n"]
# print(concatenate_list_in_range(list,4))


# //////////Advance list exercise//////////////

# 1. Write a Python function to reverse a list at a specific location.
# def reverse_lst_spc_location(list, index):
#     list1=[]
#     list2=[]
#     for index1, i in enumerate(list):
#         if index1>=index:
#             list2.append(i)
#         else:
#             list1.append(i)
#     list2.reverse()
#     list1=list1+list2
#     return list1

# list=[12,2,5,3,6,7,8]
# print(reverse_lst_spc_location(list,2))

# //////Alternative Method/////////
# def reverse_list_in_location(lst, start_pos, end_pos):
#     while start_pos < end_pos:
       
#         lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
        
#         start_pos += 1
#         end_pos -= 1

#     return lst

# list=[12,2,5,3,6,7,8]
# print(reverse_list_in_location(list,2,5))  


# def reverse_lst_location(list, index):
#     list1=[]
#     list2=[]
#     for index1, i in enumerate(list):
#         if index1>=index:
#             list2.append(i)
#         else:
#             list1.append(i)
#     list2.reverse()
#     list1=list1+list2
#     return list1

# list=[12,2,5,3,6,7,8]
# print(reverse_lst_location(list,0))

# 36. Write a Python program to get a variable with an identification number or string.
# x = 100

# print(format(id(x), 'x'))

# s = 'kashif'
# print(format(id(s), 'x'))



# def get_variable_id_or_str(id):
#     dic_list=[(1,"Kashif"),
#               (2,"Person"),
#               (3,"Kashif")]
#     for i in dic_list:
#         if i[0]==id:
#             return i[1]
#     return None

# dic=get_variable_id_or_str(1)
# print(dic)
 
 
#  37. Write a Python program to find common items in two lists.
# def common_item(list1,list2):
#     list3=[]
#     for i in list1:
#         for x in list2:
#             if i==x:
#                 list3.append(x)
        
#     return list(set(list3))

# list1=[1,2,3,4,5,6,5,9]
# list2=[2,3,4,5,6,9]

# result=common_item(list1,list2)
# print(result)   

# /////Alternative method////////

# result=list(set(list1) & set(list2))
# print(result)


# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.

# def change_positon(list1,n):
#     while n<(len(list1)-1):
#         list1[n],list1[n+1]=list1[n+1],list1[n]
#         n+=2
#     return(list1)

# list1=[1,2,4,5,6,7,8,0]
# n=0

# result=change_positon(list1,n)
# print(result)


# ////////////Alternative Method//////////////////

# Import the 'zip_longest,' 'chain,' and 'tee' functions from the 'itertools' module
# from itertools import zip_longest, chain, tee

# # Define a function named 'replace2copy' that takes a list 'lst' as input and returns a new list with elements rearranged
# def replace2copy(lst):
#     # Use the 'tee' function to create two independent iterators from 'lst'
#     lst1, lst2 = tee(iter(lst), 2)

#     # Use 'zip_longest' to pair elements from 'lst' with an offset to create a new sequence
#     # Chain the pairs together and convert them to a list
#     return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

# # Define a list 'n' containing numeric elements
# n = [0, 1, 2, 3, 4, 5]

# # Call the 'replace2copy' function with 'n' as the argument and print the result
# print(replace2copy(n)) 



# 39. Write a Python program to convert a list of multiple integers into a single integer.
# def convert_to_single_int(list):
#     converted_list=""
#     for i in list:
#         converted_list+=str(i)
#     return converted_list

# list=[1,2,3,4,5,5]
# result=convert_to_single_int(list)
# print(result)
        
# 40. Write a Python program to split a list based on the first character of a word.
# def split_list_with_chr(word_list):
#     sorted_word_list = sorted(word_list)

#     # Initialize an empty dictionary to store groups
#     grouped_words = {}

#     # Iterate through the sorted list and group words by their first letter
#     for word in sorted_word_list:
#         first_letter = word[0]
#         # If the first letter is not already a key in the dictionary, add it
#         if first_letter not in grouped_words:
#             grouped_words[first_letter] = []
#         # Append the word to the correct group
#         grouped_words[first_letter].append(word)

#     # Now, display the groups
#     for letter, words in grouped_words.items():
#         print(f"\nWords starting with '{letter}':")
#         for word in words:
#             print(f"- {word}")
        
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# split_list_with_chr(word_list)


# 41. Write a Python program to create multiple lists.
# def multi_list(list):
#     empty={}
#     for i in list:
#         empty[i] = []
#     return empty

# list=[1,2,3,4,5,6]
# output=multi_list(list)
# print(output)

# 42. Write a Python program to find missing and additional values in two lists.
# list1=["a","b","c"]
# list2=["c","d","e"]

# # for list 1, missing values are d & e, additional values are a & b
# print("Missing values in list1: ")
# for i in list2:
#     if i not in list1:
#         print(i)


# print("Additional values in list1: ")
# for ij in list1:
#     if ij not in list2:
#         print(ij)

# ///////Alternative method/////////


# list1 = ['a', 'b', 'c', 'd', 'e', 'f']
# list2 = ['d', 'e', 'f', 'g', 'h']


# missing_values = set(list1).difference(list2)
# print(f'Missing values in the second list:, {missing_values}')

# additional_values = set(list2).difference(list1)
# print(f'Additional values in the second list:,{additional_values}')

# 43. Write a Python program to split a list into different variables.
# color = [
#     ("Black", "#000000", "rgb(0, 0, 0)"),
#     ("Red", "#FF0000", "rgb(255, 0, 0)"),
#     ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
# ]

# var1, var2, var3 = color

# print(var1)
# print(var2)
# print(var3)


# 44. Write a Python program to generate groups of five consecutive numbers in a list.
# def generat_consecutive_list(start,list_number):
#     final_list=[]
#     count=1
#     while count<=list_number:
#         temp_list=[]
#         for i in range(1,6):
#             temp_list.append(start)
#             start+=1
#         final_list.append(temp_list)
#         count+=1
#     return final_list
    
    
# print(generat_consecutive_list(1,5))

# 45. Write a Python program to convert a pair of values into a sorted unique array.
# def convert_list(list):
#     result=[]
#     for i in list:
#         for j in i:
#             if j not in result:
#                 result.append(j)
#     result.sort
#     return resul
            
            
# or_list=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)] 
# print(convert_list(or_list))

# 46. Write a Python program to select the odd items from a list.
# def select_odd(list):
#     result=[]
#     for i in list:
#         if i%2!=0:
#             result.append(i)
#     return result

# list=[2,3,4,5,6,7,8,9,0,-13,8]
# print(select_odd(list))

# 47. Write a  Python program to insert an element before each element of a list.
# def insert_element(element,list):
#     result = []
#     for i in range(len(list)):
#         result.append(element)
#         result.append(i)
#     return result

# list=[2,3,4,5,6,7,8,9,0,-13,8]
# print(insert_element("d",list))

# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
# def pirnt_nested(list):
#     for i in list:
#         print(i)

# original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
# print(pirnt_nested(original_list))


# 49. Write a Python program to convert a list to a list of dictionaries.
# def convert_to_dic_list(list1,list2):
#     result = []
#     # for i in range(len(list1)):
#     #     temp_dic ={}
#     #     temp_dic.update({list1[i]:list2[i]})
#     #     result.append(temp_dic)
#     # return result
    
# # /////////alternate////////////
#     for i,j in zip(list1,list2):
#         dic={}
#         dic.update({i:j})
#         result.append(dic)
#     return result

# list1=["Black", "Red", "Maroon", "Yellow"]
# list2= ["#000000", "#FF0000", "#800000", "#FFFF00"]
# print(convert_to_dic_list(list1,list2))


# 50. Write a Python program to sort a list of nested dictionaries.
# def sort_nested_dic(list):
#     result = []
#     while list:
#         largest = list[0]["key"]["subkey"]
#         largest_dic = list[0]
#         for i in list:
#             if largest < i["key"]["subkey"]:
#                 largest = i["key"]["subkey"]
#                 largest_dic = i
#         result.append(largest_dic)
#         list.remove(largest_dic)
#     return result

# list=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]  
# print(sort_nested_dic(list))


# 51. Write a Python program to split a list every Nth element.
# def split_list_nth(elements, n):
#     final=[]
#     list1=elements[0::n]
#     list2=elements[1::n]
#     list3=elements[2::n]
#     final.append(list1)
#     final.append(list2)
#     final.append(list3)
#     return final
    
    

# Orginal_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# print(split_list_nth(Orginal_list,3))


# 52. Write a Python program to compute the difference between two lists.
# def diff_btw_lists(list1,list2):
#     result=[]
#     for i in list1:
#         if i not in list2:
#             result.append(i)
#     return result
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]

# print(diff_btw_lists(color1,color2))


# 55. Write a Python program to remove key-value pairs from a list of dictionaries
# def remove_KW(list, key):
#     for i in list:
#        if key in i:
#            del i[key]
#     return list


# orignal_list=[{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
# print(remove_KW(orignal_list, "key1"))

# 56. Write a Python program to convert a string to a list.
# def convert_str_to_list(string):
#     result = []
#     for character in string:
#         result.append(character)
#     return result

# string = "ahmar is a coder"
# print(convert_str_to_list(string))

# 57.Write a Python program to replace the last element in a list with another list.
# def replace_last_with_list(list1,list2):
    # del list1[-1]
    # for value in (list2):
    #     list1.append(value)
    # return list1

    # alternate///////////////////////
    # list1[-1:] = list2
    # return list1

# list1 = [1,12,3,4]
# list2 = [5,52,6,7]
# print(replace_last_with_list(list1,list2))

# 58 Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# def smallest_sec_idx_tuple(list):
#     smallest_value = list[0][1]
#     smallest_tuple = list[0]
#     for i in list:
#         if i[1]<smallest_value:
#             smallest_value = i[1]
#             smallest_tuple = i
#     return smallest_tuple

# list = [(4, 1), (1, 2), (6, 0)]
# print(smallest_sec_idx_tuple(list))


#61. Write a Python program to create a list of empty dictionaries.
# def create_empty_dic(n):
#     list =[]
#     count = 0
#     while count < n:
#         dic ={}
#         list.append(dic)
#         count += 1
#     return list

# print(create_empty_dic(3))

#62 Write a Python program to print a list of space-separated elements.
# def list_space_sep_elem(string):
#     list=string.split(" ")
#     return (list)
# print(list_space_sep_elem("kashif akram"))  
# ///////// Alternative/////////////////////
# Define a list 'num' containing integers
# num = [1, 2, 3, 4, 5]
# print(*num)


# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# def insert_str_at_elem(list,elem):
#     for i in range(len(list)):
#         list[i] = str(elem) + str(list[i])
#     return list

# list =[1,2,3,4]
# elem = "emp"
# print(insert_str_at_elem(list,elem ))
        
# 64. Write a Python program to iterate over two lists simultaneously.
# def iterate_simul(list1,list2):
#     for i,j in zip(list1,list2):
#         print(i,j)

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# iterate_simul(list1,list2)

# 65. Write a Python program to move all zero digits to the end of a given list of numbers.
# def move_zero_to_end(list):
#     list1=[]
#     list2=[]
#     for i in list:
#         if i==0:
#             list2.append(i)
#         else:
#             list1.append(i)
#     final=list1+list2
#     return final

# list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# print(move_zero_to_end(list))


# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# def find_largest_sum(lst):
#     largest_sum = 0
#     largest_list = lst[0]
#     for i in lst:
#         if largest_sum < sum(i):
#             largest_sum = sum(i)
#             largest_list = i
#     return largest_list

# data = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(find_largest_sum(data))

# # ///// alternate ////////
# num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# # Use the 'max' function to find the maximum sublist in 'num' based on the sum of its elements
# # The 'key' argument specifies a lambda function that calculates the sum of each sublist
# # The 'max' function returns the sublist with the maximum sum
# print(max(num, key=sum)) 

# 67. Write a  Python program to find all the values in a list that are greater than a specified number.
# def find_greater_than_given(lst, value):
#     result = []
#     for i in lst:
#         if value < i:
#             result.append(i)
#     print("these values are greater than the given value: ")
#     return result

# list2 = [5,6,7,8]
# print(find_greater_than_given(list2,6))

# # 68. Write a Python program to extend a list without appending.
# def extent_list(lst1,lst2):
#     return lst1+lst2


# list1=[1,2,3]
# list2=[5,6,7]
# print(extent_list(list1,list2))

# # /////Alternative//////
# list1.extend(list2)
# print(list1)

# # Another alter/////
# list1[:0] =list2
# print(list1)

# 69. Write a Python program to remove duplicates from a list of lists.
# def rem_dupli_from_listoflists(lst):
#     result = []
#     for i in lst:
#         if i not in result:
#             result.append(i)
#     return result
# lst =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# print(rem_dupli_from_listoflists(lst))
# # ///// alternate///////
# # Import the 'itertools' module for working with iterators and grouping
# import itertools

# # Define a list 'num' containing sublists with integers
# num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# # Print a message indicating the purpose of the following output
# print("Original List", num)

# # Sort the list 'num', which sorts the sublists lexicographically
# num.sort()

# # Use 'itertools.groupby' to group similar sublists and retain the first occurrence of each group
# new_num = list(num for num, _ in itertools.groupby(num))

# # Print a message indicating the purpose of the following output
# print("New List", new_num)


# 70. Write a Python program to find items starting with a specific character from a list.
# def find_item_by_char(lst,character):
#     result = []
#     for i in lst:
#         if i.startswith(character):
#             result.append(i)
#     return result

# data = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# print(find_item_by_char(data,"d"))


# 71. Write a Python program to check whether all dictionaries in a list are empty or not.
# def check_empty_dic(lst):
#     status = True
#     for i in lst:
#         for index in i:
#             if index == None:
#                 status = True
#             else:
#                 status = False
#                 break
#     return status
# //////////// alternate//////////////
# def all_dicts_empty(dict_list):
#     for d in dict_list:
#         if d:  # If any dictionary is not empty, return False
#             return False
#     return True  # Return True if no non-empty dictionaries were found

# data = [{6},{},{}]
# print(all_dicts_empty(data))

# 72. Write a Python program to flatten a given nested list structure.
# def flatten_nested_list(lst):
#     result = []
#     for i in lst:
#         if isinstance(i, list):
#             for j in i:
#                 result.append(j)
#         else:
#             result.append(i)
#     return result

# data =[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# print(flatten_nested_list(data))

# 73 Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
# def remove_consecutive_dupli(lst):
#     result = []
#     for i in range(len(lst)):
#         if lst[i-1] != lst[i]:
#             result.append(lst[i])
#         elif i > len(lst):
#             break
#     return result

# data = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4,4]
# print(remove_consecutive_dupli(data))

# 74. Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
# def pack_consecutive_dupli(lst):
#     result = []
#     temp = []

#     for i in range(len(lst)):
#         # If temp is empty or last element in temp matches current, add current to temp
#         if not temp or lst[i] == temp[-1]:
#             temp.append(lst[i])
#         else:
#             # Otherwise, add temp to result and start a new temp
#             result.append(temp)
#             temp = [lst[i]]
    
#     # Append the last group
#     if temp:
#         result.append(temp)
    
#     return result

# # Test data
# data = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# print(pack_consecutive_dupli(data))

