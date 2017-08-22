import os
#import csv
new_text = os.path.join("..", "Pythonday1", "Hello2.txt")
counter = 0
full = open("Hello2.txt", "r")
text = full.read()
#with open(new_text) as new_text:
word_list = text.split()
if "-" in word_list:
    word_list.pop(word_list.index("-"))
word_count = len(word_list)
sent_count = 0
for char in text:
    if char == "." or char == "!" or char == "?":
        sent_count = sent_count + 1
    if char == " " or char == "." or char == "," or char == "?" or char == "!" or char == "'" or char == "-":
        counter = counter - 1
    counter = counter + 1
counter = counter * 1.
let_per = counter / word_count
sent_len = word_count * 1. / sent_count
print("words: " + str(word_count), "sentences: " + str(sent_count), "letter count per word: " + str(let_per), "avg sent len: " + str(sent_len))
print(word_list)
