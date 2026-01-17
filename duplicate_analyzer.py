print("Duplicate & Frequency Analyzer")

lst =input("Enter a list of number seperated by spaces:")

numbers = [int(x) for x in lst.strip().split()]
print(numbers)

seen =set()
duplicates =[]
freq ={}

for num in numbers:
    if num in seen:
        duplicates.append(num)

    else:
        seen.add(num)

for num in numbers:
    if num in freq:
        freq[num] +=1

    else:
        freq[num] =1

print("Duplicates:", duplicates)
print("Seen:", seen)
print("Frequency:", freq)

# Most frequent Element

max_freq =max(freq, key= freq.get)

print(f"Most frequent :{max_freq} ({freq[max_freq]}) times" )


