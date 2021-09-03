data_translate = {
    'one': 'một',
    'two': 'hai',
    'three': 'ba',
    'four': ' bon',
    'five': 'nam',
    'six': 'sau',
    'seven': 'bay',
    'eight': 'tam',
    'nine': 'chin',
    'ten': 'muoi',
}
reverse_dic = {data_translate[k] : k for k in data_translate}
print(reverse_dic)
def tran_english(eng,vn):
    for word in eng:
        if eng[word] == vn:
            print(eng[word] ,":" ,word)
        else:
            print("Sorry ! This word not available")
input_word = input("Pleae enter word to translate VN: ")
tran_english(reverse_dic,input_word)