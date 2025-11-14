# Домашнее задание

Как узнать свою аудиторию? Построение различных вариантов кластеризаций и интерпретация результатов.

**Цель:**
На этот раз займемся классической задачкой - сегментация клиентов (в данном случае - банка). 
Крайне полезная операция, которая позволяет вам лучше познакомиться со своей аудиторией, понять, на какие группы она делится и чем они характеризуются.

**Описание/Пошаговая инструкция выполнения домашнего задания:**

### Часть 1. EDA и Preprocessing.

Скачайте данные по клиентам немецкого банка: https://www.kaggle.com/uciml/german-credit;
Проведите EDA, чтобы познакомиться с признаками;
Преобразуйте все признаки в числовые подходящими методами;
Приведите все данные к одному масштабу (а заодно поясните, почему это необходимая операция при кластеризации).

### Часть 2. Моделирование.

Постройте три варианта кластеризации: k-means, hierarhical и DBSCAN, подберите оптимальное количество кластеров для каждого метода при помощи Elbow method и Silhouette plot;
Также воспользуйтесь различными вариантами сжатия признакового пространства (PCA, UMAP, tSNE) и визуализируйте результаты кластеризации на двумерной плоскости.

### Часть 3. Интерпретация.

Теперь ваша задача - попытаться проинтерпретировать получившиеся кластеры, начните с простого расчета средних значений признаков для каждого из кластеров, есть ли интересные закономерности?
Теперь постройте boxplot-ы для каждого признака, сгруппировав значения по кластерам, по каким признакам заметно наибольшее отличие кластеров друг от друга? Можно ли их интерпретировать?

### Полезные ссылки

https://www.kaggle.com/code/paulinan/bank-customer-segmentation
https://www.kaggle.com/code/dezzpil/otus-2-2-kmeans
https://www.kaggle.com/code/dezzpil/otus-2-2-agglomerative
https://www.kaggle.com/code/nataliashcheglova/clustering-k-means-agglomerative-dbscan
https://www.kaggle.com/code/asilkanv/credit-customer-segmention (KMeans Silhoutte Method)
https://www.kaggle.com/code/cindyteh/credit-card-users-segmentation
https://www.kaggle.com/code/egadharmawan/customer-segmentation
https://www.kaggle.com/code/mitanshur/eda-of-german-credit-risk-dataset (EDA)
https://www.kaggle.com/code/abhhii/pcaimplement (PCA)
https://www.kaggle.com/code/damaradiprabowo/clustering-german-credit-data
