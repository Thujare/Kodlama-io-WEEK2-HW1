"""
ÖDEV TANIMI:

Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

*Aldığı isim soy isim ile listeye öğrenci ekleyen
*Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
*Listeye birden fazla öğrenci eklemeyi mümkün kılan
*Listedeki tüm öğrencileri tek tek ekrana yazdıran
*Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
*Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
*fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
"""

########################## STUDENT REGISTRATION SYSTEM FUNCTIONS ##########################

studentList = []

def addStudents():
    print("########## ÖĞRENCİ KAYIT EKLEME ##########")
    studentName = input("Lütfen kayıt olacak öğrencinin ismini giriniz: ")
    studentSurname = input("Lütfen kayıt olacak öğrencinin soy ismini giriniz: ")
    studentNameAndSurname = studentName + " " + studentSurname
    studentList.append(studentNameAndSurname)
    print("{} Başarılı kayıt! => ".format(studentNameAndSurname))

def removeStudents():
    print("########## ÖĞRENCİ KAYIT SİLME ##########")
    removeName = input("Kaydı silinecek öğrencinin ismini giriniz: ")
    removeSurname = input("Kaydı silinecek öğrencinin soy ismini giriniz: ")
    removeStudentNameAndSurname = removeName + " " + removeSurname
    studentList.remove(removeStudentNameAndSurname)

def addMultipleStudents():
    print("########## ÇOKLU ÖĞRENCİ KAYIT EKLEME ##########")
    numberOfStudentsToAdd = int(input("Kaydı yapılacak öğrenci sayısını giriniz: "))
    for i in range(numberOfStudentsToAdd):
        addStudents()

def MultipleStudentDelete():
    print("########## ÇOKLU KAYIT SİLME MENÜSÜ ##########")
    i = 0
    NumberOfStudentsToBeDeleted = int(input("Lütfen kaydı silinecek öğrenci sayısını giriniz: "))
    while(i <= NumberOfStudentsToBeDeleted):
        i += 1
        deletedStudentNumber = int(input("Lütfen kaydı silinecek öğrencilerin numaralarını giriniz: "))
        studentList.remove(deletedStudentNumber)

def studentsList():
    print("########## ÖĞRENCİ LİSTESİ MENÜSÜ ##########")
    if(len(studentList) == 0):
        print("Hiç öğrenci bulunmamaktadır!")
    
    else:
        for i in studentList:
            print(i)

def studentNumber():
    print("########## ÖĞRENCİ NUMARASI ARATMA MENÜSÜ ##########")
    searchForStudents = input("Lütfen aratmak istediğiniz öğrencinin ismini ve soy ismini giriniz: ")
    for i in range (len(studentList)):
        if studentList[i] == studentNumber:
            print(i)

########################## MENU SYSTEM ##########################

print("""
#######################################################################################
Öğrenci kayıt sistemine hoş geldiniz. Lütfen yapmak istediğiniz işlemi seçiniz.

1 => ÖĞRENCİ KAYIT EKLEME MENÜSÜ

2 => ÖĞRENCİ KAYIT SİLME MENÜSÜ

3 => ÇOKLU KAYIT EKLEME MENÜSÜ

4 => ÇOKLU KAYIT SİLME MENÜSÜ

5 => ÖĞRENCİ LİSTESİ MENÜSÜ

6 => ÖĞRENCİ NUMARASI ARATMA MENÜSÜ

Öğrenci kayıt sisteminden çıkış yapmak için lütfen " q " tuşuna basınız.
#######################################################################################
""")

while True:
    process = input("Lütfen görmek istediğiniz işlemi numara girerek seçiniz :")

    if (process == "1"):
        addStudents()
    
    elif (process == "2"):
        removeStudents()

    elif (process == "3"):
        addMultipleStudents()

    elif (process == "4"):
        MultipleStudentDelete()

    elif (process == "5"):
        studentsList()

    elif (process == "6"):
        studentNumber()

    elif (process == "q"):
        print("İyi günler <3 ")
        break

    else:
        print("Hatalı bir işlem gerçekleştirdiniz. ")
