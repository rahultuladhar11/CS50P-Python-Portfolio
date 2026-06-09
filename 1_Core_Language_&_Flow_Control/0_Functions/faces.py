def main():
    text = input("Enter text: ")
    emo_text = convert(text)
    print(emo_text)

def convert(emoticon):
    emoji = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()
