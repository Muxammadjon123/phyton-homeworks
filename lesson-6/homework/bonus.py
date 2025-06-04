
try:
    with open("sample.txt", "r") as file:
        text = file.read()
except FileNotFoundError:
    print("sample.txt not found. Please enter a paragraph:")
    text = input(">> ")
    with open("sample.txt", "w") as file:
        file.write(text)


text = text.lower()


punctuations = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '/', '\\']
for p in punctuations:
    text = text.replace(p, "")

words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


total_words = sum(word_counts.values())


sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

n=int(input("Please enter n top words:"))
top_n = sorted_words[:5]


print(f"\nTotal words: {total_words}")
print(f"Top {n} most common words:")
for word, count in top_n:
    print(f"{word} - {count} time{'s' if count > 1 else ''}")


with open("word_count_report.txt", "w") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write(f"Top {n} Words:\n")
    for word, count in top_n:
        report.write(f"{word} - {count}\n")
