import csv
from collections import Counter, defaultdict

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as data_csv:
            csv_reader = csv.DictReader(data_csv)
            for line in csv_reader:
                data.append(line)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    return data

def highest_price(data):
    diamond_prices = [float(diamond['price']) for diamond in data]
    return max(diamond_prices)

def average_price(data):
    diamond_prices = [float(diamond['price']) for diamond in data]
    return sum(diamond_prices) / len(diamond_prices)

def count_ideal_cut_diamonds(data):
    return sum(1 for diamond in data if diamond['cut'] == 'Ideal')

def color_diamonds(data):
    return Counter(diamond['color'] for diamond in data)

def median_carat_premium(file_path):
    premium_carats = []

    try:
        with open(file_path, 'r', encoding='utf-8') as data_csv:
            csv_reader = csv.DictReader(data_csv)
            
            for line in csv_reader:
                if line['cut'] == 'Premium':  # Ensure the value in the "cut" column is "Premium"
                    premium_carats.append(float(line['carat']))
        
        # Sort the list of premium diamond carats
        premium_carats.sort()
        
        # Calculate the median
        n = len(premium_carats)
        if n % 2 == 0:
            median_carat = (premium_carats[n//2 - 1] + premium_carats[n//2]) / 2
        else:
            median_carat = premium_carats[n//2]
        
        return median_carat

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)

def average_carat_by_cut(data):
    carats_by_cut = defaultdict(list)
    
    for diamond in data:
        cut = diamond['cut']
        carat = float(diamond['carat'])
        carats_by_cut[cut].append(carat)
    
    average_carats = {}
    for cut, carats in carats_by_cut.items():
        average_carats[cut] = sum(carats) / len(carats)
    
    return average_carats

def average_price_by_color(data):
    prices_by_color = defaultdict(list)
    
    for diamond in data:
        color = diamond['color']
        price = float(diamond['price'])
        prices_by_color[color].append(price)
    
    average_prices = {}
    for color, prices in prices_by_color.items():
        average_prices[color] = sum(prices) / len(prices)
    
    return average_prices

def main():
    file_path = input("Enter the path to your CSV file: ")
    data = read_csv(file_path)

    if data:
        while True:
            print("\nOptions:")
            print("1. Find the highest price")
            print("2. Calculate the average price")
            print("3. Count the number of diamonds with an ideal cut")
            print("4. List unique diamond colors")
            print("5. Calculate the median carat of diamonds with 'Premium' cut")
            print("6. Calculate the average carat for each cut")
            print("7. Calculate the average price for each color")
            print("8. Quit")

            choice = input("Choose an option (1/2/3/4/5/6/7/8): ")

            if choice == '1':
                print("The highest price of a diamond is: ", highest_price(data))
            elif choice == '2':
                print("The average price of a diamond is: ", average_price(data))
            elif choice == '3':
                print("The number of diamonds with an ideal cut is: ", count_ideal_cut_diamonds(data))
            elif choice == '4':
                colors = color_diamonds(data)
                print("Number of different diamond colors:", len(colors))
                print("The diamond colors are:", ', '.join(colors.keys()))
            elif choice == '5':
                median_carat = median_carat_premium(file_path)
                if median_carat is not None:
                    print("The median carat of diamonds with 'Premium' cut is:", median_carat)
            elif choice == '6':
                average_carats = average_carat_by_cut(data)
                for cut, average_carat in average_carats.items():
                    print(f"The average carat for '{cut}' cut is: {average_carat}")
            elif choice == '7':
                average_prices = average_price_by_color(data)
                for color, average_price in average_prices.items():
                    print(f"The average price for '{color}' diamonds is: {average_price}")
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1, 2, 3, 4, 5, 6, 7, or 8")

if __name__ == "__main__":
    main()