# Как запустить? 

**Mac OS**
1. Переходим в папку backend
*Наше местонахождение мы можем проверить с помощью команды pwd*
2. python3 -m venv venv
3. source venv/bin/activate 
4. pip3 install -r requirements.txt
5. uvicorn main:app --reload
6. Открываем главную страницу: http://127.0.0.1:8000/
7. Открываем документацию (Swagger): http://127.0.0.1:8000/docs 



