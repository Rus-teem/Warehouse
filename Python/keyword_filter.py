"""Фильтрация поисковых запросов по стоп-словам."""


def filter_phrases(phrases, stop_words):
    """Возвращает фразы, не содержащие ни одного стоп-слова."""
    stop_words_lower = [word.lower() for word in stop_words]
    result = []

    for phrase in phrases:
        phrase_lower = phrase.lower()
        if not any(word in phrase_lower for word in stop_words_lower):
            result.append(phrase)

    return result
