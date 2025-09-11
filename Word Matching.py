def match_words(words):
    counter = 0
    empty_list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
            empty_list.append(word)
    print("List of Words with first letter and last letter same : ", empty_list)
    return counter
count = match_words(['abc', 'cfc' , 'xyz' , 'aba' , '1221' ])
print("Count of words having first letter and last letter same : " , count)