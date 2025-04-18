from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

# Ваши запросы (пример)
queries = [
    "дизайнерский ремонт",
    "дизайн проект",
    "ремонт под ключ казань",
    "дизайн интерьера казань",
    "3д визуализация интерьера"
]

# Преобразуем текст в числовые векторы
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(queries)

# Кластеризация (например, на 2 группы)
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Результаты
df = pd.DataFrame({
    "Запрос": queries,
    "Кластер": kmeans.labels_
})
print(df)