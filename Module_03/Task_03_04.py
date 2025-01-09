def single_root_words(root_word, *other_words):
    same_words = []
    for cur_word in other_words:
        if root_word.upper() in cur_word.upper() or cur_word.upper() in root_word.upper():
            same_words.append(cur_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
