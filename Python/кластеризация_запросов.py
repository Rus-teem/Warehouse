"""Кластеризация поисковых запросов с помощью TF-IDF и KMeans."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

queries = [
    "дизайнерский ремонт",
    "дизайн проект",
    "ремонт под ключ казань",
    "дизайн интерьера казань",
    "3д визуализация интерьера"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(queries)

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

df = pd.DataFrame({"Запрос": queries, "Кластер": kmeans.labels_})
print(df)
