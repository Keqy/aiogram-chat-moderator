@echo off

# Убрать, если нет виртуального окружения.
call C:\Downloads\aiogram-chat-moderator\.venv\Scripts\Activate

# pythonw запускает бот в фоне. python - если надо видеть логи.
# Вместо "C:\Downloads\run.py" свой путь.
start pythonw C:\Downloads\aiogram-chat-moderator\run.py
