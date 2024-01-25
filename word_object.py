class wordObject:
    
    d_vowels=["a","e","i","o","u","y"]
    
    def __init__(self,v_word) -> None:
         #intanciate? and transform v_word into lowers caracters ignore
         v_word=v_word.lower()
         pass
    
    def f_compt(v_word):
        #compt length
        v_word_length=len(v_word)
        return v_word_length
    
    def f_vowels(v_word,d_vowels):
        #compt vowels in the word
        v_vowels=0
        for letter in v_word:
            if letter in wordObject.d_vowels:
                    v_vowels=v_vowels+1

        return v_vowels

def main():

    v_word=input()
    v_word_length=wordObject.f_compt(v_word)
    v_vowels=wordObject.f_vowels(v_word, wordObject.d_vowels)

    print (v_word_length)
    print (v_vowels)

if __name__ == "__main__":
    main()