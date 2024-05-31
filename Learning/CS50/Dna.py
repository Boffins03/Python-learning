from sys import argv
import csv

def main(argv):
    # Checking the argument length
    if len(argv) == 3:
        # opening the database file
        rows = []
        with open(f"{argv[1]}") as db_file:
            database = csv.DictReader(db_file)
            db_rows = database.fieldnames
            # db_rows.remove("name")
            # print(db_rows)
            for row in database:
                rows.append(row)
        # print(f"row:{row}")
        # opening the sequences file
        with open(f"{argv[2]}") as seq_file:
            sequences = csv.DictReader(seq_file)
            seq_row = sequences.fieldnames

        sequence = seq_row[0] # assgin the text into variable
        a = len(sequence) # calculating the length of string

        # counting the STRs and add into dict.
        dic = {}
        z = 0 # count variable in i
        x = 1 # starting index check
        for i in db_rows:
            temp = sequence
            y = 0
            final_count = [0]
            while (a > 0):
                try:
                    index = 0
                    lc = temp.index(i)
                    index += lc
                    if index == 0 and lc == 0 and z == 0 and y == 0:
                        x = 0

                    temp = temp[lc + len(i):]
                    if index == 0:
                        z = z + 1
                        final_count.append(z)

                    if index != 0:
                        z = 0
                        y += 1

                    a -=1
                except:
                    break

            max_count = final_count[0]
            for k in range(len(final_count)):
                if final_count[k] > max_count:
                    max_count = final_count[k]

            if x == 0:
                temp = {i:str(max_count+1)}
                x = 1
                max_count = 0
                dic.update(temp)
            else:
                temp = {i:str(max_count)}
                max_count = 0 # count variable reset
                dic.update(temp)

        count = 0
        t = 0
        for match in rows:
            count = 0
            for j in db_rows:
                if match[j] == dic[j]:
                    count = count + 1
                if count == (len(db_rows) - 1):
                    print(match["name"])
                    t = 1
                    break

        if t == 0:
            print("No match")
    else:
        print("Not enough argument given")

main(argv)
