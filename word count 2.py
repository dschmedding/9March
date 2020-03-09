f = open("/Users/dschmedding/PycharmProjects/9March/Harry Potter", "r")
data = f.read()
f.close()
words = data.split(" ")
numb_words = len(words)
numb_words = int(numb_words)
print("The number of words in Harry Potter is", numb_words)

f2 = open("/Users/dschmedding/PycharmProjects/9March/Dracula", "r")
data2 = f2.read()
words2 = data2.split(" ")
numb_words2 = len(words2)
numb_words2 = int(numb_words2)
print("The number of words in Dracula is", numb_words2)

if numb_words > numb_words2:
    print("Harry Potter has more words than Dracula")
if numb_words2 > numb_words:
    print("Dracula has more words than Harry Potter")

unique words = []
