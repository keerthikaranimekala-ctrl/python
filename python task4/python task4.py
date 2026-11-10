
def compress_string(text):
    if not text:
        print("Empty string!")
        return

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    encoded += text[-1] + str(count)

    print("Original String:", text)
    print("Original Length:", len(text))
    print("Encoded String:", encoded)
    print("Encoded Length:", len(encoded))

    if len(encoded) < len(text):
        print("Compression is beneficial.")
    else:
        print("Compression is not beneficial.")


text = input("Enter a string: ")
compress_string(text)
