# Используем базовый образ Python 3.11-slim-bookworm
FROM python:3.11-slim-bookworm

# Установка переменной среды PYTHONUNBUFFERED для Python, чтобы вывод был буферизованным
# Полезно когда вывод необходимо получать в реальном времени. Отрицательно влияет на производительность
ENV PYTHONUNBUFFERED=1

# Установка переменной среды PYTHONDONTWRITEBYTECODE для Python, чтобы избежать создания .pyc файлов
# Полезно когда не хочется отвлекаться на .pyc файлы. Данный параметр устанавливается для того чтобы они не создавались. Отрицательно влияет на производительность
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем рабочий каталог внутри контейнера
WORKDIR /tests

# Обновляем пакеты и устанавливаем несколько системных зависимостей и утилит
RUN apt-get update && apt-get install -y \
    curl \
    software-properties-common \
    python3-launchpadlib \
    fonts-liberation \
    jq \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем и устанавливаем Google Chrome и ChromeDriver
RUN curl -L 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json' \
    | jq -r '.channels.Stable.downloads|.chrome,.chromedriver|.[]|select(.platform=="linux64").url|"curl -LO \(.)"' \
    | bash \
    && unzip -d /usr/local/share 'chrome-linux64.zip' \
    && ln -s /usr/local/share/chrome-linux64/chrome /usr/bin/chrome \
    && unzip -d /usr/local/share 'chromedriver-linux64.zip' \
    && ln -s /usr/local/share/chromedriver-linux64/chromedriver /usr/bin/chromedriver \
    && rm 'chrome-linux64.zip' && rm 'chromedriver-linux64.zip'

# curl -L 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json':
#
# Эта часть команды использует curl для загрузки файла JSON с информацией о версиях Google Chrome и ChromeDriver с веб-сайта https://googlechromelabs.github.io. Флаг -L указывает на переход по перенаправлениям, если они есть.
# | jq -r '.channels.Stable.downloads|.chrome,.chromedriver|.[]|select(.platform=="linux64").url|"curl -LO \(.)"':
# После загрузки JSON-файла команда передает его на вход утилите jq, которая используется для обработки JSON-данных.
# jq выполняет следующие операции:
# 
# 1. Извлекает информацию о версиях Chrome и ChromeDriver для канала "Stable".
# 2. Выбирает URL-адреса для Linux (.platform=="linux64").
# 3. Генерирует команды curl для скачивания файлов Chrome и ChromeDriver.
#
# | bash:
# Результат команды jq, который содержит команды curl для скачивания файлов, передается на вход команды bash. Это приводит к выполнению сгенерированных команд curl для загрузки файлов Chrome и ChromeDriver в контейнер.
# && unzip -d /usr/local/share 'chrome-linux64.zip':
# После скачивания файлов Chrome и ChromeDriver, команда unzip извлекает их содержимое из ZIP-архивов в каталог /usr/local/share.
# && ln -s /usr/local/share/chrome-linux64/chrome /usr/bin/chrome:
# Эта часть команды создает символическую ссылку (ln -s) для исполняемого файла Google Chrome (chrome) в каталоге /usr/bin, что позволяет запускать Chrome из любой директории, добавив "chrome" к команде.
# && unzip -d /usr/local/share 'chromedriver-linux64.zip':
# Аналогично Chrome, команда unzip извлекает содержимое ZIP-архива ChromeDriver в каталог /usr/local/share.
# && ln -s /usr/local/share/chromedriver-linux64/chromedriver /usr/bin/chromedriver:
# Эта часть команды создает символическую ссылку для исполняемого файла ChromeDriver (chromedriver) в каталоге /usr/bin, что позволяет запускать ChromeDriver из любой директории, добавив "chromedriver" к команде.
# && rm 'chrome-linux64.zip' && rm 'chromedriver-linux64.zip':
# Наконец, после установки Chrome и ChromeDriver, файлы ZIP-архивов удаляются с помощью команд rm, чтобы освободить дисковое пространство.
# В результате выполнения этой строки команды в контейнере Docker, Google Chrome и ChromeDriver устанавливаются и готовы к использованию.
        

# Копируем файл requirements.txt и устанавливаем зависимости Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы из текущего контекста сборки в рабочий каталог
COPY . .

# Запускаем проект 
CMD ["python", "main.py"]