# დაწერე პროგრამა რომელიც ამოწმებს სიტყვების სიას (["car", "dog", "bird"])  თუ სიაში სიტყვა Bird-ს იპოვის ციკლი უნდა შეწყდეს და ეკრაზე დაპრინტოს "we found a bird"
lst = ["car" , "dog" , "bird"]
for i in lst:
    if i == 'bird':
        print("we found a bird")
        break