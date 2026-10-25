
import re

FAQS = {
    "hours": "Our support hours are Monday to Friday, 9 AM to 5 PM.",
    "price": "Please check the product page for current pricing.",
    "contact": "You can contact support by email.",
    "python": "Python is a programming language used for automation, web development and AI."
}


def get_response(message):
    message = message.lower().strip()

    if re.search(r"\b(bye|exit|quit)\b", message):
        return "Goodbye! Have a great day!"

    if re.search(r"\b(hi|hello|hey)\b", message):
        return "Hello! How can I help you today?"

    if "hour" in message or "time" in message:
        return FAQS["hours"]

    if "price" in message or "cost" in message:
        return FAQS["price"]

    if "contact" in message or "email" in message:
        return FAQS["contact"]

    if "python" in message:
        return FAQS["python"]

    return (
        "Sorry, I didn't understand. "
        "Ask about hours, price, contact or Python."
    )


def main():
    print("Welcome to the Python Assistant!")
    print("Type 'bye', 'exit' or 'quit' to stop.")

    while True:
        message = input("You: ")
        response = get_response(message)
        print("Bot:", response)

        if re.search(r"\b(bye|exit|quit)\b", message.lower()):
            break


if __name__ == "__main__":
    main()
