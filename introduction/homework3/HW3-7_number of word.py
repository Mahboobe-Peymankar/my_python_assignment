sentence = input ( " please write a sentence or phrase ..." )
len_sntence = len ( sentence )
no_word = 0
for i in range ( len_sntence ) :
    if " " in sentence [ i ] :
        no_word += 1
print ( "Nomber of words in this sentence = ", no_word + 1)        
