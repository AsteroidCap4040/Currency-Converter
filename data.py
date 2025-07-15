#Importing the library
import requests

#Getting the response from the api
response = requests.get("") #Place your API from 'Currency API'
response.raise_for_status() ##Raising an error if there is status problem
value = response.json() #converting the data into JSON datatype

money_country_data = value["data"] #Extracting the data from the JSon

countries = tuple(money_country_data.keys()) #Getting country codes and making a tuple
