# Fortsättning Python

## **Egna moduler**

Ett sätt att strukturera större programmeringsprojekt är att **flytta kod till egna moduler**. På så sätt gömmer man undan onödiga detaljer som inte är relevanta för huvudflödet i programmet. Detta är en princip som i mjukvaruutveckling kallas för **abstraktion** (eng. *abstraction*).

**För att skapa en egen modul** skapar man bara en ny python-fil bland projektfilerna \- i samma mapp som ens *huvudfil*. Se till att filen har filändelsen **`.py`**. I den nya filen lägger man den kod man vill flytta från huvudprogrammet \- grupperat i **funktioner**. Namnet på filen (om man bortser från filändelsen) blir modulens namn.

Modulen importerar man sedan med **`import`** högst upp i ens *huvudprogram*. 

#### **⏺ Exempel på en egen modul**

##### **usermanager.py**

```py
import random

def create_username(fullname):
    """Generates a username based on first and last name"""
    first_name, last_name  = fullname.lower().split()
    username = first_name[:3] + last_name[:3]
    return username
    
    
def create_password(letters = 8):
    """Generate a random password"""
    consonants = list('bcdfghjklmnpqrstvwxz')
    vowels = list('aeioyu')

    password = ""
    
    for i in range(0, letters):
        if i % 2 == 0:
            password += random.choice(vowels)
        else:
            password += random.choice(consonants)

    password += str(random.randrange(10, 99))
    return password

```

Denna modul kan sedan användas på följande sätt:

##### **main.py**

```py
import usermanager

username = usermanager.create_username('Markus Pettersson')
password = usermanager.create_password()

print('Användarnamn:', username)
print('Lösenord:', password)
```

#### **⏹ Ange ett alias för importerad modul**

Om man tycker att ett modulnamn är för långt (eller för att undvika en namnkonflikt) kan man ange ett alias för moduler man importerar.

```py
import usermanager as um

username = um.create_username('Markus Pettersson')
password = um.create_password()

print('Användarnamn:', username)
print('Lösenord:', password)
```

#### **⏹ Importera enstaka funktioner**

Om man inte behöver all funktionalitet från en modul kan man importera enstaka funktioner med **`from`**:

```py
from usermanager import create_username

username = create_username('Markus Pettersson')
print('Användarnamn:', username)
```

 

## **List comprehension**

**List comprehension** är ett sätt att med kompakt syntax skapa en ny lista baserat på värden från en annan lista. I många fall kan man ersätta en **`for`**\-loop med en **list comprehension**. 

#### **⏺ Enkel list comprehension**

I exemplet går man igenom en lista med, och metoden **`upper()`** körs för varje frukt. 

```py
# Gå igenom en lista och gör alla strängar till VERSALER

fruits = ['apple', 'banana', 'kiwi', 'pear', 'pineapple']
upper_fruits = [f.upper() for f in fruits]

print(upper_fruits)

# → ['APPLE', 'BANANA', 'KIWI', 'PEAR', 'PINEAPPLE']

```

### **⏺ Filtrera med list comprehensions**

Med **list comprehensions** kombinerat med en **if-sats** kan man filtrera en lista. Värdet läggs bara till i den nya listan ifall villkoret är uppfyllt.

```py
fruits = ['apple', 'banana', 'kiwi', 'pear', 'pineapple']
long_fruit_names = [f for f in fruits if len(f) > 4]

print(long_fruit_names)

# → ['apple', 'banana', 'pineapple']
```

### **◆ Skapa en ny lista utifrån en funktions returvärden**

Här används **list comprehension** för att skapa en ny lista med de betyg som ett provresultat ger.

```py
def get_grade(score):
  ''' Return a grade (A-F) depending of test score'''
  if score  > 90:
    return 'A'
  elif score > 80:
    return 'B'
  elif score > 70:
    return 'C'
  elif score > 60:
    return 'D'
  elif score > 50:
    return 'E'
  return 'F'
 
# En lista med testresultat
scores = [23, 45, 12, 56, 78, 23, 95, 54, 82, 34, 45]

# Skapa en ny lista med betyg (baserat på testresultat)
grades = [get_grade(score) for score in scores]

print(grades)
```

