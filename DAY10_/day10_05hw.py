#Take a paragraph string. Split into words. Count each word's frequency using .count(). 
#Remove duplicates using a set. Print the top 5 most frequent sorted by count. 
a = "My name is Sumit My name is Sumit is is name name My My My My "

words = a.split()

freq = []

for word in set(words):
    freq.append((word, words.count(word)))

freq.sort(key=lambda x: x[1], reverse=True)

for word, count in freq[:5]:
    print(word, count)


    

