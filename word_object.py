class wordObject:
    
    d_vowels=["A","E","I","O","U","Y"]
    
    def f_compt(v_word):
        #compt length
        v_word_length=len(v_word)
        return v_word_length
    
    def f_vowels(v_word,d_vowels):
        #compt vowels in the word
        for letter in v_word:
            for vowel in d_vowels:
                if letter==vowel:
                    v_vowels=v_vowels+1

        return v_vowels


    def f_return_word(v_word):
        v_word=v_word[::-1]

def main(d_vowels):
    v_word=input()
    word_obj=wordObject(v_word)
    v_word_length=wordObject.f_compt(v_word)
    v_vowels=wordObject.f_vowels(v_word, d_vowels)

    print (v_word_length)
    print (v_vowels)

if __name__=="main":
    main()