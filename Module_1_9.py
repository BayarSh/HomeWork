print("Введите любое слово: ")
example = input()
print(example[0])
print(example[-1])
NumberSimbol = len(example)

if (NumberSimbol-1)%2==0:
   NumOdd=NumberSimbol-2
else:
   NumOdd=NumberSimbol-1

print(example[NumberSimbol-NumOdd:])
print(example[::-1])
print(example[1::2])