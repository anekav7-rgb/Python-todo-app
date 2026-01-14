print("Log Analyzer")
import os

path1 =input("Enter path for log file:")
info_count=0
warning_count=0
error_count=0

error_lines =[]

try:
    with open(path1 ,newline ="") as file:
        for num,line in enumerate(file ,start =1):
            print( f"{num}: {line.strip()}")
            if "[INFO]" in line:
                info_count +=1
        
            elif "[WARNING]" in line:
                warning_count +=1
        
            elif "[ERROR]" in line:
                error_count +=1

                error_lines.append(line)
except FileNotFoundError:
    print("Error: Log file not found. Check the path.")
    exit()

except PermissionError:
    print("Error: Permission denied while opening the log file.")
    exit()

print (f"\n Summary")
print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
print(f"ERROR: {error_count}")


try:
    with open("errors.log", "w") as out_file:
        for line in error_lines:
            out_file.write(line)
    print("Errors file: errors.log created")

except PermissionError:
    print("Error: Cannot write errors.log (permission issue).")

