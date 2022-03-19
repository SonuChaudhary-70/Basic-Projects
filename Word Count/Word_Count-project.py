with open('village.txt','r') as f:
    story=f.read()

word=story.split()
for i in range(len(word)):
    i+=1
print(f"Number of words in village.txt are : {i}")