# итоговый проект
## An Efficient Algorithm for the “Optimal” Stable Marriage. 1987
---
В задаче марьяжа необходимо найти стабильное распределение по парам мужчин и женщин. 
Хотя бы одно стабильное распределение существует всегда, и его можно найти с помощью 
алгоритма Гейла-Шепли, однако этот алгоритм позволяет найти мужское оптимальное и женское 
субоптимальное решение или женское оптимальное и мужское субоптимальное.
Алгоритм Ирвинга позволяет найти "справедливое оптимальное" распределение для мужчин и женщин за O(n^4), 
где n - количество мужчин и женщин.
---
Исходные данные представляют собой xls-файл, где в строках указываются номера агентов и их предпочтения 
относительного агентов другой стороны.
---
example_data.xls - пример исходных данных.
***
data_processing.py - файл обработки исходных данных, создание базы данных предпочтений агентов.
***
male_optimal_solution_2.py - реализация алгоритма Гела-Шепли, поиск shortlists предпочтений.
***
rotations_3.py - поиск ротаций, исключение ротаций.
***
max_flow.py - решение задачи о минимальном разрезе.
***
main.py - графическое приложение.