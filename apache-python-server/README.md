Репозиторий содержит html-страницу, url-ссылки которой запускают python-скрипты.
Скрипты реализуют:
  - загрузку картинки
  - чтение данных из БД

Установка:
1. Скачать Apache.
2. Необходимо в файл конфигурации apache2.conf добавить:
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"		
    <Directory "/var/www/cgi-bin/">				
        Require all granted					
        Options +ExecCGI					
        AddHandler cgi-script .cgi			
        Options Indexes FollowSymLinks			
        AllowOverride None					
        Require all granted					
  </Directory>

  3.Весь процесс происходит в директории /var/www/
  4. Запустить скрипт build-python-venv
  5. Настроить пути
