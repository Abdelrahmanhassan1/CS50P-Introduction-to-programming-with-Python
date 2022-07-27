

def main():

    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "o", "i", "u"]
    shortened_text = ""
    for char in word:
        if char.lower() in vowels:
            continue
        shortened_text += char

    return shortened_text


if __name__ == "__main__":
    main()
