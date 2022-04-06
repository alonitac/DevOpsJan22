Q1

s = 0
elements = [-64, -8, -8, 16, 32]
for num in elements:
    if not elements or all(isinstance(num, str) for num in elements):
        quit()
    elif isinstance(num, int):
        s += num
print(s)
----------------------------------------------------------------------------------------

Q2

word = 'doing'
word_original = word
length = len(word)
# If I want to catch all "iNG/Ing/INg" options uncomment the next line
# word = word.lower()

if length >= 3 and word.endswith('ing'):
    print(word_original + "ly")
elif length >= 3 and not word.endswith('ing'):
    print(word_original + "ing")
else:
    print(word_original)


----------------------------------------------------------------------------------------

Q3 - GO OVER

words = ['take', 'me', 'home']
words = ' '.join(words)
print(words)

----------------------------------------------------------------------------------------

Q4 - GO OVER

words = ['take', 'me', 'home']
words = ' '.join(words[::-1])
print(words)

----------------------------------------------------------------------------------------

Q5







----------------------------------------------------------------------------------------
Q6

My_List = [1,-2]
My_List.reverse()
My_List2 = []
MyLeng = -len(My_List)
for i in My_List:
    My_List2.append((My_List[MyLeng] - My_List[MyLeng + 1]))
    MyLeng += 1
    if MyLeng == -1 :
        My_List2.append(None)
        break
My_List2.reverse()
print(My_List2)
----------------------------------------------------------------------------------------