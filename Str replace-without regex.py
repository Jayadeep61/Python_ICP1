text = input("Enter the sentence: ")

text_string = text.split()    #Splitting the input string at spaces
final = ''

for i in text_string:    #Checking the string for word Python

    if i == 'Python':
        i = 'Pythons'
    final += i + ' '

print(final)