### **◆ Sammanställning av förekomst**

Med list-metoden **`count()`** kan man räkna förekomster av ett visst värde i en lista. I exemplet räknar vi hur ofta ett visst betyg förekommer i listan grades. Med en **dict comprehesion** sammanställer vi resultatet i en dictionary.

```py
grades = ['D', 'C', 'A', 'D', 'F', 'D', 'A', 'E', 
          'B', 'D', 'E', 'E', 'F', 'E', 'B', 'F']

grade_options = ('A', 'B', 'C', 'D', 'E', 'F')

summary = {grade: grades.count(g) for g in grade_options}
print(summary)

# {'A': 2, 'B': 2, 'C': 1, 'D': 4, 'E': 4, 'F': 3}
```

### **⏹ Ta ut en kolumn från tabellstruktur (CSV)**

Om man har en datastruktur med listor i listor (som t.ex. en CSV-fil) och vill bara ha ut värdena från en kolumn kan man göra det enkelt med list comprehensions.

```py
column_1 = [row[0] for row in data]
```

**Scenario:** vi har enkätsvar i ett kalkylark (som vi lätt kan exportera som CSV-fil). I enkäten har 50 personer angett sina favoriter vad gäller glass, godis och maträtter. Vi vill ta reda på hur många procent som föredrar de olika glassarna.

Så här ser kalkylarket ut:

| icecream | candy | foods |
| ----- | ----- | ----- |
| cornetto | marabou mjölkchoklad | tacos |
| daimstrut | kexchoklad | husmanskost |
| cornetto | marabou mjölkchoklad | pizza |
| daimstrut | kexchoklad | sushi |
| … | … | … |

Så här ser koden ut som tar ut första kolumnen från CSV-datan och beräknar procenten:

```py
import csv

# Öppna filen
with open('favourites.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    # Hoppa över första raden (med kolumnrubriker)
    next(csvreader)
    
    # Andvänd list comprehension för att skapa en 
    # lista med första kolumnens värden
    icecream = [row[0] for row in csvreader]

# Skapa ett set med alla unika värde (alla olika glass-sorter)
unique_values = set(icecream)

# Skapa en lista med tuplar för varje glass-sort
# Första positionen i tupeln blir glassens namn, 
# den andra är andelen svar
result = [(i, icecream.count(i) / len(icecream)) for i in unique_values]

# Skriv ut resultatet på ett prydligt sätt med f-strings
for r in result:
    print(f'{r[0].capitalize():<13} {r[1]:>5.1%}')
```

## 

## **OOP \- Objektorienterad programmering**

Objektorienterad programmering (OOP) i Python är ett sätt att **strukturera kod med hjälp av objekt.** Objekt representerar ofta verkliga saker eller koncept (till exempel en produkt, användare, NPC i ett spel etc). Man kan likna ett objekt med en samling variabler och funktioner (kodstycken) som hör ihop.

OOP gör koden mer modulär, återanvändbar och lättare att underhålla. Att arbeta med klasser och objekt är också en metod för **abstraktion** \- att gömma undan detaljer för att göra helheten mindre komplex.

### **⏹ Begrepp inom OOP**

* **Klass (class):** En mall eller "ritning" för objekt. I klassen definieras attribut (variabler) och metoder (funktioner).  
* **Objekt (instanser):** En konkret tillämpning av en klass, t.ex. en specifik produkt, en specifik NPC etc.  
* **Attribut:** Variabler kopplade till en klass/objekt som beskriver objektets egenskaper (t.ex. färg, namn, ålder). Varje objekt har sina egna värden på attributen.  
* **Metoder:** Funktioner som definieras i en klass och kan användas på objekt. Vad objektet kan "göra".

### **⏹ Exempel på en klass**

