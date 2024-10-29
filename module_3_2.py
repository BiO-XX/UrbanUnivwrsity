a = 0


def check_sub_str(string, sub_str):
    global a
    a = string.count(sub_str)


def send_email(massage, recipient, sender="university.help@gmail.com"):
    check_sub_str(string=recipient, sub_str="@")
    check_1 = a

    check_sub_str(string=recipient, sub_str=".ru")
    check_2 = a

    check_sub_str(string=recipient, sub_str=".com")
    check_3 = a

    check_sub_str(string=recipient, sub_str=".net")
    check_4 = a

    check_sub_str(string=sender, sub_str="@")
    check_5 = a

    check_sub_str(string=sender, sub_str=".ru")
    check_6 = a

    check_sub_str(string=sender, sub_str=".com")
    check_7 = a

    check_sub_str(string=sender, sub_str=".net")
    check_8 = a

    sender_check = sender.lower()
    recipient_check = recipient.lower()

    check_recipient = 0
    check_sender = 0

    if check_2 == 0 and check_3 == 0 and check_4 == 0:
        check_recipient = 1

    elif check_1 == 0:
        check_recipient = 1
    elif check_6 == 0 and check_7 == 0 and check_8 == 0:
        check_sender = 1
    elif check_5 == 0:
        check_sender = 1
    else:
        check_recipient = 0
        check_sender = 0

    if check_recipient == 1 or check_sender == 1:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender_check == recipient_check:
        print(f"Нельзя отправить письмо самому себе!")

    elif sender_check == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
