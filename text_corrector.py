from textblob import TextBlob
words=[]
n=int(input("Enter the no. of words :"))
for i in range(n):
    x=input("Enter Words :")
    words.append(x)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")
