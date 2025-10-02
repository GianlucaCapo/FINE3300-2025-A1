# FINE3300 – Assignment 1
# Part 2: ExchangeRates class

import csv
#Imports the csv module to handle CSV file operations

class ExchangeRates: #Defines a new class
    def __init__(self, csv_path="BankOfCanadaExchangeRates.csv"):
        self.csv_path = csv_path
        self.rate_usd_cad = None
        self._load_latest_rate()
        #Constructor method to initialize the class.
        #Sets the path to the CSV file in repository and initializes the USD/CAD rate.

    def _load_latest_rate(self):
        with open(self.csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            #Read all rows to find the latest non-empty USD/CAD rate

            rows = list(reader)
            if not rows:
                raise ValueError("CSV is empty.")
            #Ensure the CSV is not empty

            header = rows[0]
            usd_cad_idx = None
            for i, name in enumerate(header):
                if "USD/CAD" in name.upper().replace(" ", ""):
                    usd_cad_idx = i
                    break
            if usd_cad_idx is None:
                raise ValueError("Could not find USD/CAD column in the CSV header.")
            #Find the index of the USD/CAD column in the header
            #Read rows in reverse to find the latest non-empty USD/CAD rate
            #Handle potential empty cells

            for row in reversed(rows[1:]):
                cell = row[usd_cad_idx].strip()
                if cell != "":
                    self.rate_usd_cad = float(cell)
                    break
            #Last non-empty USD/CAD rate found in the CSV

            if self.rate_usd_cad is None:
                raise ValueError("No USD/CAD rate found in data rows.")
            #Raise an error if no valid rate is found

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        #Convert currencies based on the loaded USD/CAD rate

        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate_usd_cad
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate_usd_cad
        else:
            return amount
        #If converting from USD to CAD, multiply by the rate
        #If converting from CAD to USD, divide by the rate
        #If currencies are the same or unsupported, return the original amount

if __name__ == "__main__":
    er = ExchangeRates()
    #Create an instance of ExchangeRates

    amt = float(input("Enter amount to convert (ex. 150000): "))
    from_ccy = input("From currency (USD or CAD): ")
    to_ccy = input("To currency (USD or CAD): ")
    #User input for amount and currencies

    result = er.convert(amt, from_ccy, to_ccy)
    print("Converted Amount: ${:.2f} {}".format(result, to_ccy.upper()))
    #Perform a conversion based on user input
    #Print the converted amount formatted to the nearest cent
