sentences = [
    "Python makes coding fun",
    "List comprehensions are powerful",
    "Keep practicing daily"
]


def len_cal(sent):
    l =  len(sent)
    for i in range(l):
        sub_str = sent[i].split()
        for j in range(len(sub_str)):
            if len(sub_str[j]) > 3:
                print(f"{sub_str[j]} -length  - {len(sub_str[j])}")

print(len_cal(sentences))
