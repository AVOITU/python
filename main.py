from word_object import wordObject
from palindrome import palindromeObject

def main():

    v_word=input()

    
    v_word_length=wordObject.f_compt(v_word)
    v_vowels=wordObject.f_vowels(v_word)

    print (v_word_length)
    print (v_vowels)

    v_palindrome=palindromeObject.f_word_inv(v_word)
    print(v_palindrome)

if __name__ == "__main__":
    main()