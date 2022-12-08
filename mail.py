def main() :

    mail = input(" Enter mail: ")
    
    k = 0
    j = 0
    d = 0

    if len(mail) >= 6 :
        
        if mail[0].isalpha() :

            if ("@" in mail) and mail.count("@") == 1 :

                if ( mail[-4] == "." ) ^ ( mail[-3] == "." ) :

                    for letter in mail :
                        
                        if letter == letter.isspace() :
                            k = 1
                        
                        if letter.isalpha() :
                            if letter == letter.upper() :
                                j = 1
                        
                        if letter.isdigit() :
                            continue

                        if letter == "." or letter == "@" or letter == "_" :
                            continue
                        else :
                            d = 1

                    if j == 1 or k == 1 or d == 1 :
                        print("mail invalid")

            else :
                print("mail invalid")
    else :
        print("Mail Invalid")            



if __name__ == "__main__" :
    main()