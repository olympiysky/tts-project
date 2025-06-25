from gtts import gTTS
import os

# Текущий рабочий каталог
print(os.getcwd())  # → 'C:/Users/Имя/Папка'



# Текст на русском
text = "Почему Варвара, давай просто варя.  Привет Ульяна и Варя, давайте уже спать"

# Создаём объект gTTS
tts = gTTS(text=text, lang='ru')

# Сохраняем в mp3-файл
tts.save("russian_audio.mp3")

print("Аудиофайл сохранён: russian_audio.mp3")
