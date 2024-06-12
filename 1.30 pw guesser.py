"""conditionals and strings password generator"""
"""second edition is change it to have it let you try unclimited times until you get a usablue one"""

poss_pw : str = input("Please put in your desired password.")
bad_pw : bool = True

while bad_pw:
    if len(poss_pw) >= 6: 
        if len(poss_pw) <= 16:   
            if "$" not in poss_pw and "#" not in poss_pw and "@" not in poss_pw:
                print("That is not a good password.")
                poss_pw = input("Please put in your desired password.")
            elif "$" in poss_pw or "#" in poss_pw or "@" in poss_pw: 
                print("Good password!")
                bad_pw = False
    if len(poss_pw) < 6:
        print("That is not long enough. ")
        poss_pw = input("Please put in your desired password.")
    if len(poss_pw) > 16:
        print("That is too long. ")
        poss_pw = input("Please put in your desired password.")
