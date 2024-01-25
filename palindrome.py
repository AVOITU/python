from word_object import wordObject
class palindromeObject(wordObject):

    #function to inverse words and checking if there are palindromic
    def f_word_inv(v_word):
        #inverse word
        v_word_inv=v_word[::-1]
        #checking if inversed word and normal word are the same
        if v_word_inv==v_word:
            v_palindrome=True
        else:
            v_palindrome=False
            
        return v_palindrome

def main():
    v_palindrome=palindromeObject.f_word_inv()
    print(v_palindrome)

if __name__=="__main__":
    main()