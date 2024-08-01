from textblob import TextBlob
words=[]
n=int(input("Enter the no. of words :"))
for i in range(n):
    x=input("Enter Words :")
    words.append(x)
correct_words = []
for i in words:
    correct_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in correct_words:
    print(i.correct(), end=" ")
