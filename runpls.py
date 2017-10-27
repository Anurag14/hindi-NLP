def get_count(text):
    words = text.split()
    count=0
    vowels = ['a', 'e', 'i', 'o', 'u']
    cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','y','z']
    for word in words:
        ch=word[0]
        for i in range(1,len(word)-1,1):
            if word[i] in vowels and word[i-1] in cons:
                count+=1
                break
    return count
            
def xx_count(text):
    words = text.split()
    count=0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        ch=word[len(word)-1]
        if ch in vowels:
            count+=1
    return count


def eval_text(text):
    words = text.split()
    if len(words) == 0:
        print "Empty text"
        return
    raw_features = [0, 0, 0, 0, 0]
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in words:

        if len(word) <= 2: continue
        # Ends with vowels for italian.
        if word[-1] in vowels:                      raw_features[0] += 1
        if word[-1] == '.' and word[-2] in vowels:  raw_features[0] += 1

        # Long words in dutch.
        #if len(word) > 8:   raw_features[1] += 1

        # Words ending in "ed" for English in past tense.
        if word[-2:] == 'ed': raw_features[4] += 1

    #raw_features[1] = text.count('en')  # bigram en.
    raw_features[2] += 4 * text.count('hai')

    # ij pretty much NEVER shows up anywhere ever except Dutch!
    raw_features[1] += text.count('wo')

    # 'th' for english as most frequent bigram
    raw_features[3] = 2 * text.count('th')

    raw_features = [feature * 1.0 / len(words) for feature in raw_features]

    return raw_features


def get_example_set():

    op = [0,0,0]
    combined_set=[]
    with open('nl_big') as f:
        for line in f:
            print line
            this_example_op = op[:]
            #this_example_op[index] = 1
            combined_set.append((eval_text(line), this_example_op))


    ip,op=[],[]
    for i,o in combined_set:
       print i
       print o

get_example_set()
