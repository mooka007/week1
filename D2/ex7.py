import random


def get_random_temp(season):
   
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(5, 23), 1)
    elif season == "summer":
        return round(random.uniform(18, 40), 1)
    elif season == "autumn":
        return round(random.uniform(5, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1)  
    

def get_season_from_month(month):
    
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    

def main():
        month= int(input("Enter the month(1 - 12): "))
        season = get_season_from_month(month)
        temp = get_random_temp(season)
        print(f"The temperature in {season} is {temp} degrees")

        if temp < 0:
            print("It's freezing! Better grab a scarf!")
        elif 0 <= temp <= 16:
            print("It's quite chilly. Better wear a light jacket!")
        elif 16 <= temp <= 23:
            print("It's a lovely day! The sun is shining and the temperature is just right.")
        elif 23 <= temp <= 32:
            print("It's getting warm! Better wear a light sweater!")
        else:
            print("It's hot! Better wear shorts and a t-shirt!")
        

main()