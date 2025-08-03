import wikipedia

SUMMARY_SENTENCES = 2

def main():
    """prompt the user for wikipedia page titles, retrieves and display  page information. """
    titles = prompt_user_for_titles()


def prompt_user_for_titles():
    """Prompt the user for page titles and return them one by one."""
    titles =[]
    title = input("Enter page title :").strip()
    while titles:
        titles.append(title)
        title = input("Enter page title:").strip()
        return titles

