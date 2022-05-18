import re
import time
import unicodedata

import termooo


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


words_final = {}
for i in termooo.words_used:
    words_final.update({remove_accents(i): i})
# words_final |= termooo.words_a


def search_5():
    emmbed_dict = []
    w_not = "umasenhv"
    w_have = "trgoi"
    w_local = "t...."
    w_not_local = ".grr."

    regex_not = "".join([f"(?!.*{x})" for x in w_not])
    regex_have = "".join([f"(?=.*{x})" for x in w_have])
    regex_local = f"(?={w_local})" if w_local != "....." and w_local != "" else ""
    regex_not_local = f"(?!{w_not_local})" if w_not_local != "....." and w_not_local != "" else ""

    pattern = f"^{regex_not}{regex_have}{regex_local}{regex_not_local}.*$"
    for word in words_final:
        if re.fullmatch(pattern, word):
            emmbed_dict.append(words_final[word])
    return emmbed_dict


start_time = time.time()
words = search_5()
print(sorted(words)[:2000])
print("\nTotal words:", len(words))
print("Time execution: ", time.time() - start_time)
