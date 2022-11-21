# MEDUSA - Media usage
#### Video Demo:  https://youtu.be/9V0wtKn-NxU
#### Description:

### EN
This is a presentation of my latest CS50P Harvard Course Design.

Project name: MEDUSA

MEDUSA stands for Media Usage.

The program takes data from a CSV file (date and reading from an energy, water, electricity, gas or other meter) and calculates the following values:
- [x] shows a menu with possible options to choose from
- [x] that the meter has been replaced
- [x] daily consumption in the interval between readings
- [x] adds units, e.g. m3, kWh, GJ, etc.
- [x] counts the days between readings
- [x] counts the consumption between readings
- [x] shows the minimum and maximum amount of daily consumption
- [x] calculates the arithmetic mean of the total use
- [x] Shows a date-to-daily graph of consumption

### Program operation
The program runs on the command line.
In order for the program to start working, use the command:
```python project.py```

or

```python project.py filename.csv```


In the first case, the program will ask you to enter a file name with the extension ".csv" until it is successful or will allow you to exit the program with the command ```exit``` or ```q```.

```File:```

In both cases, the program will ask you to enter the units in which the meter reads them until successful, or will allow you to exit the program with the command ```exit``` or ```q```.

```Units:```

You can skip this step by appending the unit file name to the end as follows:

```filename__units.csv```

2 underscores are needed example:

```electricity__kWh.csv```

### Protection:
You cannot specify more than one file name on the command line.
When a menu is displayed, only those commands that are available in the menu can be selected.
The program will be terminated if the given file is not compatible with the input data:

```
date, meter
2015-12-01,318
2016-01-01,555
```

### Packages used:
```sys```
```csv```
```datetime```
```tabulate```
```re```
```matplotlib.pyplot```

### Class
There is one class in the program that calculates the necessary results:

```Gauge```

#
#### Opis:
### PL
To jest prezentacja mojego ostatniego projektu kursu Harvard'a CS50P.

Nazwa projektu: MEDUSA

MEDUSA to skrót od Media Usage.

Program pobiera dane z pliku CSV (datę i odczyt z licznika energii, wody, prądu, gazu lub innego) i oblicza następujące wartości:

- [x] pokazuje menu z możliwymi opcjami do wyboru
- [x] czy licznik został wymieniony
- [x] zużycie dzienne w przedziale między odczytami
- [x] dodaje jednostki np.: m3, kWh, GJ itp.
- [x] liczy dni pomiędzy odczytami
- [x] liczy zużycie pomiędzy odczytami
- [x] pokazuje minimalną i maksymalną wartość poboru dziennego
- [x] liczy średnią arytmetyczną z całości urzytkowania
- [x] pokazuje wykres data do dziennego zużycia

### Działanie programu
Program działa w linii komend.
Aby program rozpoczął działać, należy użyć komendy:

```python project.py```

lub

```python project.py nazwa_pliku.csv```

W pierwszym przypadku program poprosi o podanie nazwy pliku z rozszeżeniem ".csv" do skutku lub pozwoli opuścić program poleceniem ```exit```, lub ```q```.

```File:```

W obydwóch przypadkach program poprosi o podanie jednostek, w jakich je licznik odczytuje do skutku lub pozwoli opuścić program poleceniem ```exit```, lub ```q```.

```Units:```

Można pominąć ten krok, dodając do końca nazwy pliku jednostki w następujący sposób:

```nazwa_pliku__units.csv```

Potrzebne są 2 podkreślenia przykład:

```electricity__kWh.csv```

### Zabezpieczenia:
Nie można podać w linii komend więcej niż jednej nazwy pliku.
Po wyświetleniu menu można wybrać tylko te polecenia, które są dostępne w menu.
Program wyłączy się, jeżeli podany plik będzie niekompatybilny z danymi wejściowymi:
```
date,meter
2015-12-01,318
2016-01-01,555
```
### Użyte pakiety:
```sys```
```csv```
```datetime```
```tabulate```
```re```
```matplotlib.pyplot```

### Klasy
W programie została stworzona jedna klasa obliczająca potrzebne wyniki:

```Gauge```