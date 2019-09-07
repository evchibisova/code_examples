from make_mail_list import MailListMaker

mlm = MailListMaker()
print(mlm.mails)  # empty list

mlm.get_from_list(["masha@mail.ru", "ma.sha@mail.ru", "vanya@bk.ru"])
print(mlm.mails)  # ["masha@mail.ru", "ma.sha@mail.ru", "vanya@bk.ru"]

target = mlm.find_target_mails()
print(target)  # ["masha@mail.ru", "vanya@bk.ru"]

count = mlm.count_target_mails()
print(count)  # 2