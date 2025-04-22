REM This Source Code Form is subject to the terms of the Mozilla
REM Public License, v. 2.0. If a copy of the MPL was not distributed
REM with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

@echo off

# Убрать, если нет виртуального окружения.
call C:\Downloads\aiogram-chat-moderator\.venv\Scripts\Activate

# pythonw запускает бот в фоне. python - если надо видеть логи.
# Вместо "C:\Downloads\run.py" свой путь.
start pythonw C:\Downloads\aiogram-chat-moderator\run.py
