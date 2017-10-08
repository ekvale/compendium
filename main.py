import time


def user_time():
    with open(r"EnglishStopWords.txt", 'r') as deleting:
        dele = deleting.read().split()

    userinput = input("Enter file name: ")
    with open(userinput, 'r') as infile:
        fin = infile.read().split()

    outfile = "users_file.txt"
    fout = open(outfile, "w+")
    dele = [element.lower() for element in dele]
    dele = [dele]
    fin = [element.lower() for element in fin]
    fin = [fin]

    final = [x for x in fin[0] if x not in dele[0]]
    final = [y for y in final if y.isalpha()]
    wordcount = {}
    for word in final:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    l4 = sorted(wordcount, key=wordcount.get, reverse=True)
    print("The word that occured the most times is: ", l4[0], """\n 
    A copy of the compendium has been saved to address_file.txt. Thank You.""")
    time.sleep(2)
    for k, v, in wordcount.items():
        num = v
        fout.write("{:<15}, {:<15} \n".format(k, num))
        print("{:<15}, {:<15}".format(k, num))

    final = str(final)
    fout.write(final)
    deleting.close()
    infile.close()
    fout.close()
    main()


def main():
    print("Welcome to the Compendium")
    print("Press 1. To enter the name of the file you wish to search.")
    print("Press 2. To Quit")
    choice = input("")
    if choice == "1":
        user_time()
    else:
        quit()


main()
