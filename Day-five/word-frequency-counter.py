def word_counter():
    text = input("Enter a sentence:\n").lower()

    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\n📊 Word Frequency:\n")
    for word, count in word_count.items():
        print(f"{word}: {count}")

word_counter()