import os
import gtts

def read_from_file ():
    global words_bank

    result = os.listdir ("homework8")
    print (result)
    if "Translate.txt" in result :
        f = open ("homework8\Translate.txt","r")
        temp = f.read ().split ("\n")
        
    
        words_bank = []
        for i in range (0 , len (temp) , 2) :
            if temp[i] != "" :
                my_dict = {"en" : temp [i] , "fa" : temp [ i+1 ]}
                words_bank.append (my_dict)
               
        f.close()
    else:
        print ("desired database is not exist in this path")
        exit (0)

def show_menu ():
   
    print ("1 : translate english to persian")    
    print ("2 : translate persian to english")
    print ("3 : add new word to database")
    print ("4 : exit")

def translate_en_to_fa () :
    user_text = input ("enter your english text :  ")

    user_words = user_text.split (" ")
    
    output = ""
    for user_word in user_words :
        for word in words_bank :
            if "." in user_word :
                if user_word.replace(".","") == word ["en"] :
                    output = output + word ["fa"] + ". "
                    break
            else :
                if user_word == word ["en"] :
                    output = output + word ["fa"] + " "
                    break
        else :
            output = output + user_word + " "

    print (output)
    x = gtts.gTTS(output,lang = "en" , slow =False) 
    x.save ("homework8/voice1.mp3")
   
def translate_fa_to_en () :
    user_text = input ("enter your persian text :  ")

    user_words = user_text.split (" ")
    
    output = ""
    for user_word in user_words :
        for word in words_bank :
            if "." in user_word :
                if user_word.replace (".","") == word ["fa"] :
                    output = output + word ["en"] + ". "
                    break
            else :
                if user_word == word ["fa"] :
                    output = output + word ["en"] + " "
                    break
        else :
            output = output + user_word + " "

    print (output)
    x = gtts.gTTS(output,lang = "ar" , slow =False) 
    x.save ("homework8/voice2.mp3")


def add_word_to_database () :
    en_word = input ("type english word   ")
    fa_word = input ("type persian word   ")
    new_word = {"en" : en_word , "fa" :fa_word}
    words_bank.append (new_word)

def update_database () :
    f = open ("homework8\Translate.txt","w")

    for word in words_bank :
        line = word ["en"] + "\n"
        f.write (line)
        line = word ["fa"] + "\n"
        f.write (line)

    f.write ("\n")
    f.close ()    

read_from_file ()
print ("Welcome to my translator")
while True:
    show_menu ()

    choice = int (input ("enter your choice:   "))

    if choice == 1 :
        translate_en_to_fa ()
    elif choice == 2 :
        translate_fa_to_en ()
    elif choice == 3 :
        add_word_to_database ()
    elif choice == 4 :
        update_database ()
        exit (0)
    else :
        print ("invalid choice")
        print ("please type the correct choice")



