import math

# To Make each example function, you need to remove the '#' 

#text
#Number_to_Multiply = input('please enter a number ')
#Number_to_Multiply = float(Number_to_Multiply)

#example 1 
#Amount_to_convert = input('please enter the amount to conver: ')
#Amount_to_convert = float(Amount_to_convert)

#print (Amount_to_convert) 

#example 2:  EUR/USD
#EURUSD = 1.18

#def get_user_input():
    #Amount_to_convert = input('please enter the amount to conver: ')
    #Amount_to_convert = float(Amount_to_convert)
    #return (Amount_to_convert) 
#def convert_currency(rate, amount):
   # converted_amount = amount * rate
    #print (f'EUR amount {amount} converts to {converted_amount} in USD')
    
#eur_amount = get_user_input()
#convert_currency(EURUSD, eur_amount)

#example 3: Adding WHile/loop 
#def prompt_user():
    #prompt = input('Do you wish to convert another figure? Please enter Y or N')
    #return (prompt)

#run_converter = True 

#while run_converter == True:
    #eur_amount = get_user_input()
    #convert_currency(EURUSD, eur_amount)
    #run_again = prompt_user()
    #if run_again == 'N':
        #run_converter = False
        #print ('Thanks for using the converter')

#example 4: Addind a dictionary "currency pairs"
currency_rates = {
    'EURUSD': 1.18,
    'GBPUSD': 1.30,
    'USDJPY': 105.74,
    'GBPEUR': 1.10
}

def get_user_input():
    Currency_pair = input('please provide the currency pair: ')
    Amount_to_convert = input('please enter the amount to convert: ')
    Amount_to_convert = float(Amount_to_convert)
    user_input = [Currency_pair,Amount_to_convert]
    return (user_input)

def convert_currency(currency_pair, amount):
    rate = currency_rates.get(currency_pair)
    converted_amount = amount * rate
    print (f'ccypair was {currency_pair}.  amount {amount} converts to {converted_amount}')
    
def prompt_user():
    prompt = input('Do you wish to convert another figure? Please enter Y or N')
    return (prompt)
    
run_converter = True 
    
while run_converter == True:
    user_input = get_user_input()
    convert_currency(user_input[0], user_input[1])
    run_again = prompt_user()
    if run_again == 'n':
        run_converter = False
        print ('Thanks for using the converter')