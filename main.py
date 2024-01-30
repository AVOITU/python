from palindrome import palindromeObject

def main():

    v_word=input()

    X=palindromeObject(v_word)
    v_word_length=X.f_compt()
    #v_word_length=palindromeObject.f_compt(v_word)
    v_vowels=X.f_vowels()
    #v_vowels=palindromeObject.f_vowels(v_word)

    print (v_word_length)
    print (v_vowels)

    v_palindrome=X.f_word_inv()
    print(v_palindrome)

if __name__ == "__main__":
    main()