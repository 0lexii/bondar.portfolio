import re
import sqlite3

conn = sqlite3.connect('pol_lab07.s3db')
c = conn.cursor()

c.execute("SELECT sgN FROM tnoun WHERE sgN='stół'")
print(c.fetchone()[0])

c.execute("SELECT sgN FROM tnoun WHERE sgA LIKE 'd_%'")
print(", ".join([str(word[0]) for word in c.fetchall()]))

gender = "1"
nw = "pies"
c.execute(f"INSERT INTO tnoun (gender, sgN) VALUES (?, ?)", (gender, nw))
c.execute("SELECT sgN, gender FROM tnoun ORDER BY id DESC LIMIT 1")
print(c.fetchone())


def parse(lemma):
    pattern1 = re.compile(f"(?P<word>\w+)\t{lemma}\t(?P<tags>.+)")
    pattern2 = re.compile("(?<=sg:)[\w\.]+(?=:)")
    with open("parse_lab07.txt", "r", encoding="utf-8") as h:
        lines = h.readlines()

    valid = []
    for line in lines:
        check = re.match(pattern1, line)
        if check:
            valid.append(check.group("word", "tags"))

    sgN = sgG = sgD = sgA = sgI = sgL = sgV = None

    for line in valid:
        iter = re.finditer(pattern2, line[1])
        if iter:
            for i in iter:
                if i.group(0) == "nom":
                    sgN = line[0]
                elif i.group(0) == "gen":
                    sgG = line[0]
                elif i.group(0) == "dat":
                    sgD = line[0]
                elif i.group(0) == "acc":
                    sgA = line[0]
                elif i.group(0) == "inst":
                    sgI = line[0]
                elif i.group(0) == "loc":
                    sgL = line[0]
                elif i.group(0) == "voc":
                    sgV = line[0]

    return [sgN, sgG, sgD, sgA, sgI, sgL, sgV]


forms = parse(nw)

if forms:
    column_list = ["N", "G", "D", "A", "I", "L", "V"]
    for i, column in enumerate(column_list):
        if forms[i]:
            c.execute(f"UPDATE tnoun SET sg{column}=? WHERE sgN = ?", (forms[i], nw))

c.execute("SELECT * FROM tnoun ORDER BY id DESC LIMIT 1")
print(c.fetchone())

conn.commit()
conn.close()
