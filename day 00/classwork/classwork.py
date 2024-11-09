# # შექმენი ფუნქცია სადაც გაიგებ მომხმარებლის შემოტანილი პაროლი == თუ არა ძველ პაროლს 
# def new_password_and_old_password():
#     new_password = input("enter your password")
#     old_password = 'programmingbest'
#     if new_password != old_password:
#         return 'ar udris'
#     else:
#         return 'udris'
# print(new_password_and_old_password())


#შექმენი ფუნქცია სადაც მომხმარებელმა უნდა შეასრულოს რეგისტრაცია 
# და რეგისტრაციაში უნდა შეიტანოს email password date ანუ როდის 
# დაიბადა და ასევე რატომ შემოდის გოაში
def registration():
        email = input('enter your email')
        print(f'you email is this {email}')
        password = input('enter your password')
        print(f"you password is this {password}")
        date = input('enter your date')
        print(f'you date is this {date}')
        question = input('enter your question')
        print(f'you question is this {question}')
        print('you email is this')
        print("you password is this")
        print('you date is this')
        print('you question is this')
registration()
