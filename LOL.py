meme_dict =   {
                "CRINGE" : "Garip yada utandırıcı bir şey"
                "LOL" : "Komik bir şeye verilen cevap"
                        "SUS" : "Şüpheli bir durumda kullanılır"
        "TROL" : "Alay durumlarında kullanılır"
            }
word = input ("anlamını öğrenmek istediğin modern kelimeyi gir")

    if word in meme_dict.keys():
            print ("aradığın kelimenin anlamı", meme_dict[word])
    else:
        print("maalesef aradğın kelime bende yok")
                
