"""
Languages.py
Estimate : 30 minutes
Actual  total 2 files times: 50 minutes
"""

from programming_languages import ProgrammingLanguages

def main():
    """ demonstrating the programming languages. """
    java_language = ProgrammingLanguages("Java language", "Static",True, 1995)
    double_plus_language = ProgrammingLanguages("C++ language", "Static", False, 1983)
    python = ProgrammingLanguages("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguages ("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguages ("Visual Basic", "Static", False,1991 )

    print(python)

    languages = [java_language, double_plus_language, python, ruby, visual_basic]

    print ("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print (language)


main()

