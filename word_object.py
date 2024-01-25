d_vowels=["A","E","I","O","U","Y","a","e","i","o","u","y"]
class wordObject:
    
    def f_compt(v_word):
        #compt length
        v_word_length=len(v_word)
        return v_word_length
    
    def f_vowels(v_word,d_vowels):
        #compt vowels in the word
        v_vowels=0
        for letter in v_word:
            for vowel in d_vowels:
                if letter==vowel:
                    v_vowels=v_vowels+1


        return v_vowels


    def f_return_word(v_word):
        v_word=v_word[::-1]

def main():
    v_word=input()
    v_word_length=wordObject.f_compt(v_word)
    v_vowels=wordObject.f_vowels(v_word, d_vowels)

    print (v_word_length)
    print (v_vowels)

if __name__ == "__main__":
    main()