import Homework

print(Homework)

text = "The further classes has been cancelled"
translate = " "
words = text.split()
for w in words:
    translate = translate + " " + Homework.d[w]

print(translate)
