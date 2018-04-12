'''description: This program takes user two words or numbers from the user input
and compares them in length if they are words, or compares them in value if they
are numbers. The longer word, or larger value is then described in the output.'''

#compares word lengths
def word_length(word1, word2):
    if len(word1) > len(word2):
        return word1
    elif len(word1) < len(word2):
        return word2
    else:
        return "The words are similar in length"

#compares number values
def num_info(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "The numbers are the same"


def main():

    words = input("Enter two words or two numbers seperated by a space: ")
    words = words.split()
    
    if (words[0].isdigit()) and (words[1].isdigit):
        info = num_info(words[0], words[1])
        print("\n", "Between the two numbers you entered,", info, "is the larger number")

    else:
        info = word_length(words[0], words[1])
        print("\n","Between the two words you entered,", info, "is the longer word")
    
    print("\n","\n")
    print("    0         0   ")
    print()
    print("         U")
    print(" *               *")
    print("  *            *")
    print("    *        *")
    print("       *  *")
    
   

main()
