# cw
# გამოიტანე რიცხვები 10 დან 20 მდე, უკუსვლით მაგ: 20,19,18 ასე შემდეგ
"""
for i in reversed (range(10,21)):
    print(i)

"""

# 2)
# გამოიტანე რიცხვები 1 დან 20 მდე for loop ის მეშვეობით, შემდეგგამოტოვე რიცხვი 6,
"""
for x in range(1,21):
    if x == 6:
        continue
    print(x)
"""

# 3)
# გამოიტანე რიცხვები 1 დან 20 მდე for loop ის მეშვეობით, 15 ის მერე რიცხვები აღარ გამოვიდეს
"""
for x in range(1,21):
    if x == 16:
        break
    print(x)
"""


# 4)
# გამოიტანე რიცხვები 1 დან 20 მდე, უკუსვლით მაგ: 20,19,18 ასე შემდეგ
# გამოტოვე 15, და 18,
# შემდეგ 6 ის მერე შეჩერდეს ციკლი
# გამოიყენე: reversed, continue, break

"""
for x in reversed (range(1,21)):
    if x == 15:
        continue
    elif x == 18:
        continue
    elif x == 5:
        break
    print(x)
"""




