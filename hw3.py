class CreditCardPayment:
    def __init__(self, currency: str):
        self.currency = currency

    def pay(self, amount: float):
        print(f"Оплата карткою {amount}{self.currency}")


class PayPalPayment:
    def __init__(self, currency: str):
        self.currency = currency

    def pay(self, amount: float):
        print(f"Оплата PayPal {amount}{self.currency}")


class CryptoPayment:
    def __init__(self, currency: str):
        self.currency = currency

    def pay(self, amount: float):
        print(f"Оплата криптогаманцем {amount}{self.currency}")


def create_payment():
    payment_type = input("Оберіть тип оплати (card/paypal/crypto): ").strip().lower()

    currency = input("Введіть валюту (наприклад, USD або ₴): ").strip()

    if payment_type == "card":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        raise ValueError("Невідомий тип оплати!")


payments_list = []

try:
    for i in range(3):
        print(f"\nНалаштування платежу №{i + 1}:")
        payment_obj = create_payment()
        payments_list.append(payment_obj)

    print("\n--- Процес оплати ---")
    for payment in payments_list:
        amount_to_pay = float(input(f"Введіть суму для {type(payment).__name__}: "))
        payment.pay(amount_to_pay)

except ValueError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Сталася помилка: {e}")
