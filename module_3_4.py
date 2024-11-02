def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        check_word = word.lower()
        chek_root_word = root_word.lower()
        if chek_root_word.count(check_word) > 0 or check_word.count(chek_root_word) > 0:
            same_words.append(word)
        else:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)