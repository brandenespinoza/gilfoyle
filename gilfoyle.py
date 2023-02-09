import requests
import datetime
import time
import subprocess
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_price():
    url = "https://data.binance.com/api/v3/ticker?symbol=BTCUSDT"
    response = requests.get(url, verify=False)
    current_price = response.json()["lastPrice"]
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
        print("2. HIGHER HIGHS MODE")
        choice=input("Enter your selection (1 or 2): ").lower()
        if choice == '1':
            print("You have selected GILFOYLE MINING MODE. You will be alerted when you should toggle your mining rig on or off.")
            target_price = int(input("Enter BTC Target Price: $"))
            current_price = get_price()
            countdown = "5...4...3...2...1...\n"
            for l in countdown:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(.25)
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
                time.sleep(60)
        elif choice == '2':
            recent_high_price = get_recent_high_price()
            print(f"You have selected HIGHER HIGHS. This will play an alert any time the current Bitcoin price breaks above the 24hr high of ${recent_high_price}.")
            while True:
                current_price = get_price()
                recent_high_price = get_recent_high_price()
                timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                if current_price > recent_high_price:
                    play_music(1.0)
                    print(f"{timestamp}: A New 24hr High!!! Current price of bitcoin is ${current_price}.")
                else:
                    print(f"{timestamp}: Current price of bitcoin is ${current_price}.")
                time.sleep(60) 
        else:
            print("Invalid selection. Please try again.")
if __name__ == "__main__":
    main()