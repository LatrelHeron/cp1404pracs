import wikipedia


def main():
    user_input = input("Title/Phrase: ").title()
    while user_input != "":
        get_wikipedia_summary(user_input)
        user_input = input("Title/Phrase: ").title()
    print("Thank you for using wiki")


def get_wikipedia_summary(title):
    try:
        page = wikipedia.page(title, autosuggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.PageError:
        print("Page not found.")


main()
