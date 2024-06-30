#Importing the library
import requests

#Getting the response from the api
response = requests.get("https://api.currencyapi.com/v3/latest?apikey=cur_live_net8rRd48e8Q435gpRmK2ouGvencWF1Ci0IeQg7C") #Place your API from 'Currency API'
response.raise_for_status() ##Raising an error if there is status problem
value = response.json() #converting the data into JSON datatype

money_country_data = value["data"] #Extracting the data from the JSon

countries = tuple(money_country_data.keys()) #Getting country codes and making a tuple