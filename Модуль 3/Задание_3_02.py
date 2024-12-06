def send_email(message, recipient, *, sender="university.help@gmail.com"):

    # Проверка на корректность e-mail отправителя и получателя.
    if check_email(recipient) == False  or check_email(sender) == False:
       print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    # Проверка на отправку самому себе.
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    # Проверка на отправителя по умолчанию.
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

def check_email(email_adress):
    # == Функция проверки на корректность e-mail ==
    domen_list = ['.com', '.ru', '.net']
    n = len(email_adress)
    flg_email_correct = False

    if "@" in email_adress:
        for cur_domen in domen_list:
            m = len(cur_domen)
            if email_adress[n - m : n] == cur_domen:
                flg_email_correct = True
                break
    if flg_email_correct:
        return True
    else:
        return False

print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.fanmail.ru'))
