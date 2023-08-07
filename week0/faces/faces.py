def main ():
    sentence = input ("Enter a sentence: ")
    convert(sentence)

def convert(sen):
    if ":)" in sen:
        sen = sen.replace(":)", "🙂")
    if ":(" in sen:
        sen = sen.replace(":(", "🙁")
    print (sen)

main()