```py
# Definiera en klass

class Dog:
    """A class representing a dog."""
    def __init__(self, name, age):
        self.name = name    # attribut
        self.age = age

    def bark(self):         # metod
        print(f"{self.name} säger: Voff!")


# Skapa objekt (instanser)
elmo = Dog("Elmo", 3)
fido = Dog("Fido", 5)


# Använda metoder och attribut
elmo.bark()        
print(fido.age)


# →'Elmo säger: Voff!'
# → 5
```

### **◆ Arv inom OOP**

Arv är när en **klass (child class)** tar över **egenskaper och metoder** från en annan klass (**parent class**). Det används för att **återanvända kod** och skapa **specialiserade versioner** av en klass.

```py
class Animal:
    """A class representiong an animal"""
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
      print(f'Yummy, {food}!')
      self.speak()
      
    def speak(self):
        return "Pip"
        

# Här är en klass för en hund som ärver från Animal
class Dog(Animal):
    """A class representing a dog"""
    def speak(self):
        print("Voff!")


# Här är en klass för en katt som ärver från Animal
class Cat(Animal):
    """A class representing a cat"""
    def speak(self):
        print("Mjau!")


elmo = Dog('Elmo')
sigge = Cat('Sigge')

elmo.eat('korv')
sigge.eat('fisk')
```

## 

## **Dataformatet JSON**

**JSON** står för JavaScript Object Notation och är (precis som CSV) ett **textbaserat format för att lagra och utbyta data**. Det används ofta när data ska skickas mellan en server och en webbläsare eller sparas i filer. (Till exempel konfigurationsfiler för program eller sparfiler för spel.)

Den stora skillnaden mellan JSON från CSV är att du i JSON kan ha **nästlade datastrukturer.** Du kan alltså kombinera dictionaries med listor på flera olika sätt. I exemplet nedan har vi en lista som innehåller dictionaries över filmer, varje film har i sin tur en lista för skådespelarna.

### **⏺ JSON-formatet**

