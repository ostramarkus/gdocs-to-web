# Grunderna i Python

## **Variabler och datatyper**

Variabler används för att lagra enskilda värden. Variabler är av olika **datatyper** beroende på vilken typ av data som lagras.

### **De vanligaste datatyperna**

| Datatyp | Exempel | Förklaring |
| :---- | :---- | :---- |
| **str** (string / text) | `name = "Elmo"` | Textsträngar, skrivs inom `" "` eller `' '`. |
| **int** (heltal) | `x = 5` | Heltal, utan decimaler. Kan vara positiva eller negativa. |
| **float** (flyttal) | `y = 3.14` | Tal med decimaler. |
| **bool** (boolean) | `is_happy = True` | Kan bara vara `True` eller `False`.  |

### **Definiera variabler**

Variabler skapas och tilldelas ett värde med likamedstecknet: **`=`**.

```py
# Sträng / str
my_string = 'Hello World'

# Heltal / int
my_int = 42	

# Decimaltal / float
my_float = 3.14			
```

### **Omvandla mellan datatyper**

Man kan omvandla värden/variabler mellan olika datatyper. (Eng: *type conversion* eller *type casting.*)

```py
# Gör om ett värde till en textsträng
my_string = str(42)

# Gör om ett värde till ett heltal
my_int = int(13.3)	
		
# Gör om ett värde till ett decimaltal
my_float = float('3.14')	
```

### **Ta reda på datatyp**

Med funktionen **`type()`** kan man ta reda på datatypen för en variabel.

```py
name = 'Markus'
print(type(name))

# → <class 'str'>
```

### **Räkna med variabler**

Variabler kan användas i beräkningar.

```py
x = 100
my_sum = 100 + x
```

### **Vanliga operatorer för beräkningar**

Operatorer som används i beräkningar kallas för **aritmetiska operatorer**.

|  | Förklaring |
| :---: | :---- |
| **`+`** | Addition |
| **`-`** | Subtraktion |
| **`*`** | Multiplikation |
| **`/`** | Division |
| **`//`** | Division med avrundning nedåt |
| **`**`** | Upphöjt |
| **`%`** | Modulo / rest från division |
| **`+=`** | Addera till |
| **`-=`** | Subtrahera från |

### **Addera eller subtrahera variabler**

```py
x = 1
y = 100

# Addera 1 till x
x += 1

# Subtrahera 3 från y
y -= 3
```

### 

## **Input och output**

### **Skriva ut med `print()`**

Funktionen **`print()`** skriver ut text till terminalfönstret. 

```py
print('Hello World!')
```

### **Skriv ut flera värden med kommatecknet**

Man kan ange flera värden att skriva ut med hjälp av kommatecknet. Man får ett automatiskt mellanslag mellan värdena. Det spelar ingen roll vilken **datatyp** värdena är.

```py
name = 'Markus'
score = 100

print('Hello', name, 'Your score:', score) 
# → 'Hello Markus Your score: 100'
```

### **Skriv ut utan att skapa en ny rad**

Om man vill skriva ut fler värden på samma rad kan man ange en tom sträng för argumentet **`end`** i print-funktionen.

```py
print('One ', end="")
print('Two ', end="")
print('Three')

# → 'One Two Three'
```

### **Input-funktionen**

Funktionen **`input()`** pausar programmet och väntar på text-input från användaren. Den input man får lagrar man oftast i en variabel. 

