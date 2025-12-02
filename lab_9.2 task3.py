for _ in range(3):
    line = input()
    word = line.split()
    words = []
    for w in word:
        w = w.strip(".,:;!?()[]«»\"")
        words.append(w)
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    print(longest)
