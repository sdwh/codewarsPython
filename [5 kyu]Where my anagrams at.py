def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

print(anagrams('aabb',['aabb','bbaa','ccaa','baba']))
