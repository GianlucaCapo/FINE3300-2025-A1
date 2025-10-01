# FINE3300 – Assignment 1
# Part 1: MortgagePayment class

class MortgagePayment: #Defines a new class
    def __init__(self, quoted_rate_percent, years):
        self.j2 = quoted_rate_percent / 100.0 
        self.years = int(years)
    #Constructor method to initialize the class.
    #Convert interest rate from percentage to decimal.
    #Ensure years is an integer

    def _effective_annual_rate(self): 
        return (1 + self.j2 / 2) ** 2 - 1 
    #Defines a helper method to calculate the effective annual rate

    def _periodic_rate(self, payments_per_year):
        i_eff = self._effective_annual_rate()
        return (1 + i_eff) ** (1 / payments_per_year) - 1
    #Defines a helper method to calculate the periodic interest rate 
    #based on the number of payments per year

    def _annuity_factor(self, r, n):
        return (1 - (1 + r) ** (-n)) / r
    #Defines a helper method to calculate the present value of an annuity 
    #factor based on the periodic rate and number of payments

    def payments(self, principal):
        m_month = 12
        m_semimonth = 24
        m_biweekly = 26
        m_weekly = 52
        #Defines payment frequencies

        r_month = self._periodic_rate(m_month)
        r_semimonth = self._periodic_rate(m_semimonth)
        r_biweekly = self._periodic_rate(m_biweekly)
        r_weekly = self._periodic_rate(m_weekly)
        #Calculates periodic interest rates for each payment frequency

        n_month = self.years * m_month
        n_semimonth = self.years * m_semimonth
        n_biweekly = self.years * m_biweekly
        n_weekly = self.years * m_weekly
        #Calculates total number of payments for each payment frequency

        monthly = principal / self._annuity_factor(r_month, n_month)
        semi_monthly = principal / self._annuity_factor(r_semimonth, n_semimonth)
        bi_weekly = principal / self._annuity_factor(r_biweekly, n_biweekly)
        weekly = principal / self._annuity_factor(r_weekly, n_weekly)
        #Calculates the standard annuity payment for each payment frequency (Principal/PVA(r,n))

        rapid_biweekly = monthly / 2
        rapid_weekly = monthly / 4
        #Calculates the accelerated payment amounts based on the monthly payment

        return (monthly, semi_monthly, bi_weekly, weekly, rapid_biweekly, rapid_weekly)
        #Returns a tuple containing all calculated payment amounts

if __name__ == "__main__":
    principal = float(input("Enter principal amount (no commas, ex. 250000): "))
    rate = float(input("Enter quoted annual rate (percent value, ex. 3.5): "))
    years = int(input("Enter amortization period in years (ex. 20): "))
    #Collect user inputs for principal, interest rate, and amortization period
    #Assumes valid inputs from users

    mp = MortgagePayment(rate, years)
    p = mp.payments(principal)
    #Creates an instance of the MortgagePayment class and calculates payments

    print("Monthly Payment: ${:.2f}".format(p[0]))
    print("Semi-monthly Payment: ${:.2f}".format(p[1]))
    print("Bi-weekly Payment: ${:.2f}".format(p[2]))
    print("Weekly Payment: ${:.2f}".format(p[3]))
    print("Rapid Bi-weekly Payment: ${:.2f}".format(p[4]))
    print("Rapid Weekly Payment: ${:.2f}".format(p[5]))
    #Prints the calculated payment amounts formatted to the nearest cent
    