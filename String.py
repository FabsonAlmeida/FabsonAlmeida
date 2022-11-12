print("Entry some word or text")
text0=input()

print("Entry some word or text")
text1=input()

print("What do you want to do? \n 1 - Join text \n 2 - Spell the word/text")
option=input()

if option=='1':
   print(text0+text1)
elif option=='2':
   a=len(text0)+len(text1)
   i=0
   text2=text0+text1
   while i<=a:
    print(text2[i])
    i=i+1
