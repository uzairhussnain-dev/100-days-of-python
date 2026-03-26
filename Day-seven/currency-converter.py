import requests

def convert_currency():
    print("💱 Currency Converter")
    
    from_currency = input("From (e.g. USD): ").upper()
    to_currency = input("To (e.g. PKR): ").upper()
    amount = float(input("Amount: "))

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if "rates" not in data:
            print("❌ Invalid currency")
            return

        rate = data["rates"].get(to_currency)

        if not rate:
            print("❌ Currency not found")
            return

        result = amount * rate

        print(f"\n💰 {amount} {from_currency} = {result:.2f} {to_currency}")

    except Exception as e:
        print("Error:", e)

convert_currency()