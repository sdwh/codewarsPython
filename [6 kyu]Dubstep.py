import re
def song_decoder(song):
    print(song)
    return ' '.join([word for word in re.findall(r'[A-Z]*',song.replace('WUB',' ')) if len(word) != 0])

print(song_decoder('WUBAWUBCCWUBDD'))