def send_email(massage, recipient, sender="university.help@gmail.com"):
    recipient.lower()
    sender.lower()
    a = len(recipient)
    b = len(sender)
    if recipient.count(".ru", (a-3), a) == 0 and recipient.count(".com", (a-4), a) == 0 and recipient.count(".net", (a-4), a) == 0 or recipient.count("@") == 0:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender.count(".ru", (b-3), b) == 0 and sender.count(".com", (b-4), b) == 0 and sender.count(".net", (b-4), b) == 0 or sender.count("@") == 0:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
