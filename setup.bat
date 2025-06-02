@echo off


echo Activating virtual environment...
call venv\Scripts\activate

echo Installing requirements...
pip install -r "requirements.txt"

echo Setup complete!
pause
