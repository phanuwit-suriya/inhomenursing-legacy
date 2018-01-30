import os


class Medicine:

    def __init__(self):
        hasdrug, hasfreq, hasamount, hasbefore = True, False, False, False
        f = ['m', 'n', 'e', 'b']
        self.med = False
        self.drugs = {}

        while hasdrug:
            while hasdrug:
                os.system("cls")
                if self.med:
                    self.show()
                drug = input("Drug name   : ")
                if drug == "exit":
                    hasdrug = False
                elif drug == "":
                    pass
                else:
                    hasdrug = False
                    hasfreq = True

            while hasfreq:
                freq = []
                os.system("cls")
                if self.med:
                    self.show()
                print(f"Drug name   : {drug}")
                input_freq = set(input("Frequency   : ").lower())
                if all(c in r"mneb" for c in input_freq):
                    input_freq = sorted(input_freq, key=lambda word: [
                                        f.index(w) for w in word])
                    input_freq = sorted(input_freq, key=lambda char: [
                                        f.index(c) for c in char])
                    for ch in input_freq:
                        if ch == 'm':
                            freq.append('Morning')
                        elif ch == 'n':
                            freq.append('Noon')
                        elif ch == 'e':
                            freq.append('Evening')
                        else:
                            freq.append('Before bedtime')
                    freq = ", ".join(freq)
                    hasfreq = False
                    hasamount = True
                elif input_freq == "":
                    pass

            while hasamount:
                os.system("cls")
                if self.med:
                    self.show()
                print(f"Drug name   : {drug}")
                print(f"Frequency   : {freq}")
                amount = input("Amount      : ")
                if amount.isdigit() and amount != 0:
                    hasamount = False
                    hasbefore = True
                elif amount == "":
                    pass

            while hasbefore:
                os.system("cls")
                if self.med:
                    self.show()
                print(f"Drug name   : {drug}")
                print(f"Frequency   : {freq}")
                print(f"Amount      : {amount}")
                before = input("Before Meal : ").lower()
                if before == "yes" or before == "no":
                    if before == "yes":
                        before = "Yes"
                    else:
                        before = "No"
                    hasbefore = False
                    hasdrug = True
                    self.med = True
                    self.drugs[drug] = [freq, amount, before]
                else:
                    pass

    def add(self):
        pass

    def remove(self):
        self.drugs = {}
        self.med = False
        return("Removed all prescriptions!!!")

    def show(self):
        formatted_text = "{:>15}{:>50}{:>10}{:>15}"
        print('\n', formatted_text.format(
            "Drug name", "Frequency", "Amount", "Before Meal"), '\n')
        if self.med:
            for drug in self.drugs:
                print(formatted_text.format(drug, *self.drugs[drug]), '\n')
