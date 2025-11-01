# Fortsättning Python

## **Dataformatet JSON**

**JSON** står för JavaScript Object Notation och är (precis som CSV) ett **textbaserat format för att lagra och utbyta data**. Det används ofta när data ska skickas mellan en server och en webbläsare eller sparas i filer. (Till exempel konfigurationsfiler för program eller sparfiler för spel.)

### **JSON-formatet**

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

### **Läsa och tolka JSON-data från fil**

Här finns den JSON-fil som används i exemplet: 🔗[movies.json](http://data/movies.json)

```py
import json

# Öppna och läs filen
with open("movies.json", "r", encoding="utf-8") as file:
    # Avkodar JSON till Python-objekt (lista med dictionaries)
    data = json.load(file)  

# Skriv ut titlar och årtal
for movie in data:
    print(movie["title"], "-", movie["year"])
```

### **Spara Python-data som JSON**

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

## **OOP \- Objektorienterad programmering**

Objektorienterad programmering (OOP) i Python är ett sätt att **strukturera kod med hjälp av objekt.** Objekt representerar oftast verkliga saker eller koncept (till exempel en produkt, användare, NPC etc). OOP gör koden mer modulär, återanvändbar och lättare att underhålla.

### **Begrepp inom OOP**

* **Klass (class):** En mall eller "ritning" för objekt.  
  Definierar attribut (variabler) och metoder (funktioner).  
* **Objekt (instanser):** en konkret tillämpning av en klass, t.ex. en specifik produkt, en specifik NPC etc.  
* **Attribut:** variabler kopplade till en klass/objekt som beskriver objektets tillstånd (t.ex. färg, namn, ålder). Varje objekt kan ha sina egna värden på attributen.  
* **Metoder:**  funktioner som definieras i en klass och kan användas på objekt.

### **Exempel på en enkel klass**

```py
# Definiera en klass
class Dog:
    def __init__(self, name, age):
        self.name = name    # attribut
        self.age = age

    def bark(self):         # metod
        print(f"{self.name} säger: Voff!")

# Skapa objekt (instanser)
elmo = Dog("Elmo", 3)
buddy = Dog("Fido", 5)

# Använda metoder och attribut
elmo.bark()        # Output: Elmo säger: Voff!
print(buddy.age)   # Output: 5

```

## **Mer avancerad hantering av listor**

### **Funktionen `zip` \- para ihop värden från listor**

Funktionen `zip` kan användas för att para ihop värden från två listor eller tuplar. (Funktionen funkar även med samlingen set, men då garanteras inte ordningen av värdena.)

Det funktionen returnerar är ett zip-objekt som sedan kan konverteras till den samling man önskar (dict, tupel eller lista).

```py
days = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']
food = ['kebab', 'pizza', 'sushi', 'meatballs', 'tacos']

menu = zip(days, food)
menu = dict(menu)

print(menu)

# {'Måndag': 'kebab', 'Tisdag': 'pizza', 'Onsdag': 'sushi', 
# 'Torsdag': 'meatballs', 'Fredag': 'tacos'}
```

### **Uppackning (unpacking) av samlingar**

Ibland vill man ta en lista (eller tupel) och tilldela dess värden till enskilda variabler. Det går att göra genom att ange flera variabelnamn separerade med kommatecken och tilldela dem listan:

```py
user = ['Markus Pettersson', 'marpet', 'supersecret']

name, username, password = user

print('Namn:', name)
print('Användarnamn:', username)
print('Lösenord:', password)
```

### **Enumerate**

Ibland vill man iterera/gå igenom en lista och samtidigt ha tillgång till en räknare. T.ex. om man vill rangordna något, som favoritfilmer t.ex. Detta går att göra på flera olika sätt. Här använder man längden på listan i en range-funktion:

```py
# Sämre exempel 1
fav_movies = ['Toy Story 2', 'Toy Story', 'Finding Nemo', 'Inside Out']

for i in range(0, len(fav_movies)):
  movie_title = fav_movies[i]
  print(i + 1, movie_title)
```

Man kan också använda en separat variabel som räknare:

```py
# Sämre exempel 2
fav_movies = ['Toy Story 2', 'Toy Story', 'Finding Nemo', 'Inside Out']

counter = 1

for movie in fav_movies:
  print(counter, movie)
  counter += 1
```

Ett smidigare sätt är att använda funktionen **`enumerate`** för att iterera en lista och samtidigt få tillgång till en räknare. Med argumentet **`start`** kan man räknarens startvärde. 

```py
# Smartare exempel
fav_movies = ['Toy Story 2', 'Toy Story', 'Finding Nemo', 'Inside Out']

for number, movie in enumerate(fav_movies, start=1):
  print(number, movie)
```

### **Sortera en lista av dictionaries**

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

print(ranking)
```

### **List comprehension**

List comprehension är ett sätt att med kompakt syntax skapa en ny lista baserat på värden från en annan lista. I exemplet går man igenom listan med frukter och metoden **`upper()`** körs för varje frukt. 

```py
# Gå igenom en lista och gör alla strängar till VERSALER

fruits = ['apple', 'banana', 'kiwi', 'pear', 'pineapple']
upper_fruits = [f.upper() for f in fruits]

print(upper_fruits)

# → ['APPLE', 'BANANA', 'KIWI', 'PEAR', 'PINEAPPLE']

```

### **Filtrera med list comprehensions**

Med list comprehensions kombinerat med en if-sats kan man filtrera en lista. Värdet läggs bara till i den nya listan ifall villkoret är uppfyllt.

```py
fruits = ['apple', 'banana', 'kiwi', 'pear', 'pineapple']
long_fruit_names = [f for f in fruits if len(f) > 4]

print(long_fruit_names)

# → ['apple', 'banana', 'pineapple']
```

### **Skapa en ny lista utifrån en funktions returvärden**

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

### **Gå igenom två listor samtidigt**

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

### **Sammanställning av förekomst**

Med list-metoden **`.count()`** kan man räkna förekomster av ett visst värde i en lista. I exemplet räknar vi hur ofta ett visst betyg förekommer i listan grades. Med en **dict comprehesion** sammanställer vi resultatet i en dictionary.

```py
grades = ['D', 'C', 'A', 'D', 'F', 'D', 'A', 'E', 
          'B', 'D', 'E', 'E', 'F', 'E', 'B', 'F']

grade_options = ('A', 'B', 'C', 'D', 'E', 'F')

summary = {g: grades.count(g) for g in grade_options}
print(summary)

# {'A': 2, 'B': 2, 'C': 1, 'D': 4, 'E': 4, 'F': 3}
```

## **Set \- mängdteori och mängoperationer**

### **Set \- skillnader: `difference()`**

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

### **Set \- överlappande: `intersection()`**

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

### **Förena två set: `.union()`**

Med metoden **`.union()`** kan man förena två sätt. I exemplet nedan använder vi både **`.union()`** och **`.difference()`** för att hantera tre olika set.

```py
# Här vill vi ta reda på vilka elever i matte 5-gruppen 
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

### **Delmängd \- `issubset()`**

Om man vill se om alla värden i ett set finns i ett annat set kan man använda metoden **`.issubset()`**. (Med matematiska begrepp vill vi alltså kontrollera om en mängd är en *delmängd* av en annan mängd.)

```py
# Teknikelever
te_class = {'Adrian', 'Berit', 'Cathrine', 'Didrik', 'Eivor', 
            'Fanny', 'Gert', 'Hans', 'Igor', 'Jannike'}

# A-elever
a_students = {'Gert', 'Berit', 'Eivor', 'Fanny'}

print(a_students.issubset(te_class))

# → True
```

