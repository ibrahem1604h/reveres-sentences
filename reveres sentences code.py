sentence=input("Enter a sentence: ").split()
reversed_sentance=[]
x=0
for i in sentence:
  x=x-1
  reversed_sentance.append(sentence[x])
  
print((" ").join(reversed_sentance)) 
