import wikipedia

SUMMARY_SENTENCES = 2

def main():
    """prompt the user for wikipedia page titles, retrieves and display  page information. """
    titles = prompt_user_for_titles()
    for title in titles:
        page = get_wikipedia_page(title)

    print("Thank you")

def prompt_user_for_titles():
    """Prompt the user for page titles and return them one by one."""
    titles =[]
    title = input("Enter page title :").strip()
    while titles:
        titles.append(title)
        title = input("Enter page title:").strip()
        return titles

def get_wikipedia_page(title):
    """Try to get a wikipedia page for the given title."""
    try:
        return wikipedia.page(title, auto_suggest = False)
    except wikipedia.DisambiguationError as error:
        handle_disambiguation_error(title, error)
    except wikipedia.pageError:
        handle_page_error(title)
    return None

def handle_disambiguation_error(title, error):
    """ Handle wikipedia disambiguation errors by displaying suggested alternatives."""
    print(f'We need a more specific title for "{title}". Try one of the following:')
    for option in error.options:
        print(f"-{option}")

def handle_page_error(title):
    """Handle wikipedia page errors by displaying suggested alternatives."""
    print(f'Page "{title}" does not exist. Please try another search.')

def display_page_info(page):
    """Display the title, a short summary and the url of a wikipedia page."""
    print(f"\n {page.title}")
    print(wikipedia.summary(page.title,sentences = SUMMARY_SENTENCES))
    print(page.url)
