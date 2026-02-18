#vowels and consonent in a strings=input("Enter a string: ").lower()
vowels=['a', 'e', 'i','o','u']
vowelsNum=0
cosonentNum=0
for i in s:
  if i.isalpha():
    if i in vowels:
     vowelsNum+=1
    else:
      cosonentNum+=1
print(vowelsNum,cosonentNum)
