class wordObject:
    
    d_vowels=["a","e","i","o","u","y"]
    
    def __init__(self,v_word) -> None:
         #transform v_word into lowers caracters ignore
         self.v_word=v_word.lower()
    
    def f_compt(self):
        #compt length of the word
        return len(self.v_word)
    
    def f_vowels(self):
        #compt vowels in the word
        v_vowels=0
        for letter in self.v_word:
            if letter in wordObject.d_vowels:
                    v_vowels=v_vowels+1
        return v_vowels
    
#Test
#v_word=input()
#X=wordObject("v_word")
#v_word_length=X.__f_compt()
#v_vowels=X.f_vowels()

#print(v_word_length)
#print(v_vowels)