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


### Установка PyTorch

https://pytorch.org/get-started/locally/

```bash
# Версия CUDA: 13.0
nvidia-smi
# Нужна версия `python = ">=3.12,<3.15"` в pyproject.toml
poetry source add --priority=explicit pytorch-cu130 https://download.pytorch.org/whl/cu130
poetry add torch torchvision torchaudio

```
