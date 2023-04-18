# Парсинг, скрапинг и системные скрипты на Python
## Python scripts and snippets

## Скрипты:
1. [Скрапинг таблиц с XPath](#xpath_scraping)
2. [Генератор карты сайта sitemap.xml](#sitemap_generator)
3. [Локальный FTP-сервер](#ftp_server)


### <a name="xpath_scraping">Скрапинг таблиц с множества страниц с XPath</a>
#### Scraping tables from multiple pages using XPath

[Скрипт для скрапинга таблиц с XPath](https://github.com/natkaida/scripts/blob/main/scrape_tables.py)

Скрапинг словаря на 132 страницах:

![Screenshot](https://user-images.githubusercontent.com/85797091/180638580-9e7275f5-a7f3-4590-8081-005e65c2e5af.png)

### <a name="sitemap_generator">Генератор sitemap.xml</a> 
#### XML Sitemap generator in Python

[Скрипт для генерации карты сайта](https://github.com/natkaida/scripts/blob/main/sitemap_generator.py)

Скрипт запрашивает Last modified, преобразует дату в формат W3C, собирает внутренние ссылки и генерирует карту сайта.

![sitemap](https://user-images.githubusercontent.com/85797091/213441629-116f4fba-9f45-4a67-882f-d0d6a7db9d91.jpg)

### <a name="ftp_server">Локальный FTP-сервер</a> 
#### Скрипт для запуска ftp-сервера с помощью pyftpdlib

[Скрипт для запуска локального ftp-сервера](https://github.com/natkaida/scripts/blob/main/ftp_server.py)

Если ваш компьютер под управлением Ubuntu 20.04 - 22.04 не хочет скачивать объемные файлы из shared папки Windows 7-11, и вы уже перепробовали все советы, а передача файла все равно упорно прерывается... просто запустите FTP-сервер на Windows компьютере.

В настройках скрипта используется адрес роутера 192.168.1.101. Чтобы узнать адрес, выполните ipconfig в cmd.

Строки ```import pyftpdlib.handlers``` и ```pyftpdlib.handlers.PassiveDTP.timeout = None``` отключают таймаут. Это нерекомендуемые настройки, но в особо тяжелых случаях помогают:).

![screen](https://user-images.githubusercontent.com/85797091/232847541-a9e8160a-b6fb-4ea4-ad7d-bc8c0ac5663a.jpg)


