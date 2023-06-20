


author =(
'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Ales Stransky
email: ales.stransky@seznam.cz
discord: Ales S#5138
''')

uzivatele = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]



def vygeneruj_graf(slova, max_delka_slova): 
 
  vyskyty_delek_slov = [] 
  for i in range(max_delka_slova+1):
    vyskyty_delek_slov.append(0)
  
  for i in range(len(slova)):
      vyskyty_delek_slov[ len(slova[i]) ] +=1 
  
  delka_pole_hvezd = max(vyskyty_delek_slov)+2
  print("-" *40)
  print("LEN|" + "OCCURENCES".center(delka_pole_hvezd) + "|NR.")
  print("-" *40)
  
  for i in range(1, len(vyskyty_delek_slov)):
      print(str(i).rjust(3) + "|" + "*"*vyskyty_delek_slov[i] + " "*(delka_pole_hvezd-vyskyty_delek_slov[i]) + "|" +str(vyskyty_delek_slov[i]) )
      



#funkce pro analyzu textu
def analyzuj(text):

  pocet_slov_start_uppercase=0 
  pocet_slov_uppercase=0
  pocet_slov_lowercase=0
  pocet_numeric_strigs=0
  suma=0

  max_delka_slova=0

  slova = text.split()

  for i in range(len(slova)):

      #odstraneni tecky  nebo carky na konci slova:
      slova[i]=slova[i].strip(".,;:")
      #if (slova[i][-1] == ",") or (slova[i][-1] == "."):
      #  slova[i] = slova[i][0:len(slova[i])-1]

      #print(slova[i])
      #print(i)

      if (slova[i][0].isupper() ):
          pocet_slov_start_uppercase += 1 
          #print("**") 
      if ( slova[i].isupper() and slova[i].isalpha()):
          pocet_slov_uppercase +=1
          #print("*")
      if ( slova[i].islower() ):
          pocet_slov_lowercase +=1  
          #print("***") 
      if ( slova[i].isdigit() ):
          pocet_numeric_strigs +=1
          suma +=int(slova[i])
      
      if len(slova[i]) > max_delka_slova :
          max_delka_slova = len(slova[i])



  print(f"There are {len(slova)} words in the selected text.")

  #slova zacinajici velkym pismenem
  print(f"There are {pocet_slov_start_uppercase} titlecase words.")
  print(f"There are {pocet_slov_uppercase} uppercase words.")
  print(f"There are {pocet_slov_lowercase} lowercase words.")
  print(f"There are {pocet_numeric_strigs} numeric strings.")
  print(f"The sum of all the numbers {suma}")

  vygeneruj_graf(slova, max_delka_slova)






def prihlaseni():
    uzivatel= input("username:")
    heslo= input("password:")


    if uzivatele.get(uzivatel) == heslo :
  
        print("-" *40)
        print(f"\nWelcome to the app, {uzivatel}")
        print("We have 3 texts to be analyzed.")
        print("-" *40)

        text_cislo=input("Enter a number btw. 1 and 3 to select:")

        if not( text_cislo.isdigit() ):
            print("Entered input is not number, terminating the program..")
            quit()  #to quit() tam ani byt nemusi

        elif (int(text_cislo) < 1) or (int(text_cislo) > 3):
            print("Entered number is not btw. 1 and 3, terminating the program..")
            quit()  #to quit() tam ani byt nemusi
        else:
            print("-" *40)
            text= TEXTS[int(text_cislo)-1]
            analyzuj(text)

    else:  # heslo nebo uzivatel jsou chybne
        print("unregistered user, terminating the program..")
        quit()  #to quit() tam ani byt nemusi


 
prihlaseni()

#text= TEXTS[0]
#analyzuj(text)
