print("csv cleaner")
import csv 

path1 = input("Enter the path of csv file:")

with open(path1, newline ="") as file:
    reader =csv.reader(file)

    header =next(reader)
    print("header--->",  header)

    count =0
    cleaned_rows =[]


    for row in reader:
        if not any(cell.strip() for cell in row):
            continue

        clean_row =[cell.strip() for cell in row]
        count +=1
        cleaned_rows.append(clean_row)
        print(clean_row)
    print(f"Total rows cleaned: {count}")


# Output clean file

path2 =input("Enter the path for a new csv file:")

with open(path2, "w", newline ="") as new_file:
    writer =csv.writer(new_file)

    writer.writerow(header)

    for row in cleaned_rows:
        writer.writerow(row)