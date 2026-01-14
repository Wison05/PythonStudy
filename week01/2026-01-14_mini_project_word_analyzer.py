def read_text_list(L):
    return [word for i in range(L) for word in input().split()]

def read_ban_words(B):
    return [input() for i in range(B)]

def make_lower_word(list):
    return [i.lower() for i in list]

def classify_only_alpha(text_list):
    text_list = [''.join(text for text in list if text.isalpha()) for list in text_list]
    return [t for t in text_list if t != '']

L = int(input()) #review text line number
text_list = read_text_list(L)
text_list = make_lower_word(text_list)
text_list = classify_only_alpha(text_list)
print(text_list)
B = int(input()) #banned words number
ban_words = read_ban_words(B)
print(ban_words)
N = int(input()) #many used word Top N


