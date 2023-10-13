"""
Word Occurrences
Estimate: 25 minutes
Actual:   took breaks in between undetermined
"""
#words = []
#text = input("Text: ")
#in_file = open(words)
#words.append(text)
#in_file.close()
#print(text)
#max_length = max(len(word)) for word in list(words.keys())
#for word in words.keys():
#    print(f"{word:{max_length}} - {len(word)}")

#words = text.split()
#words.sort()
#word_to_count = {}
#print(words)
#for word in words:
#    if word in words:
#        word_to_count[word] += 1
#    else:
#        word_to_count[word] = 1
#print(word_to_count)

text = input("Text: ")
words = text.lower().split()
words.sort()
max_length = max(len(word) for word in words)
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
for word, count in word_to_count.items():
    print(f"{word:{max_length + 1}}: {count:>3}")