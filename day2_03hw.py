#BUILD A USD CURRENCY CONVERTER . USER ENTERS AN AMOUNT IN USD. PRINT 
#THE EQUIVALENT IN NRS , EUR AND GBP.
# USE ALL_CAPS FOR YOUR EXCHANGE RATE CONSTANTS. FORMAT THE OUTPUT WITH COMMA SEPARATORS AND 2 DECIMAL PLACES
#$1 USD NPR 154.66. , $1 USD €0.86 EUR. , $1 USD £0.74 GBP

'''usd=float(input("Enter usd dollars needed to convert:"))
CONVNPR=usd * 154.66
CONVEUR=usd * 0.86
CONVGBP=usd * 0.74
print(f"The equivalent NPR is {CONVNPR:,.2f}")
print(f"The equivalent EUR is {CONVEUR:,.2f}")
print(f"The equivalent GBP is {CONVGBP:,.2f}") '''

def npr(us_dollar,npr_exchangerate):
    conv_npr=us_dollar * npr_exchangerate
    print(f"The equivalent NPR is {conv_npr:,.2f}")
def eur(us_dollar,eur_exchangerate):
    conv_eur=us_dollar * eur_exchangerate
    print(f"The equivalent EUR is {conv_eur:,.2f}")
def gbp(us_dollar,gbp_exchangerate):
    conv_gbp=us_dollar * gbp_exchangerate
    print(f"The equivalent GBP is {conv_gbp:,.2f}")

us_dollar=float(input("Enter the dollar you want to convert:"))
npr_exchangerate= 154.66
eur_exchangerate= 0.86
gbp_exchangerate= 0.74
choice=input("Enter NPR if you want to convert it into NPR or EUR if you want to convert it into EUR or GBP if you want to convert it into GBP/n:")
if choice.lower()== "npr":
    npr(us_dollar,npr_exchangerate)
elif choice.lower() == "eur":
    eur(us_dollar,eur_exchangerate)
elif choice.lower() == "gbp":
    gbp(us_dollar,gbp_exchangerate)
else:
    print("invalid option")






