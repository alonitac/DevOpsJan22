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

couple (1)

men = {"John": 20, "Bill": 10, "Abraham": 45}
women = {"July": 18, "Kim": 26, "lili": 15}

#if (min(men, key=men.get)) and (min(women, key=women.get)):
#    a = min(men, key=men.get), min(women, key=women.get)

#print(a)
#print(type(a))

couple (2)

for (key, value) in men.items():
    if value == min(men.values()):
        for (key2, value) in women.items():
            x = key, key2
        print(x)


couple (3)

men = {"John": 20, "Bill": 10, "Abraham": 45, "Danny": 45}
women = {"July": 18, "Kim": 26, "lili": 15}

max_key = None
max_val = None
max_key1 = None
max_val1 = None

for key, val in men.items():
    if max_val is None or val < max_val:
        max_val = val
        max_key = key
    for key1, val1 in women.items():
        if max_val1 is None or val1 < max_val1:
            max_val1 = val1
            max_key1 = key1

print(max_key, max_val)
print(max_key1, max_val1)
couple = max_key, max_key1
print(type(couple))
print(couple)


last question - sum of digits (1)

aaa = '888'
lst = [int(a) for a in str(aaa)]
suma = 0
for i in range(len(lst)):
    suma = suma + (lst[i])

print(suma)

(7 boom)

for x in range(0, 100):
    if '7' in str(x) or x % 7 == 0:
        print(x)