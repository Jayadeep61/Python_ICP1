name = input("Enter a string: ")   #String as a input
rem_char = name.replace("o", "")   #Deleting letter 'O' from the string
final = rem_char.replace("t", "")
print(final[::-1])   #Using this function we can reverse the string. We can also provide indexes to sort.