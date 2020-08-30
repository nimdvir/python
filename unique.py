import urllib.request, urllib.parse, urllib.error
import re

fhand = urllib.request.urlopen('https://raw.githubusercontent.com/nimdvir/teaching/master/imdb.txt')
#fhand2 = " ".join(re.findall("[a-zA-Z]+", fhand))
counts = dict()
for line in fhand:
    words = line.decode().split()
    #words = words.lower()
    #words2 = " ".join(re.findall("[a-zA-Z]+", words))
    for word in words:
        word = word.lower()
        words2 = " ".join(re.findall("[a-zA-Z]+", word))
        words3 = words2.split()
        for word2 in words3:
            counts[word2] = counts.get(word2, 0) + 1
unique_words = 0
total_words=0
for entry in counts:
    unique_words += 1
    total_words = total_words + counts[entry]
print(unique_words)
print(total_words)
sorted_counts = sorted(counts, key=counts.get, reverse=False)
print(sorted_counts)
for count in sorted_counts:
    print(count, " - ", counts[count] )