* Data representeras som **nyckel–värde-par** precis som dictionaries i Python.  
* **Objekt** skrivs inom **`{ }`** (motsvarar dictionaries i Python).  
* **Listor (arrayer)** skrivs inom **`[ ]`**.  
* **Strängar** omges av dubbla citattecken `" "`.  
* **Värden** kan vara: strängar, tal, booleska (**`true`**/**`false`**), **`null`**, objekt eller listor.

### **Exempel på JSON-data**

```json
[ 
 {
    "title": "Blade Runner 2049",
    "year": 2017,
    "imdb_rating": 8.0,
    "director": "Denis Villeneuve",
    "main_cast": ["Ryan Gosling", "Harrison Ford", "Ana de Armas"]
  },
  {
    "title": "Ex Machina",
    "year": 2014,
    "imdb_rating": 7.7,
    "director": "Alex Garland",
    "main_cast": ["Domhnall Gleeson", "Alicia Vikander", "Oscar Isaac"]
  },
	...
]
```

### **⏹ Läsa och tolka JSON-data från fil**

Här finns den JSON-fil som används i exemplet: 🔗[movies.json](https://python.ostrawebb.se/data/movies.json)

```py
import json

# Öppna och läs filen
with open("movies.json", "r", encoding="utf-8") as file:
    # Avkodar JSON till Python-objekt (lista med dictionaries)
    movies = json.load(file)  

# Skriv ut titlar och årtal
for movie in movies:
    print(movie["title"], "-", movie["year"])
    main_cast = ', '.join(movie['main_cast'])
    print('Actors: ' + main_cast)
    print('------------------------------------')
```

### **⏹ Spara Python-data som JSON**

```py
import json

game_data = {
  'xp': 12,
  'play_time': 512,
  'inventory': ['diamond pickaxe', 'ender eye'],
  "location": {'x': 123, 'y': 234, 'z': 65}
}

# Spara speldata till en fil
with open("save_file.json", "w", encoding="utf-8") as file:
    json.dump(game_data, file, indent=4) 

print("Data sparad till save_file.json")
```

## 

## **Avancerad hantering av listor**

### **⏹ Funktionen `zip` \- para ihop värden från listor**

Funktionen **`zip`** kan användas för att para ihop värden från två listor eller tuplar. (Funktionen funkar även med samlingen set, men då garanteras inte ordningen av värdena.)

Det funktionen returnerar är ett zip-objekt som sedan kan konverteras till den samling man önskar (dict, tupel eller lista).

```py
days = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']
food = ['kebab', 'pizza', 'sushi', 'meatballs', 'tacos']

menu = zip(days, food)
menu = dict(menu)

print(menu)

# → {'Måndag': 'kebab', 'Tisdag': 'pizza', 'Onsdag': 'sushi', 
#     'Torsdag': 'meatballs', 'Fredag': 'tacos'}
```

### **⏹ Uppackning (unpacking) av samlingar**

Ibland vill man ta en lista (eller tupel) och tilldela dess värden till enskilda variabler. Det går att göra genom att ange flera variabelnamn separerade med kommatecken och tilldela dem listan:

```py
user = ['Markus Pettersson', 'marpet', 'supersecret']

name, username, password = user

print('Namn:', name)
print('Användarnamn:', username)
print('Lösenord:', password)
```

### **⏹ Enumerate**

Ibland vill man iterera/gå igenom en lista och samtidigt ha tillgång till en räknare. (T.ex. om man vill rangordna något, som favoritfilmer eller liknande.) Ett smidigt sätt är att använda funktionen **`enumerate`**. Då kan man iterera en lista och samtidigt få tillgång till en räknare. Med argumentet **`start`** kan man ange räknarens startvärde. 

```py
fav_movies = ['Toy Story 2', 'Toy Story', 
              'Finding Nemo', 'Inside Out']

for number, movie in enumerate(fav_movies, start=1):
    print(number, movie)# → 1 Toy Story 2
#    2 Toy Story
#    3 Finding Nemo
#    4 Inside Out
```

### **◆ Sortera en lista av dictionaries**

Här används funktionen **sorted()** i kombination med en **lambda**\-funktion (en namnlös en-rads-funktion) för att sortera en lista med dictionaries på ett av dict:ens värden (score).

```py
test_result = [
  {
    'student': 'Orvar Orvarsson',
    'class': 'TETE28',
    'score': 25
  },
  {
    'student': 'Anders Andersson',
    'class': 'TETE28',
    'score': 12
  },
  {
    'student': 'Nils Nilsson',
    'class': 'TETE28',
    'score': 42
  },  
]

ranking = sorted(test_result, key=lambda tr: tr['score'], reverse=True)
```

### **◆ Gå igenom två listor samtidigt**

Med funktionen **`zip`** och **unpacking** kan vi gå igenom/iterera två listor samtidigt.

```py
scores = [23, 45, 12, 56, 78, 23, 95, 54, 82, 34, 45]
grades = ['F', 'F', 'F', 'E', 'C', 'F', 
          'A', 'E', 'B', 'F', 'F']

for score, grade in zip(scores, grades):
    print(f"Score: {score} → Grade: {grade}")

# Score: 23 → Grade: F
# Score: 45 → Grade: F
# Score: 12 → Grade: F
# ...
```

## 

## 

## **Set \- mängdteori och mängoperationer**

### **⏺ Lägg till och ta bort från ett `set`**

```py
a_students = {'Gert', 'Berit', 'Eivor', 'Fanny'}

# Lägg till ett värde till set
a_students.add('Kjell')

# Ta bort ett värde från ett set
a_students.discard('Gert')

print(a_students)
```

### **⏹ Set \- skillnader: `difference()`**

Med metoden **`difference`** får man ett nytt **set** med *differensen* mellan mängderna*.* I exemplet nedan får vi alltså namnen på de elever som **inte** finns i båda listorna.

```py
# Alla elever i klassen
students = {'Anna', 'Bertil', 'Ceasar', 
            'David', 'Erik', 'Frida'}

# Närvarande elever
attending = {'David', 'Anna', 'Erik', 'Frida'}

# Vilka elever är frånvarande? Skillnaden mellan mängderna.
absent = students.difference(attending)

print(absent)

# → {'Bertil', 'Ceasar'}
```

### **⏹ Set \- överlappande: `intersection()`**

Med metoden **`intersection`** får man ett nytt **set** med de element som **finns** i båda seten. Inom matematiken kallas detta för ett *snitt.* 

```py
# Alla elever i klassen
students = {'Anna', 'Bertil', 'Ceasar', 
            'David', 'Erik', 'Frida'}

# Mina vänner
friends = {'Ines', 'David', 'Henrik', 'Lisa', 
           'Erik', 'Frida', 'Johan', 'Klas'}

# Vilka av mina vänner går i min klass?
friends_in_class = friends.intersection(students)

print(friends_in_class)

# → {'Frida', 'David', 'Erik'}
```

### **◆ Förena två set: `union()`**

Med metoden **`union()`** kan man förena två set. I exemplet nedan använder vi både **`union()`** och **`difference()`** för att hantera tre olika set.

```py
# Vi vill ta reda på vilka elever i matte 5-gruppen 
# som inte går teknik eller natur

# Teknikelever
te_class = {'Adrian', 'Berit', 'Cathrine', 'Didrik', 'Eivor', 
            'Fanny', 'Gert', 'Hans', 'Igor', 'Jannike'}

# Naturelever
na_class = {'Krister', 'Lars', 'Marit', 'Noah', 'Ofelia',
            'Petrus', 'Qasim', 'Rickard', 'Steve', 'Thomas'}

# Elever i matte 5
ma5_group = {'Berit', 'Igor', 'Steve', 'Ulf', 
             'Marit', 'Qasim', 'Adrian', 'Gert', 
             'Wincent', 'Noah', 'Victor', 'Hans'}
             
# Förena natur- och teknikklasserna med .union
te_and_na = te_class.union(na_class)

# Ta reda på vilka i matte 5 som inte finns i klasserna
other = ma5_group.difference(te_and_na)

print(other)

# → {'Wincent', 'Ulf', 'Victor'}
```

### **⏹ Delmängd \- `issubset()`**

Om man vill se om alla värden i ett set finns i ett annat set kan man använda metoden **`issubset`**. (Med matematiska begrepp vill vi alltså kontrollera om en mängd är en *delmängd* av en annan mängd.)

```py
# Teknikelever
te_class = {'Adrian', 'Berit', 'Cathrine', 'Didrik', 'Eivor', 
            'Fanny', 'Gert', 'Hans', 'Igor', 'Jannike'}

# A-elever
a_students = {'Gert', 'Berit', 'Eivor', 'Fanny'}

print(a_students.issubset(te_class))

# → True
```

## **Decorators** 

### **◆ Vad är en decorator?**

En **decorator** är ett sätt att “lägga till funktionalitet” till en befintlig funktion, utan att ändra själva funktionen. Det gör man genom att “omsluta” funktionen med en annan funktion som körs före eller efter huvudfunktionen.

I exemplet nedan har vi en decorator som kontrollerar om användaren är inloggad innan funktionen körs.

#### **◆ Exempel på decorator**

```py
# Simulerar en global variabel för inloggningsstatus
user_logged_in = False

# Här är vår decorator-funktion
def require_login(func):
    """Decorator checks if logged in."""
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            print("Åtkomst nekad. Du måste logga in först.")
            return
        # Om användaren är inloggad körs den riktiga funktionen
        return func(*args, **kwargs)
    return wrapper


@require_login
def view_profile():
    print("Visar användarprofilen.")

@require_login
def edit_profile():
    print("Profil uppdaterad!")


# Anropa funktionen utan att vara inloggad
view_profile()      

# Simulera en inloggning
user_logged_in = True

# Anropa funktionen som inloggad
view_profile()
```

### **◆ Varför decorators är användbara**

* De låter dig återanvända logik (t.ex. rättighetskontroller, loggning, tidsmätning) utan att upprepa kod.  
* Du kan enkelt lägga till eller ta bort funktionalitet bara genom att lägga till eller ta bort en rad (`@decorator`).  
* De används ofta i webbramverk som Flask eller Django.

### 

### 

### **◆ Vad är \*args och \*\*kwargs?**

#### **\*args**

* Står för *arguments*.  
* Används för att skicka ett **obestämt antal positionella argument** till en funktion.  
* Argumenten samlas i en **tuple**.

#### **◆ Exempel på \*args**

```py
def summa(*args):
    """Sums all arguments"""
    return sum(args)

print(summa(1, 2, 3))  # → 6
print(summa(5, 10))    # → 15
```

#### **\*\*kwargs**

* Står för *keyword arguments*.  
* Används för att skicka ett **obestämt antal namngivna argument**.  
* Argumenten samlas i en **dictionary**.

#### **◆ Exempel på \*\*kwargs**

```py
def print_key_and_value(**kwargs):
    """Print key and value from keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key} = {value}")

skriv_ut(name="Elmo", breed="Cavapoo")

# → name = Elmo
#    breed = Cavapoo

```

#### **◆ Kombination av \*args och \*\*kwargs**

```py
def exempel(*args, **kwargs):
    """Prints arguments and keyword arguments"""
    print("args:", args)
    print("kwargs:", kwargs)

exempel(1, 2, 3, a=4, b=5)

# → args: (1, 2, 3)
# → kwargs: {'a': 4, 'b': 5}
```

## **Rekursion**

*Rekursion* är när en funktion anropar sig själv, som i sin tur anropar sig själv etc. Det används inom programmering för att lösa matematiska problem eller för att gå igenom trädstrukturer som till exempel ett filsystem.

### **◆ Beräkna fakultet**

Fakulteten är summan av produkten av alla positiva heltal från 1 upp till och med ett visst nummer. Fakulteten för 5 är alltså: 1 x 2 x 3 x 4 x 5 \= 120\. En funktion som räknar ut fakulteten för ett nummer med rekursion kan se ut så här:

```py
def factorial(n):
    """Räkna ut fakulteten för ett visst nummer"""
    
    # Ifall numret är 0 eller 1 avsluta med att returnera 1
    if n == 0 or n == 1:
        return 1
    # Annars använd rekursion och anropa sig själv    
    else:
        return n * factorial(n - 1)

print(factorial(5))

# → 120
```

### **◆ Fibonnaci-serien**

Fibonaccis talföljd är en välkänd talföljd där varje tal är summan av de två föregående Fibonaccitalen. De två första talen i serien är 0 och 1\. En Fibonnaci-serie går enkelt att skapa med rekursion:

```py
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_series = [fibonacci(n) for n in range(10)]
print(fib_series)  
```

### **◆ Genomgång av filsystem**

Här används modulen **`os`** tillsammans med rekursion för att lista alla filer i en mapp. När funktionen stöter på en undermapp listas den mappen också genom att anropa funktionen igen (med rekursion).

```py
import os

def list_files(folder):
    """Skriver ut alla filer i mappen och dess undermappar."""
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path):
            print(path)  # Hittad fil
        elif os.path.isdir(path):
            list_files(path)  # Gå in i undermappen 

# Exempel: lista alla filer i mappen 'images'
list_files("images")

```

## **Kryptering**

### **◆ Enkel manuell kryptering**

Med funktionen **`ord`** för man ett teckens [Unicode](https://sv.wikipedia.org/wiki/Unicode)\-värde. (Ett heltal mellan 1 och 1114111\. ) Funktionen **`chr`** gör det motsatta \- returnerar ett tecken från ett Unicode-värde.

```py
def encode(message):
    """Returns a list of Unicode values."""
    return [ord(l) for l in message]

def decode(codes):
    """Processes a list of Unicode values. Returns a str"""
    return ''.join([chr(i) for i in codes])

coded_message = encode("I like Python")

print(coded_message)
print(decode(coded_message))

```

### **Hashing**

## **Kombinatorik**

\* Kombinationer

\* Permutationer

\* Produkt