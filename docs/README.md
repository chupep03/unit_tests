# Математические формулы
## Площадь
- Circle: **S = πR²**
- Rectangle: **S = ab** 
- Square: **S = a²**

## Периметр
- Circle: **P = 2πR**
- Rectangle: **P = 2a + 2b**
- Square: **P = 4a**

# Документация проекта

## Общее описание решения
Проект предоставляет функции для вычисления площадей и периметров фигур: круга, прямоугольника, квадрата.

## Описание функций

### Файл circle.py

#### area(r)
Вычисляет площадь круга по формуле **S = πR²**
- **Аргументы:** r (float) - радиус круга
- **Возвращает:** float - площадь круга  
- **Пример вызова:** `area(5)` вернет `78,53...`

#### perimeter(r)
Вычисляет периметр круга (длину окружности) по формуле **P = 2πR**
- **Аргументы:** r (float) - радиус круга
- **Возвращает:** float - периметр круга
- **Пример вызова:** `perimeter(5)` вернет `31,41...`

### Файл rectangle.py

#### area(a, b)
Вычисляет площадь прямоугольника по формуле **S = ab**
- **Аргументы:** a (float), b (float) - длины сторон
- **Возвращает:** float - площадь прямоугольника
- **Пример вызова:** `area(8, 5)` вернет `40`

#### perimeter(a, b)
Вычисляет периметр прямоугольника по формуле **P = 2a + 2b**
- **Аргументы:** a (float), b (float) - длины сторон  
- **Возвращает:** float - периметр прямоугольника
- **Пример вызова:** `perimeter(3, 5)` вернет `16`

### Файл square.py

#### area(a)
Вычисляет площадь квадрата по формуле **S = a²**
- **Аргументы:** a (float) - длина стороны
- **Возвращает:** float - площадь квадрата
- **Пример вызова:** `area(5)` вернет `25`

#### perimeter(a)
Вычисляет периметр квадрата по формуле **P = 4a**
- **Аргументы:** a (float) - длина стороны
- **Возвращает:** float -перимет квадрата
- **Пример вызова:** `perimeter(5)` вернет `20`

## История изменения проекта

- **6ae23f9** (HEAD -> new_features_505371) documentation and readme.md were added
- **8334c04** (HEAD -> new_features_505371) fixed fault in file rectangle.py
- **00adfaa** added file triangle.py
- **86edb1c** (origin/release) L-05: Update Docs. Add user agreement info
- **438b89a** L-05: Add user agreement
- **6adb962** L-03: Docs added
- **3049431** (origin/feature) L-04: Add rectangle.py
- **b5b0fae** (origin/develop) L-04: Update docs for calculate.py
- **d76db2a** L-04: Add calculate.py
- **51c40eb** L-04: Doc updated for triangle
- **d080c78** L-04: Triangle added
- **d078c8d** (origin/main, origin/HEAD, main) L-03: Docs added
- **8ba9aeb** L-03: Circle and square added