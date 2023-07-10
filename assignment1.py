#question4 Write a function that takes in a non empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
# If no two numbers sum up to target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two diff integers in the array; you can’t add a single integer to
# itself in order to obtain the target sum.
# You can assume that there will be at most one pair of numbers summing up to the target sum.
# Array = [3, 5, -4, 8, 11, 1, -1, 6]
# Targetsum = 10
# Sample output
# [-1,11]

def twosum(Arraylist, target):
    newset=set()
    ans=[]
    for num in Arraylist:
        compliment=target-num
        if compliment in newset:
            ans.append((compliment,num))
        newset.add(num)
    return ans
Array=[3,5,-4,8,11,1,-1,6]
Targetsum=10
result=twosum(Array,Targetsum)
print(result)

#question5 Find all of the numbers from 1–1000 that are divisible by 8 using list comprehension.
div8=[n for n in range(1,1000) if n%8==0]
print(div8)

#question6. Count the number of spaces in a string using list comprehension. Eg string : “my name is Khan”.
text="my name is khan"
no_of_spaces=len([x for x in text if x==" "])
print(no_of_spaces)

#question7 Remove all the vowels from a string using list comprehension.
string=input("enter sring:")
Vowels=['a','e' ,'i','o','u']
remove_vowels=[x for x in string if x.lower() not in Vowels]
string_remove_vowels=''.join(remove_vowels)
print(string_remove_vowels)

#question 8. “A Python list comprehension consists of brackets containing the expression, which is executed
# for each element along with the for loop to iterate over each element in the”
# Find all the words in the string having length less than 4 letters using list comprehension.
def find_the_words(string):
    findwords=string.split()
    shot_words=[word for word in findwords if len(word)<4]
    return shot_words
words=input("enter the string")
result=find_the_words(words)
print(result)
#9. words = ['data', 'science', 'machine', 'learning']
# Using dict comprehension create a dict having list items and their length as value.
# Example : {‘data’ : 4}
listitems=input("enter the list of items")
words=listitems.split()
word_dict={x:len(x) for x in words}
print(word_dict)
#question10. 
def sorted_arr(array):
    ans=list()
    for i in array:
        ans.append(i*i)
    ans2=sorted(ans)
    return ans2
array=input("enter the array")
elements = array.split()
array1 = [int(element) for element in elements]
result=sorted_arr(array1)
print(result)
#question11 You are given a list of integers and an integer. Write a function that moves all
# instances of that integer in the list to the end of the list and returns the list.
# Sample input : [2,1,2,2,2,3,4,5]
# toMove = 2

# Sample output : [1,3,4,2,2,2,2,2]
def move_to_end(lst, to_move):
    count = lst.count(to_move)  # Count the number of occurrences of the integer
    lst = [x for x in lst if x != to_move]  # Create a new list excluding the integer
    lst.extend([to_move] * count)  # Add the integer to the end of the list as many times as its count
    return lst

input1=input("enter the array")
elements = input1.split()
array=[int(x) for x in elements]
moveobj=int(input("enter the element for move"))
ans=move_to_end(array,moveobj)
print(ans)





