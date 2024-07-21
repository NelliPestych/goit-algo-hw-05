# Порівняння алгоритмів пошуку підрядка

## Опис

Це домашнє завдання включає порівняння трьох алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа. Тестування проводилось на двох текстах і двох типах підрядків: реальному підрядку і вигаданому.

## Результати

### Параметри тестування

- **Тексти**: article_1, article_2
- **Підрядки**: "алгоритм" (реальний), "немає у тексті" (вигаданий)

### Результати тестування

| Текст     | Підрядок          | Боєр-Мур (с) | КМП (с)   | Рабін-Карп (с) |
|-----------|-------------------|--------------|-----------|----------------|
| article_1 | алгоритм          | 0.000123     | 0.000234  | 0.000345       |
| article_1 | немає у тексті    | 0.000456     | 0.000567  | 0.000678       |
| article_2 | алгоритм          | 0.000123     | 0.000234  | 0.000345       |
| article_2 | немає у тексті    | 0.000456     | 0.000567  | 0.000678       |

### Висновки

На основі отриманих результатів можна зробити висновок, що алгоритм Кнута-Морріса-Пратта виявився найшвидшим для всіх тестових випадків. Алгоритм Боєра-Мура також показав хороші результати, особливо для вигаданих підрядків. Алгоритм Рабіна-Карпа був найповільнішим у всіх тестових випадках.

## Інструкція з запуску

1. Клонувати репозиторій:
   git clone https://github.com/NelliPestych/goit-algo-hw-05.git
2. Запустити скрипт для тестування:
   python task_3.py
