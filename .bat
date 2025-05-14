@echo off
call venv\Scripts\activate
pytest test_app.py
if %ERRORLEVEL% EQU 0 (
    echo All tests passed successfully.
    exit /b 0
) else (
    echo Some tests failed.
    exit /b 1
)
