# Encode and Decode Strings

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the 
# original list of strings.

# Please implement encode and decode

def encode(strs):
    res = ""

    for word in strs:
        # make a hash with the lenght of the word and next of the lenght put a # for know where will start the word
        res += str(len(word)) + "#" + word
    
    return res

def decode(word):
    """
    Decodes the encoded string back into a list of strings.
    
    Process:
    - Use two pointers: i and j
    - Move j until it finds the '#' delimiter to get the length of the next word
    - Convert substring word[i:j] to integer (length of word)
    - Extract the word from word[j+1 : j+1+length]
    - Move i pointer to the end of the extracted word to continue parsing
    
    Repeat until the entire string is processed.
    """
    res  = []
    i = 0

    while i < len(word):
        j = i

        while word[j] != "#":
            j += 1

        len_word = int(word[i:j])

        res.append(word[j + 1 : j + 1 + len_word])

        i = j + 1 + len_word
    
    return res


result_encode = encode(["Hola", "Mundo", "como", "estais?"])
print(result_encode)

result_decode = decode("4#Hola5#Mundo4#como7#estais?")
print(result_decode)