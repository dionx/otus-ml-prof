# Домашнее задание

Почувствуй мощь трансформеров в бою

**Цель:**

Научиться работать с трансформерными моделями и применять их для различных NLP задач.

**Описание/Пошаговая инструкция выполнения домашнего задания:**

В качестве данных выберете возьмите датасет RuCoLA для русского языка https://github.com/RussianNLP/RuCoLA 
(в качестве train возьмите in_domain_train.csv, а в качестве теста in_domain_dev.csv).

Разбейте in_domain_train на train и val.

Зафайнтьюньте и протестируйте RuBert или RuRoBerta на данной задаче (можно взять любую предобученную модель руберт с сайта huggingface. 
Например, ruBert-base/large https://huggingface.co/sberbank-ai/ruBert-base / https://huggingface.co/sberbank-ai/ruBert-large 
или rubert-base-cased https://huggingface.co/DeepPavlov/rubert-base-cased, ruRoberta-large https://huggingface.co/sberbank-ai/ruRoberta-large, 
xlm-roberta-base https://huggingface.co/xlm-roberta-base).

Возьмите RuGPT3 base или large и решите данное задание с помощью методов few-/zero-shot.

а) переберите несколько вариантов затравок;
б) протестируйте различное число few-shot примеров (0, 1, 2, 4).

Обучите и протестируйте модель RuT5 на данной задаче (пример finetun’а можете найти здесь https://github.com/RussianNLP/RuCoLA/blob/main/baselines/finetune_t5.py).

Сравните полученные результаты.

**Links**

* https://habr.com/ru/companies/sberdevices/articles/596103/?ysclid=ml2rupael9953567214
* https://github.com/ai-forever/ru-gpts
* https://habr.com/ru/companies/sberdevices/articles/596103/

