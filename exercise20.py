def solve(s):
    words = s.split(' ')
    for i in range(len(words)):
        word = list(words[i])
        print(word)
        if len(word) > 0:
            word[0] = word[0].upper()
            words[i] = ''.join(word)
    return ' '.join(words)
        


phrase = '132 456 Wq  m e'


print(solve(phrase))