**OBS\!** Input-datan är alltid en textsträng/**`str`**.

```py
name = input('Vad heter du?')
```

### **Typomvandla direkt från input-funktion**

Om man vill göra beräkningar eller numeriska jämförelser med datan från en input-funktion kan man konvertera den direkt till en annan datatyp.

```py
age = int(input('Hur gammal är du?'))
```

## **Textsträngar**

### **Sätta ihop textsträngar**

Med plustecknet kan man sätta ihop flera textsträngar. Detta kallas **konkatenering**.

**OBS\!** Alla värden måste vara textsträngar.

```py
name = 'Markus'
print('Hello ' + name + '!') 

# → Hello Markus!
```

```py
firstname = 'Markus'
lastname = 'Pettersson'
full_name = firstname + ' ' + lastname

# full_name → 'Markus Pettersson'
```

### **Sträng-formatering med f-strings**

Med så kallad f-sträng-formattering kan man sätta in variabler direkt i en textsträng. Man kan också ange hur variablerna ska formateras vid utskrift (t.ex. antalet decimaler.)

```py
price = 19.9
product_name = 'kexchoklad'
print(f'Du har köpt en {product_name} för {price:.2f} kr.')

# → 'Du har köpt en kexchoklad för 19.90 kr.'
```

🔗[Python f-string: A Complete Guide | DataCamp](https://www.datacamp.com/tutorial/python-f-string)

| Typ | Exempel | Förklaring | Resultat |
| :---- | :---- | :---- | :---- |
| Decimaler | `f"{pi:.2f}"` | 2 decimaler | `"3.14"` |
| Begynnande nollor | `f"{11:4d}"` | Lägger till nollor så att strängen blir 4 tecken | "0011" |
| Procent | `f"{0.85:.0%}"` |  | `"85%"` |
| Tusentalsavgränsning | `f"{1234567:,}"` |  | `"1,234,567"` |

### **Ta ut delar av en sträng**

Strängar kan på många sätt hanteras som listor. Man kan till exempel ta utdelar av en sträng med hakklammer **`[]`**. Detta kallas för **slicing**.

```py
name = 'Markus'
first_three_letters = name[0:2] 

# first_three_letters → 'Mar'
```

### **Ändra stora/små bokstäver**

```py
name = 'Markus'
big_name = name.upper()	# → 'MARKUS'
small_name = name.lower()	# →  'markus'
```

### **Sök och ersätt i text**

```py
string = 'find and replace'
new_string = string.replace('find', 'replace')

# new_string → 'replace and replace'
```

### **Ta bort tomrum (och ny-rad-tecken) från sträng**

```py
name = '    Markus      '
new_name = name.strip()	

# new_name → 'Markus'
```

### **Konvertera sträng till lista**

```py
my_string = 'ABCDEF'
my_list = list(my_string)

# my_list → ['A', 'B', 'C', 'D', 'E', 'F']
```

## 

## **Listor**

Listor används för att lagra flera värden som hör samman med varandra. En lista skapar man som en variabel med värden separerade med kommatecken. Listans värden ramas in i klammerparenteser **`[]`**.

### **Definiera en lista**

```py
my_list = ['value1', 'value2', 'value3']
```

### **Nå ett listvärde**

För att nå ett värde i listan använder man ett positionsnummer. Den första positionen har numret 0\. Positionsnummer kallas även **index**.

```py
my_list = ['value1', 'value2', 'value3']
first_value = my_list[0]

# first_value → 'value1'
```

### **Räkna bakifrån**

Med negativa positionsnummer räknar man bakifrån från sista positionen. 

```py
my_list = ['value1', 'value2', 'value3']
last_value = my_list[-1]

# last_value → 'value3'
```

### **Välj delar av en lista**

Med kolon **:** kan man ange ett intervall av positioner. Detta kallas för **slicing**.

```py
my_list = ['value1', 'value2', 'value3', 'value4']
first_three_values = my_list[0:2]

# first_three_values → ['value1', 'value2', 'value3']
```

### **Tilldela ett värde till en viss position**

```py
my_list[0] = 'new value'
```

### **Lägga till ett till värde till en lista**

```py
my_list.append('new value')
```

### **Ta reda på längden på en lista eller sträng**

```py
my_list = ['value1', 'value2', 'value3']
list_size = len(my_list)

# list_size → 3
```

```py
name = 'Markus'
string_size = len(name)

# string_size → 5
```

### **Gå igenom/iterera en lista ett värde i taget**

```py
menu = ['pizza', 'kebab', 'sushi']

for food in menu:
    print(food)
```

### **Skapa en lista från en textsträng**

```py
food_string = 'kebab, pizza, sushi, meatballs'
food_list = food_string.split(',')

# food_list → ['kebab', ' pizza', ' sushi', ' meatballs']
```

### **Skapa en textsträng från en lista**

```py
food_list = ['kebab', ' pizza', ' sushi', ' meatballs']
food_string = ','.join(food_list)

# food_string → 'kebab, pizza, sushi, meatballs'
```

### **Sortera en lista**

```py
menu = ['B', 'D', 'C', 'A']
menu.sort()

# menu → ['A', 'B', 'C', 'D']
```

```py
numbers = [1, 5, 2.4, 0.3, 100]
numbers.sort()

# numbers → [0.3, 1, 2.4, 5, 100]
```

### **Summera en lista**

```py
scores = [12, 34, 56, 12, 32, 34]

print(sum(scores))
# → 180
```

### **Max- och min-värden**

```py
scores = [12, 34, 56, 12, 32, 34]

print(min(scores))
# → 12
```

```py
scores = [12, 34, 56, 12, 32, 34]

print(max(scores))
# → 56
```

### **Medelvärde**

```py
scores = [12, 34, 56, 12, 32, 34]

print(sum(scores) / len(scores))
# → 30.0
```

## 

## **Villkor \- if-satser**

If-satser används för att programmet ska utföra viss kod endast då ett visst villkor är uppfyllt. Det kodblock som ska utföras har 4 mellanslags indrag. (*Indentering*)

**`else`** används för att ange vad som ska göras ifall villkoret inte uppfylls. **`elif`** används för att kedja flera villkorstester efter varandra.

### **Vanliga operatorer för villkor**

|  | Förklaring |
| :---: | :---- |
| **`==`** | Lika med |
| **`!=`** | Inte lika med |
| **`<`** | Mindre än |
| **`>`** | Större än |
| **`>=`** | Lika eller större än |
| **`<=`** | Lika eller mindre än |
| **`and`** | Och |
| **`or`** | Eller |

### **Jämförelse av textsträngar**

```py
name = 'Markus'

if name == 'Markus':
   print('Welcome!')
else:
   print('Go away!')

# → 'Welcome!'
```

### **Jämförelse av numeriska värden**

```py
age = 25

if age > 20:
   print('Hello!')
else:
   print('Goodbye')

# → 'Hello!'
```

### **Flera villkor med `and`** 

Med **`and`** kan man ange flera villkor som alla måste vara sanna.

```py
username = 'marpet'
password = 'secret'

if username == 'marpet' and password == 'secret':
    print('Welcome!')
else:
    print('Access denied!')

# → 'Welcome!'
```

### **Flera villkor med `or`**

Med **`or`** kan man ange flera villkor. Det räcker med att ett av villkoren är sant.

```py
if username == 'marpet' or username == 'marpet2':
    print('Welcome!')
else:
    print('Access denied!')
```

### **Else-if \- flera jämförelser**

Med **`elif`** testas flera villkor efter varandra. När ett villkor är sant avslutas if-satsen.

```py
if role == 'admin':
    print('Welcome admin!')
elif role == 'user':
    print('Welcome user!')
elif role == 'author':
    print('Welcome author!')
else:
    print('Access denied!')
```

### **If och listor**

Med en if-sats kan man kontrollera ifall ett värde finns i en lista.

```py
menu = ['kebab', 'pizza', 'meatballs']

if 'pizza' in menu:
   print('Yes! Pizza!')
else:
   print('Nooooo..... I want pizza!')

# → 'Yes! Pizza!'
```

### **If och strängar**

Med en if-sats kan man kontrollera ifall en textsträng innehåller en viss annan sträng.

```py
text = 'Python is easy!'

if 'easy' in text:
   print('Correct!')
else:
   print('You are wrong! Practice more!')

# → 'Correct'
```

### **If och funktioner**

Funktioner som returnerar **`True`** eller **`False`** (booleska värden) kan användas direkt som villkor i if-satser.

```py
if is_logged_in():
   print('Welcome!')
else:
   print('Access denied!')
```

## 

## **Loopar**

Loopar används när man vill upprepa kod flera gånger. Den kod som ska utföras i loopen *indenteras* med 4 mellanslag.

### **En for-loop med range()**

För att ange hur många gånger en **`for`**\-loop ska köras används funktionen **`range()`** som skapar en talserie mellan två heltal.

```py
for i in range(0, 10):
   print('I can count to:', i)
```

### **En for-loop för att gå igenom en lista/sträng**

For-loopar används även för att gå igenom (*iterera*) listor och strängar.

```py
menu = ['pizza', 'kebab', 'sushi']

for food in menu:
    print(food)
```

```py
name = 'Markus'

for letter in name:
    print(letter)
```

### **While-loop**

En **`while`**\-loop körs så länge ett villkor är uppfyllt.

```py
i = 0

while i < 10:
    print('I can count to:', i)
    i += 1
```

### **Evig `while`\-loop**

Om man anger ett villkor som alltid är sant, skapas en evig loop.

```py
while True:
    input('Are we there yet?')
```

### **Avbryta en loop med `break`** 

Man kan använda **`break`** för att avbryta en loop.

```py
while True:
    answer = input('Are we there yet?')
    if answer == 'yes':
        print('Finally!')
        break
```

### **Skapa listor med range**

Funktionen **`range`** kan även användas för att skapa en lista av talserier. Funktionen tar även ett tredje argument som anger avståndet mellan talen i talserien.

```py
my_list = list(range(0, 50, 10))
print(my_list)

# → [0, 10, 20, 30, 40]
```

## 

## **Funktioner**

En *funktion* är namngiven kod som man kan anropa från sitt program. Med funktioner slipper man upprepa sig när man vill göra samma sak flera gånger i ett program. Funktioner är också ett sätt att dela upp ett större program i mindre, mer lätthanterliga delar. 

### **Egen funktion**

```py
def hello():
    print('Hello!')
    print('Have a nice day!')

hello()
```

### **Funktion som tar emot argument**

De värden som skickas in i en funktion kallas för **argument**.

```py
def hello(name):
    print('Hello', name)

hello('Markus')
```

### **Flera argument \- returnera ett värde**

Det är vanligt att en funktion bearbetar information för att sedan skicka tillbaka ett resultat till huvudprogrammet \- funktionen **returnerar** ett värde.

```py
def triangle_area(base, height):
    area = base * height / 2
    return area
    
my_area = triangle_area(5, 7)
print(my_area)
```

### **Returnera booleska värden**

Det är vanligt med funktioner som returnerar **`True`** eller **`False`** (*booleska* värden).

```py
def is_weekend(day):
    if day == 'saturday' or day == 'sunday':
        return True
    else:
        return False
```

Om funktionen bara testar ett eller flera villkor behöver man inte någon if-sats. Man kan istället direkt returnera resultatet av villkorstestet:

```py
def is_weekend(day):
    return day == 'saturday' or day == 'sunday'
```

### **Funktioner med keyword-arguments**

Om man vill göra sina funktioner tydligare och flexiblare kan man använda **keyword-arguments** (nyckelargument). Då namnger man argumenten som funktionen tar emot och anger även **default-värden** för argumenten.

Med keyword-argument behöver man inte hålla koll på ordningen för argumenten när man anropar funktionen. Och med default-värden kraschar inte programmet om man utelämnar ett argument.

```py
# Funktion med keyword-arguments och default-värden
def triangle_area(base=10, height=10):
    area = base * height / 2
    return area
    
# Funktionen anropas med de namngivna argumenten
my_area = triangle_area(base=5, height=7)

# Funktionen anropas utan argument - då används default-värden
my_area1 = triangle_area()
```

## 

## **Dictionary \- dict**

Datatypen **dictionary** (dict) är en *samling* precis som listor. Istället för att de olika elementen representeras av ett positionsnummer (0, 1, 2 etc.) används beskrivande namn. Namnen som identifierar positionerna kallas för **keys** (sv. nycklar).

### **En enkel dictionary**

```py
car = {'brand': 'Volvo', 'color': 'black', 'max_speed': 280}

print(car['max_speed'])
```

### **En dictionary på flera rader**

```py
car = {
    'brand': 'Volvo', 
    'color': 'black', 
    'max_speed': 280,
    'price': 200000,
    'model_year': 2018,
}
```

### **En lista av dictionaries**

```py
products = [
    {
        "name": "Ahlgens bilar",
        "price": 17.5,
        "quantity": 2,
    },
    {
        "name": "Gott och blandat",
        "price": 18.5,
        "quantity": 3,
    },
]
```

### 

### **Gå igenom en dictionary med en for-loop**

```py
car = {
    'brand': 'Volvo', 
    'color': 'black', 
    'max_speed': 280,
    'price': 200000,
    'model_year': 2018,
}

for key, value in car.items():
    print(key, ':', value)
```

## 

## **Tuplar och set**

**Tuplar** och **set** är samlingar (*collections*) och alternativ till listor. 

De viktigaste skillnaderna mot vanliga listor:

* **Tuplar** är inte ändringsbara (de är *immutable*). Man kan alltså inte ändra dess värden efter att tupeln är skapad.  
* **Set** kan endast innehålla unika värden. De kan alltså inte innehålla dubbletter.

### **Definiera en tupel**

```py
my_tuple = ('kebab', 'pizza', 'meatballs')
```

### **Definiera ett set**

```py
my_set = {'kebab', 'pizza', 'meatballs'}
```

### **Skillnaderna mellan listor, tuplar och set**

| Egenskap | List (`list`) | Tuple (`tuple`) | Set (`set`) |
| :---- | :---- | :---- | :---- |
| **Ordning** | Bevaras | Bevaras | Ingen garanterad ordning |
| **Dubbletter** | Tillåts | Tillåts | Ej tillåtna (unika element) |
| **Ändringsbar** | Ja | Nej (immutable) | Ja (men endast unika element) |
| **Sökning (`x in ...`)** | Långsammare  | Långsammare  | Mycket snabb  |
| **Använd som dict-nyckel** | Nej | Ja | Nej |
| **Vanliga användningsområden** | Listor av data som kan ändras, ordning viktig | Koordinater, fasta värden, säkra datastrukturer | Unika värden, mängdoperationer (union, snitt, skillnad) |
| **Prestanda** | Flexibel men lite långsammare | Snabbare än listor | Snabb för medlemskap och mängdlogik |

## **Modulen random**

Modulen **`random`** används för att hantera slumptal.

### **Importera moduler**

Moduler som **`random`** behöver importeras innan de används. Import av moduler görs högst upp i ens kod.

```py
import random
```

### **Slumpar ett decimaltal mellan 0 och 1**

```py
r1 = random.random()
```

### **Slumpar ett heltal mellan vissa värden**

```py
r2 = random.randrange(10, 20)
```

### **Slumpar ett alternativ från en lista**

```py
menu = ["pizza", "kebab", "pasta"]
food = random.choice(menu)
```

## **Modulen datetime**

Modulen **`datetime`** används för att hantera tid och datum.

### **Ta fram dagens datum**

```py
import datetime

today = datetime.date.today()
```

### **Ta fram ett annat datum**

```py
christmas = datetime.date(2025, 12, 24)
```

### **Ta fram ett datum från en sträng i iso-format**

```py
christmas = date.fromisoformat("2025-12-24")
```

### **Ta fram veckodag för datum**

Metoden **`weekday()`** ger veckodagens nummer. Måndag \= 0, tisdag \= 1 etc.

```py
christmas = datetime.date(2025, 12, 24)
print(christmas.weekday())

# → 2
```

### **Räkna med datum**

```py
christmas = datetime.date(2025, 12, 24)
today = datetime.date.today()

time_to_christmas = christmas - today

print(time_to_christmas)
```

```py
today = datetime.date.today()

ten_days = datetime.timedelta(days = 10)
in_ten_days = today + ten_days

print(in_ten_days)
```

### **Datetime \- datum och tid tillsammans**

```py
now = datetime.datetime.now()

print(now)
# → 2025-09-16 10:05:21.723942

print(now.time())
# → 10:05:21.723942

print(now.date())
# → 2025-09-16
```

### **Översikt över modulen datetime**

| Klass | Egenskaper (attribut) | Vanliga metoder |
| :---- | :---- | :---- |
| **`date`** | `year`, `month`, `day` | `today()`, `fromisoformat()`, `weekday()`, `isoweekday()`, `isoformat()`, `replace()` |
| **`datetime`** | `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond` | `now()`, `today()`, `utcnow()`, `fromtimestamp()`, `strftime()`, `strptime()`, `date()`, `time()`, `replace()` |
| **`time`** | `hour`, `minute`, `second`, `microsecond` | `isoformat()`, `replace()` |
| **`timedelta`** | `days`, `seconds`, `microseconds` | `total_seconds()` \+ stöder aritmetik med datum/tid (\+, \-) |

## **Filer: läsa och skriv**

### **Öppna och läs in en hel textfil**

```py
with open('names.txt') as file:
    content = file.read()

print(content)
```

### **Öppna och läs en textfil rad för rad**

Genom att använda metoden **`strip()`** tar vi bort tecknet för "ny rad" i slutet på varje textrad.

```py
with open('names.txt') as file:
    for line in file:
        print(line.strip())
```

### **Öppna och läs en textfil rad för rad**

```py
with open('names.txt') as file:
    for line in file:
        print(line)
```

### **Öppna och läs in en textfil till en lista**

```py
with open('names.txt') as name_file:
    names = name_file.readlines()
```

### **Öppna och skriv till en textfil**

Detta tar bort eventuellt tidigare innehåll

```py
with open('textfile.txt', 'w') as textfile:
    textfile.write('Hello world!')
```

### **Öppna och lägg till i befintlig fil**

```py
with open('textfile.txt', 'a') as textfile:
    textfile.write('Hello world!')
```

### **Skriva en ny rad med tecknen: `\n`**

Om man vill lägga till en radbrytning i texten som man skriver kan man använda teckenkombinationen: **`\n`**

```py
with open('textfile.txt', 'a') as textfile:
    textfile.write('Hello world!\n')
    textfile.write('Hello again!')
```

### **Lägeskoder vid öppning av filer**

| Lägeskod | Betydelse | Exempel | Kommentar |
| :---- | :---- | :---- | :---- |
| `"r"` | Läsning (read) | `open("fil.txt", "r")` | Filen måste redan finnas |
| `"w"` | Skrivning (write) | `open("fil.txt", "w")` | Skriver över hela filen |
| `"a"` | Append (lägg till) | `open("fil.txt", "a")` | Skriver i slutet av filen |
| `"b"` | Binärt läge | `open("bild.png", "rb")` | För filer som inte är text |
| `"x"` | Skapa ny fil | `open("nyfil.txt", "x")` | Fel om filen redan finns |

## **Felhantering**

En viktig del i programmering är att hantera eventuella fel som kan uppstå i ens program. 

### **Tre typer av fel**

| Typ av fel | När det uppstår | Kan fångas med try/except? | Exempel |
| :---- | :---- | ----- | :---- |
| Syntaxfel | När programmet tolkas | ❌ Nej | Saknat kolon, fel indentering |
| Körningsfel (Exception) | Under körning | ✅ Ja | ZeroDivisionError, ValueError, NameError |
| Logiskt fel | Under körning (utan krasch) | ❌ Nej | Fel formel, fel algoritm |

Körningsfel (**exceptions**) kan fångas upp och hanteras med **`try`**/**`except`**.

