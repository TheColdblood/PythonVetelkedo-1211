def Negyedik():
    KariVers = open("szoveg/KariVers.txt", "r", encoding="utf-8")
    vers = KariVers.read()
    KariVers.close()

    KariVers2 = open("szoveg/KariVers2.txt", "a", encoding="utf-8")
    KariVers2.write(vers)
    KariVers2.write("\n Tiszta öröm tüze átég \na szemeken, a harangjáték \nszól, éjféli üzenet: \nKis Jézuska született!")
    KariVers2.close()
