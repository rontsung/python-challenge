import os
# choose text file to analyze
new_text = os.path.join("paragraph_1.txt")
# variables for sentence count and character count sans certain punctuation
counter, sent_count = 0, 0
with open(new_text, "r") as full:
    text = full.read()
    # split string of text into list of words
    word_list = text.split()
    # " - " counts as a word and this annoyed me
    if "-" in word_list:
        word_list.pop(word_list.index("-"))
    # count elements in word list
    word_count = len(word_list)
    # runs through all characters in string
    for char in text:
        # count sentences; doesn't cover exceptions like typos or middle initials
        # remove the character from the letter count
        if char == "." or char == "!" or char == "?":
            sent_count = sent_count + 1
            counter = counter - 1
        elif char == " " or char == "," or char == ";" or char == ":":
            counter = counter - 1
        # add to letter count
        counter = counter + 1
# change counter from integer to float or calculations will round off as integers
counter = counter * 1.
# avg letters per word
let_per = counter / word_count
# avg words per sentence, convert to float first
sent_len = word_count * 1. / sent_count
# print results!
print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count:", word_count) 
print("Approximate Sentence Count:", sent_count)
print("Average Letter Count:", let_per)
print("Average Sentence Length:", sent_len)
