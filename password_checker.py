print("Password Strength Checker")

password =input("Enter a password: ")

print("Password received")

length_ok = False
has_digit = False
has_upper = False
has_lower = False


if len(password) <6:
    print("WEAK :Too short")

else:
    print("LENGTH is fine")
    length_ok =True

if any(chac.isdigit() for chac in password):
    print("Has Digits")
    has_digit =True

else:
    print("WEAK :No digits")

if any( ch.isupper() for ch in password):
    print("Has uppercase letter")
    has_upper =True

else:
    print("WEAK :NO uppercase letters")


for ch in password:
    if ch.islower():
        has_lower =True
        print("Has Lowercase Letter")
        break

if has_lower:
    print("Has Lowercase Letter")
    
else:
    print("WEAK :NO lowercase letters")


score =0

if length_ok:
    score +=1
if has_digit:
    score +=1
if has_upper:
    score +=1
if has_lower:
    score +=1

if score ==4:
    print("PASSWORD strength: STRONG")

elif score >=2:
    print("PASSWORD strength: MEDIUM")

else:
    print("PASSWORD strength: WEAK")
    