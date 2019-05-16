def find_long_word(word_list):
    word_list.sort(key=len)
    return word_list
print(find_long_word(["mani","mnIASSSS","MHFEBFJBSFF","M"]))
