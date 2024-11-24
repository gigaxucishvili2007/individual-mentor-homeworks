# შექმენი ფუნქცია სადაც შექმნი ლისტს და მაგ ლისტიდან ამოიღებ ყველა სიტყვას სადაც არის a ასო
def remove_a_word(lst):
    result = []
    for i in lst:
        if 'a' not in lst:
            result.append(i)
    print(result)
print(remove_a_word(['Giga', 'python' , 'Mr Daniel']))