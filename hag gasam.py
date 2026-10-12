import random as ra
mok = ["mokeb:geteh|1", "mokeb:geteh|2", "mokeb:geteh|3", "mokeb:geteh|4", "mokeb:geteh|5", "mokeb:geteh|6", "mokeb:geteh|7", "mokeb:geteh|8", "mokeb:geteh|9", "mokeb:geteh|10", "mokeb:geteh|11", "mokeb:geteh|12", "mokeb:geteh|13, ""mokeb:geteh|14", "mokeb:geteh|15", "mokeb:geteh|16", "mokeb:geteh|17", "mokeb:geteh|18", "mokeb:geteh|19", "mokeb:geteh|20"]
nok = ["st.sahda khanok|kocheh 17|home dovm", "st.gahade|kocheh 20|home 8", "st.sarbaz|kocheh 9|home 5"]
def dadan():
    with open("yadvarh.txt", "r") as f:
        content = f.read()
        if content:
            print(content)
def sabtenam():
    ali = input("What is your name >> ")
    parsa = input("What is your last name >> ")
    with open("salgard.txt", "a") as f:
        f.write(ali + "|" + parsa + "|sabtenam|\n")
    print("Sabtenam angam shode")
def gerfatan():
    aa = input("What is your name and last name >> ")
    mokeb = ra.choice(mok)
    print(mokeb)
    with open("salgard.txt", "a", encoding="utf-8") as f:
        f.write(aa + "|" + mokeb + "|" + "\n")
def eskan():
    while True:
        print("1. Eskan dadan")
        print("2. Eskan gerftan")
        lk = input("What is your number >> ")
        if lk == "1":
            gv = input("What is your name and last name >> ")
            bn = input("What is your makan >> ")
            with open("yadvarh.txt", "a", encoding="utf-8") as f:
                f.write(gv + "|" + bn + "|eskan dadan| +\n")
            print("Information saved.")
        elif lk == "2":
            par = ra.choice(nok)
            ga = input("What is your name and last name >> ")
            print(par)
            with open("yadvarh.txt", "a", encoding="utf-8") as f:
                f.write(ga + "|eskan gerftan|" + par + "\n")
def main():
    while True:
        print("\n1. Dedan khatete as sahed")
        print("2. Gerftan mokeb")
        print("3. Eskan shaer")
        print("4. Sabtenam")
        print("5. Exit")
        xa = input("What is your number >> ")
        if xa == "1":
            dadan()
        elif xa == "2":
            gerfatan()
        elif xa == "3":
            eskan()
        elif xa == "4":
            sabtenam()
        elif xa == "5":
            print("Goodbye!")
            break
        else:
            print("eshtabh")
main()