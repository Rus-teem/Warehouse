"""Совместимый запуск фильтрации поисковых запросов."""

from combining_words import phrases, words
from keyword_filter import filter_phrases


def main():
    """Печатает отфильтрованные фразы."""
    print(filter_phrases(phrases, words))


if __name__ == "__main__":
    main()
