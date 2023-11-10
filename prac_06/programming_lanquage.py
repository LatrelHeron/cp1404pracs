"""
Word Occurrences
Estimate: 40 mins
Actual: 60 mins
"""
from prac_06.languages import ProgrammingLanguage


def main():
    """Programming languages"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    for language in languages:
        print(language)


main()
