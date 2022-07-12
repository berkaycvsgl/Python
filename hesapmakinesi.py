s1 = "1. topla"
s2 = "2. çıkar"
s3 = "3. çarp"
s4 = "4. böl"
s5 = "5. karesini hesapla"
s6 = "6. karekökünü hesapla"


a1 = "{} istediğiniz ilk sayıyı giriniz. \n"
a2 = "{} istediğiniz ikinci sayıyı giriniz. \n"


print(s1, s2, s3, s4, s5, s6, sep="\n")

while True: 
    soru = input("yapmak istediğiniz işlemin numarasını giriniz. \n(Çıkış yapmak için q)\n")

    if soru == "q":
        print("çıkılıyor..")
        break

    elif soru == "1":
    
        sayı1 = int(input(a1.format("toplamak")))
        sayı2 = int(input(a2.format("toplamak")))
    
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2 , "\n","-" *30)
    
    elif soru == "2":
    
        sayı1 = int(input(a1.format("çıkarmak")))
        sayı2 = int(input(a2.format("çıkarmak")))
    
        print(sayı1, "-", sayı2, "=", sayı1 - sayı2, "\n", "-" * 30)

    elif soru == "3":

        sayı1 = int(input(a1.format("çarpmak")))
        sayı2 = int(input(a2.format("çarpmak")))
    
        print(sayı1, "*", sayı2, "=", sayı1 * sayı2, "\n", "-" * 30)
    
    elif soru == "4":

        sayı1 = int(input(a1.format("bölmek")))
        sayı2 = int(input(a2.format("bölmek")))
   
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2, "\n", "-" * 30)

    elif soru == "5":
    
        sayı1 = int(input(a1.format("karesini almak")))
    
        print(sayı1,"'in karesi", sayı1**2, "'dir")
    
    elif soru == "6":
    
        sayı1 = int(input(a1.format("karekökünü almak")))
    
        print(sayı1,"'in karekökü", sayı1**0.5,"'dir")
    
    
    
   
    else:
        print("lütfen geçerli bir sayı giriniz!",)
