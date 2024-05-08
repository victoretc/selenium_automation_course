Введение в Docker:

1. Установка Docker: <https://docs.docker.com/get-docker/>
2. Начиная: <https://docs.docker.com/get-started/>
3. Основные команды Docker: <https://timeweb.com/ru/community/articles/osnovnye-komandy-docker>

**Использованные команды для первичной настройки Ubuntu 22.04**

```python
cat /etc/*release
apt-get upgrade
apt-get update
apt-get install -y vim htop git curl wget
```

Настройка входа по ssh

```python
vim /etc/ssh/sshd_config
service ssh restart
vim ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

Cоздаем новый терминал и проверяем что работает подключение без пароля

Почитать про ssh авторизацию можно тут: <https://selectel.ru/blog/ssh-authentication/>
Установка Docker: <https://docs.docker.com/engine/install/ubuntu/>
Selenium manager: <https://www.selenium.dev/documentation/selenium_manager/>
Chrome для тестирования: <https://developer.chrome.com/blog/chrome-for-testing/>
