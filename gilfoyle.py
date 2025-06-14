import requests
import datetime
import time
import subprocess
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_price():
    url = "https://data.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url, verify=False)
    current_price = response.json()["price"]
    return int(float(current_price))

def get_recent_high_price():
    url = "https://data.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
    response = requests.get(url, verify=False)
    recent_high_price = response.json()["highPrice"]
    return int(float(recent_high_price))

def play_music1(volume):
    subprocess.run(["afplay", "-v", str(volume), "youSuffer.mp3"])

def play_music2(volume):
    subprocess.run(["afplay", "-v", str(volume), "youSuffer.mp3"])

def main():
    while True:
        print("Select a mode:")
        print("1. GILFOYLE MODE")
        print("2. JERRY GARCIA MODE")
        choice=input("Enter your selection (1 or 2): ").lower()
        if choice == '1':
            print("----- STARTING GILFOYLE MINING MODE -----")
            target_price = int(input("Enter BTC Target Price: $"))
            polling_frequency = int(input("Enter the Polling Frequency (Seconds): "))
            current_price = get_price()
            countdown = "Loading Data...\n"
            for l in countdown:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(.331)
            while True:
                last_price = current_price 
                current_price = get_price()
                timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                print(f"{timestamp}: Current price of bitcoin is ${current_price}.")
                if current_price > target_price and last_price <= target_price:
                    play_music1(1.0)
                    print(f"Bitcoin just broke above your price ceiling.  Time to toggle on your miners.")
                elif current_price < target_price and last_price >= target_price:
                    play_music2(1.0)
                    print(f"Bitcoin just fell below your price target.  Time to toggle off your miners.")
                time.sleep(polling_frequency)
        elif choice == '2':
            recent_high_price = get_recent_high_price()
            print("----- STARTING JERRY GARCIA MODE -----")
            polling_frequency = int(input("Enter the Polling Frequency (Seconds): "))
            while True:
                current_price = get_price()
                recent_high_price = get_recent_high_price()
                timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                if current_price > recent_high_price:
                    play_music1(1.0)
                    print(f"{timestamp}: A New 24hr High!!! Current price of bitcoin is ${current_price}.")
                else:
                    print(f"{timestamp}: Current price of bitcoin is ${current_price} compared to the 24hr High of ${recent_high_price}.")
                time.sleep(polling_frequency)
        else:
            print("Invalid selection. Please try again.")
if __name__ == "__main__":
    main()
