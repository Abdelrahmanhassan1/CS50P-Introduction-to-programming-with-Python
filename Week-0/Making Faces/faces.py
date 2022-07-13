def convert(emoji_text):
    if emoji_text == ":)":
        return str("🙂")
    elif emoji_text == ":(":
        return str("🙁")
    else:
        return emoji_text


def main():
    user_words = input().split(" ")
    new_text = []
    for word in user_words:
        new_text.append(convert(word))

    print(" ".join(new_text))


main()
