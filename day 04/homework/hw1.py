# შექმენი ფუნქცია სადაც გამოიტან ყველა იმ სიტყვას სადაც არაა aeiou ნახსენები
"""
def find_a_e_i_o_u_letter(lst):
    for i in lst:
        if 'aeiou' not in i:
            print("aeiou ar aris am siashi" , lst)
print(find_a_e_i_o_u_letter("html" , "website" ,))
"""