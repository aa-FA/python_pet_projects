#email cleance form
def clear_emails():
    email = input()
    cut_spaces = email.strip()
    lower_emails = cut_spaces.lower()
    print(lower_emails)

clear_emails()
print(clear_emails())

#добавить обязательное условие почты через @
#добавить лист с отредактированными почтами
#интегрировать на другую платформу, например в эксель или дата базу