# Tik tak tok 
s = input("Enter all X and O in a line:") 
ls = [s[0:3], s[3:6], s[6:9], s[0] + s[3] + s[6], s[1] + s[4] + s[7], s[2] + s[5] + s[8], s[0] + s[4] + s[8], s[6] + s[4] + s[2]]
print(f"""
---------
| {s[0]} {s[1]} {s[2]} |
| {s[3]} {s[4]} {s[5]} |
| {s[6]} {s[7]} {s[8]} |
---------""")
if ("XXX" in ls and "OOO" in ls) or abs(s.count("X") - s.count("O")) >= 2:
    print("Impossible")
elif "_" not in s and "XXX" not in ls and "OOO" not in ls:
     print("Draw")
elif "_" in s and "XXX" not in ls and "OOO" not in ls:
    print("Game not finished")
elif "XXX" in ls:
    print("X wins")
elif "OOO" in ls:
     print("O wins") 