### **Try och except**

Den kod man misstänker kan utlösa ett körningsfel sätts i ett kodblock under `try`. Med **`except`** anger man vilket fel som förväntas och i ett kodblock under anger man hur felet ska hanteras.

```py
try:
  age = int(input("Hur gammal är du?"))
  
except ValueError:
  print("Du måste ange ett heltal!")
  exit()
```

### **Felaktig input \- försök igen**

Ett sätt att hantera felaktig input är att be användaren att försöka igen. Det går att göra med en evig loop som bryts (med **break**) när inget fel inträffar.

```py
while True:
  try:
    age = int(input("Hur gammal är du?"))
    break
    
  except ValueError:
    print("Du måste ange ett heltal.")

print(f"Du är {age} år gammal!")

```

### **Några vanliga exceptions**

| Feltyp | När det händer | Exempel |
| :---- | :---- | :---- |
| `ValueError` | När ett värde inte kan tolkas korrekt | `int("hej")` |
| `TypeError` | När du blandar fel datatyper | `"hej" + 5` |
| `ZeroDivisionError` | När du dividerar med noll | `10 / 0` |
| `IndexError` | När du försöker nå ett index som inte finns | `lista[10]` |
| `KeyError` | När en nyckel saknas i en dictionary | `min_dict["namn"]` om nyckeln inte finns |
| `FileNotFoundError` | När du försöker öppna en fil som inte finns | `open("saknas.txt")` |
| `NameError` | När en variabel inte är definierad | `print(x)` utan att `x` finns |
| `AttributeError` | När ett objekt saknar ett visst attribut | `"hej".append("då")` |
| `ImportError` | När ett importerat paket inte hittas | `import felpaket` |

