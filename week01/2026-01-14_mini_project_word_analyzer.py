import re
from collections import Counter


def read_text_list(L):
    return [word for i in range(L) for word in input().split()]

def read_ban_words(B):
    return [input() for i in range(B)]

def make_lower_word(list):
    return [i.lower() for i in list]

def classify_only_alpha(text_list):
    text_list = [''.join(ch for ch in s if ch.isascii() and ch.isalpha()) for s in text_list if not any(ch.isdigit() for ch in s)]
    return [t for t in text_list if t != '' and len(t)>1]

def reduce_text_length(text_list):
    return [re.sub(r"(.)\1{2,}",r"\1\1",text) for text in text_list]

def masking_ban_words(text_list,ban_list):
    return ["***" if text in ban_list else text for text in text_list ]

def ratio_cnt_dict(text_list): #edit part
    filtered = [t for t in text_list if t != "***"]
    total = len(filtered)
    cnt = Counter(filtered)
    return {word: (cnts,(cnts/total if total else 0.0)) for word,cnts in cnt.items()}

def cal_ratio(cnt,total):
    return cnt/total

def return_top_n(text_ratio_dict,N):
    return dict(sorted(text_ratio_dict.items(), key=lambda x: x[1][0], reverse=True)[:N]) #edit part

L = int(input()) #review text line number
text_list = read_text_list(L)
text_list = make_lower_word(text_list)
text_list = classify_only_alpha(text_list)
text_list = reduce_text_length(text_list)
B = int(input()) #banned words number
ban_words = read_ban_words(B)
text_list = masking_ban_words(text_list,ban_words)
text_ratio = ratio_cnt_dict(text_list)
N = int(input()) #many used word Top N
text_ratio = return_top_n(text_ratio,N)

print("CLEANED_TEXT:")
print(' '.join(text_list),"\n")
print("TOP_WORDS:")
for key,value in text_ratio.items():
    print(f"{key}: {value}")
print()
print("BAN WORDS:")
print(' '.join(ban_words))





