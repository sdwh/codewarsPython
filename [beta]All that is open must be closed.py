def is_balanced(string, caps):
    for open,close in [(caps[i],caps[i+1]) for i in range(0,len(caps),2)]:
        print(open,close)
    for p in [c for c in string if c in caps]:
        pass

print(is_balanced('(Sensei [says) no!]','()[]'))    