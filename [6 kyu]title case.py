def title_case(title, minor_words = ''):
    if len(title) == 0:
        return ''
    res = [title.title().split()[0]]
    for word in title.title().split()[1:]:
        if word.lower() in [w.lower() for w in minor_words.split()]:
            res.append(word.lower())
        else:
            res.append(word)
    return ' '.join(res)

print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('', ''))