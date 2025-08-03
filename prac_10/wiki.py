import wikipedia

SUMMARY_SENTENCES = 2

def main():
    """prompt the user for wikipedia page titles, retrieves and display  page information. """
    titles = prompt_user_for_titles()
    for title in titles:
        page = get_wikipedia_page(title)

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
    except wikipedia.DisambiguationError as e:
        handle_disambigution_error(title, e)
    except wikipedia.pageError:
        handle_page_error(title)
    return None

