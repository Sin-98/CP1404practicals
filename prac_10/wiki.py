import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    """Main function."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"{page.title}\n{page.summary}\n{page.url}\n")
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        title = input("Enter page title: ").strip()
    print("Thank you.")

main()