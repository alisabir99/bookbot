def main(): 
    with open('./books/frankenstein.txt') as f:
        
        # read the contents
        
        file_contents = f.read()

        # count the words

        word_array = file_contents.split()


        # count characters

        my_dict = {}

        for word in word_array:
            for char in word:
                my_dict[char.lower()] = my_dict.get(char.lower(),0) + 1

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(word_array)} words were found in the document")
        print("")

        dic_list = sorted([(frequency,ting) for ting,frequency in my_dict.items()],reverse = True)

        for frequency,ting in dic_list:
            print(f"The {ting} character was found {frequency} times")

        print("")
        print("--- End report ---")



main()


