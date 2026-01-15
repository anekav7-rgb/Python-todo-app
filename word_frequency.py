print("Word Frequency Analyzer")

import string 

path1 =input("Enter a text file: ")

word_count ={}
with open(path1, newline ="") as file:
    for line in file:
            raw_words =line.strip().lower().split()
            words =[]

            for word in raw_words:
                  clean_word =word.strip(string.punctuation)

                  #For ignoring empty strings
                  if clean_word:
                        words.append(clean_word)

            for word in words:
                word_count[word] =word_count.get(word, 0) +1

    print(word_count)

    #N--> How many top results?

    N= int(input("How many top results do you want?"))
    items =word_count.items()

    sorted_words =sorted(items, key=lambda x: x[1], reverse =True)

    for word, count in sorted_words[:N]:
            print(f"{word}--> {count}")
