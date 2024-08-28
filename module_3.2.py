def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' not in sender or sender[-4:] not in ['.com', '.ru', '.net']:
        print("Невозможно отправить письмо с адреса <{}> на адрес <{}>".format(sender, recipient))
        return
    if '@' not in recipient or recipient[-4:] not in ['.com', '.ru', '.net']:
        print("Невозможно отправить письмо с адреса <{}> на адрес <{}>".format(sender, recipient))
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса <{}> на адрес <{}>.".format(sender, recipient))
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{}> на адрес <{}>".format(sender, recipient))

message = input("Введите сообщение для отправки: ")
recipient = input("Введите адрес получателя: ")
sender = input("Введите адрес отправителя (по умолчанию university.help@gmail.com): ")

send_email(message, recipient, sender)