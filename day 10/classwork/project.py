# 2) შექმენი მაღაზია სადაც გექნება პროდუქტები, პირველ რიგში შემოატანინე მომხმარებელს მისი ბალანსი, შემდეგ შექმენი პროდუქტები და გაარკვირე რომელი პროდუქტების შეძენა შეგვიძლია, მინიმუმ უნდა იყოს 5 პროდუქტი და უნდა ჰქონდეს ყველა პროდუქტს მისი ფასი

balance = int(input("enter your balance"))
products = ["milk", "drink", "butter", "Bread"]

if balance == 3:
    print("you can buy milk")
elif balance == 250:
    print("you can buy drink")
elif balance == 5:
    print("you can buy butter")
elif balance == 70:
    print("you can buy Bread")