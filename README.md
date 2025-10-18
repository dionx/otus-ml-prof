# OTUS ML Prof


### Установка и настройка

Если нет poetry, установить его:

```bash
rm -rf ~/.local/share/pypoetry
curl -sSL https://install.python-poetry.org | python3 -
```

Создать окружение


```bash
make install 

# или...
python3 -m venv .venv
source .venv/bin/activate
poetry env use $(which python)

cd src
export PYTHONPATH=$(pwd)
```

### Домашние работы по темам

- [1. Git, Shell](hw-1/)
- [2. Визуализация данных](hw-2/)

### Ссылки

* https://www.conventionalcommits.org/ru/v1.0.0/
* https://www.desmos.com/calculator?lang=ru

