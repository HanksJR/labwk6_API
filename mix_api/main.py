import requests
import os
import urllib.request

def return_currency(country):
    url = "https://restcountries.eu/rest/v2/name/{}".format(country)
    response = requests.get(url)
    resp = response.json()[0]["currencies"][0]["code"]
    return resp

def exchange(currencies):
    url = "https://api.exchangeratesapi.io/latest"
    response = requests.get(url)
    resp = response.json()["rates"][currencies]
    return resp

def time():
    url = "http://worldtimeapi.org/api/ip/"
    response = requests.get(url).json()
    time = response["datetime"]
    current = [time[:4],time[5:7],time[8:10],time[10],time[11:19]]
    return current

def main():
    country = input()
    currencies = exchange(return_currency(country))
    allt = time()
    year = allt[0]
    month = allt[1]
    days = allt[2]
    day = allt[3]
    times = allt[4]
    check = {"S":"Sunday","M":"Monday", "T":"Tuesday", "W":"Wednesday", "Th":"Thursday", "F":"Friday", "Sat":"Saturday"}
    print("{} exchange rates base on EUR is {}".format(country, currencies))
    print("Your location current time is {} {} {} {} {}".format(check[day], days, month, year, times))

main()
