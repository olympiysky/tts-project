# tts-project
tts-project

# Установка:
```bash
pip install gTTS
```

# Основной класс gtts.gTTS
```python
gtts.gTTS(text, lang='en', slow=False, tld='com')
```

Параметр	Описание
text	Текст, который нужно озвучить.
lang	Язык озвучки (например, 'en', 'ru', 'kk', 'fr', 'de' и т.д.)
slow	Если True, речь будет медленной. По умолчанию False.
tld	Используемый TLD (домен верхнего уровня) для Google (например, 'com', 'co.uk', 'ru'). Влияет на акцент.

# Методы
save(filename) Сохраняет речь в файл (обычно .mp3):
```from gtts import gTTS
tts = gTTS("Привет, мир!", lang='ru')
tts.save("hello.mp3")

```
write_to_fp(fp)
Записывает аудио в файлоподобный объект:
```
import io
from gtts import gTTS

tts = gTTS("Пример", lang='ru')
with io.BytesIO() as f:
    tts.write_to_fp(f)
    f.seek(0)
    # теперь можно воспроизвести или сохранить
```

# Языки
gtts.lang.tts_langs()
Возвращает словарь поддерживаемых языков:

```
from gtts.lang import tts_langs
print(tts_langs())
```
# Пример полного использования:

```
from gtts import gTTS
import os

text = "Здравствуйте! Это пример использования библиотеки gTTS."
tts = gTTS(text=text, lang='ru', slow=False)
tts.save("output.mp3")
os.system("start output.mp3")  # Windows
```

# Замечания
Работает только с интернет-соединением, так как использует онлайн-сервис Google Translate.

Нет возможности изменять голос, тон или пол спикера.

Нет офлайн-режима.

Если вы хотите использовать TTS офлайн — стоит рассмотреть альтернативы, такие как pyttsx3.




