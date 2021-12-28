# mvc-simple-task

1. Запустить приложение.
2. Реализовать сохранение данных, получаемых из метода POST в файл (json, csv) или базу данных sqlite.
3. Корректно подключить и использовать шаблонизатор Jinja2 (реализовать приложение как пакет и подключить Jinja2 корректно).
4. Реализовать содержимое класса Record (или Item), в котором содержатся и проверяются данные, связанные с регистрацией на конференцию.
5. Использовать шаблонизатор Jinja2 и реализовать три шаблона: один - базовый с head, title, body. Второй — содержимое формы, которая 
отображается на индексной странице; Третий шаблон - отображение всех записей, которые были добавлены в базу данных / файл.

По пункту 2: 
```python
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(loader=PackageLoader('app', 'templates'),
autoescape=select_autoescape(['html', 'xml']))

```


Соответствующее задание ИСР 1.2. Создание пользовательского пакета для приложения "Гостевая книга" 
