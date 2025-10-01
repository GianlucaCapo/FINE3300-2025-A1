# FINE3300 – Assignment 1
# Part 2: ExchangeRates class

import csv

class ExchangeRates:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.rate_usd_cad = None  # CAD per 1 USD (USD/CAD)

        self._load_latest_rate()

    def _load_latest_rate(self):
        with open(self.csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            rows = list(reader)
            if not rows:
                raise ValueError("CSV is empty.")

            header = rows[0]
            # Try to find the column that corresponds to USD/CAD (case-insensitive)
            usd_cad_idx = None
            for i, name in enumerate(header):
                if "USD/CAD" in name.upper().replace(" ", ""):
                    usd_cad_idx = i
                    break
            if usd_cad_idx is None:
                raise ValueError("Could not find USD/CAD column in the CSV header.")

            # Latest rate = last non-empty row
            for row in reversed(rows[1:]):
                cell = row[usd_cad_idx].strip()
                if cell != "":
                    self.rate_usd_cad = float(cell)
                    break

            if self.rate_usd_cad is None:
                raise ValueError("No USD/CAD rate found in data rows.")

    def convert(self, amount, from_currency, to_currency):
        """
        from_currency/to_currency: 'USD' or 'CAD'
        USD->CAD: amount * (USD/CAD rate)
        CAD->USD: amount / (USD/CAD rate)
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate_usd_cad
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate_usd_cad
        else:
            # Either same currency or unsupported
            return amount

if __name__ == "__main__":
    path = input("Enter path to BankOfCanadaExchangeRates.csv: ")
    er = ExchangeRates(path)

    amt = float(input("Enter amount (e.g., 100000): "))
    from_ccy = input("From currency (USD or CAD): ")
    to_ccy = input("To currency (USD or CAD): ")

    result = er.convert(amt, from_ccy, to_ccy)
    print("Converted Amount: ${:.2f} {}".format(result, to_ccy.upper()))
