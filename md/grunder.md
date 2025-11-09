# Grunderna i Python

## **Vad är programmering?**

Programmering handlar om att ge datorn instruktioner, steg för steg,  för att lösa problem eller utföra uppgifter. Dessa instruktioner skrivs i ett **programmeringsspråk**, till exempel Python. Datorn följer instruktionerna i tur och ordning, rad för rad, vilket kallas att koden **körs sekventiellt**.

### **Ett programs byggstenar: satser och uttryck**

Ett program består av **satser** och **uttryck**. En **sats** (eng. *statement*) är en instruktion som gör något, till exempel att skriva ut text på skärmen med `print("Hej!")` eller att tilldela ett värde till en variabel med `x = 5`. 

Ett **uttryck** (eng. *expression*) är en del av koden som beräknar ett värde, till exempel `3 + 5` eller `x * 2`. Man kan tänka sig att ett uttryck **ger** ett värde, medan en sats **gör** något. I många fall används uttryck inuti satser, till exempel `print(x + 2)` där uttrycket `x + 2` beräknas innan resultatet skrivs ut.

### **Kontrollstrukturer \- styra flödet i programmet**

För att styra i vilken ordning saker sker i ens program används **kontrollstrukturer** – till exempel **villkor** (`if`\-satser) för att fatta beslut, och **loopar** (`for` och `while`) för att upprepa kod flera gånger.

### **Lagring av information \- variabler och datastrukturer**

Information i ett program sparas i **variabler**, som är namn på platser i datorns minne där värden kan lagras. Värdena kan vara av olika **datatyper**, som heltal, decimaltal (float), text (strängar) eller booleska värden (sant/falskt). När man behöver lagra flera värden används **datastrukturer** som listor, tupler, dictionaries eller set (sv. *mängder*).

### **Struktur av program \- funktioner, klasser, egna moduler**

För att göra program tydligare och enklare att underhålla kan man dela in koden i **funktioner**, **klasser** och **moduler**. En **funktion** samlar kod som utför en viss uppgift, så att den kan återanvändas flera gånger. **Klasser** används för att samla data (variabler) och körbar kod (funktioner) och på så sätt strukturera sitt program enligt objektorienterade principer. **Moduler** gör det möjligt att dela upp större program i flera filer, vilket gör koden mer organiserad och lättare att samarbeta kring.

### **Använda moduler för utökad funktionalitet**

Python innehåller ett stort antal **inbyggda moduler** – färdiga kodbibliotek som kan användas för vanliga uppgifter utan att du behöver skriva all kod själv. Exempel är `random` för slumpmässiga tal, `math` för matematiska funktioner, och `datetime` för datum och tid. 

Dessutom finns **externa moduler** som du kan installera, till exempel `Pillow` för bildhantering, `Flask` för webbappar och `NumPy` och `Pandas` för dataanalys. Genom att använda moduler kan man bygga mer avancerade program snabbare och dra nytta av redan färdiga lösningar.

## **Varför Python?**

**Python** är ett av världens mest använda programmeringsspråk. Det är känt för att vara **enkelt att läsa och förstå**, vilket gör det särskilt lämpligt för nybörjare, men det används också professionellt inom många olika områden.

Python används bland annat till:

* Dataanalys och artificiell intelligens (t.ex. med biblioteken *Pandas*, *NumPy*, *TensorFlow*).  
* Webbutveckling (t.ex. med *Flask* eller *Django*).  
* Automatisering och scripting (för att bearbeta filer eller hantera data).  
* Grafik, visualisering och spelutveckling.  
* Vetenskapliga beräkningar och forskning.

## 

## **Variabler och datatyper**

Variabler används för att lagra information. Variabler är av olika **datatyper** beroende på vilken typ av värden som lagras.

### **⏺ De vanligaste datatyperna**

| Datatyp | Exempel | Förklaring |
| :---- | :---- | :---- |
| **str** (string / text) | `name = "Elmo"` | Textsträngar, skrivs inom `" "` eller `' '`. |
| **int** (heltal) | `x = 5` | Heltal, utan decimaler. Kan vara positiva eller negativa. |
| **float** (flyttal) | `y = 3.14` | Tal med decimaler. |
| **bool** (boolean) | `is_happy = True` | Kan bara vara `True` eller `False`.  |

#### **⏺ Definiera variabler**

Variabler skapas (*initialiseras*) och tilldelas ett värde med likamedstecknet: **`=`**.

```py
# Sträng / str
my_string = 'Hello World'

# Heltal / int
my_int = 42	

# Decimaltal / float
my_float = 3.14			
```

### **⏹ Namngivning av variabler**

Namnet på variabler väljer man själv. Det finns dock några regler man bör hålla sig till:

* Ett variabelnamn bör vara **beskrivande** och ge information om vad variabeln är till för eller vad den innehåller. Undvik namn som till exempel **`variabel1`**.  
* Ett variabelnamn kan **inte börja** på en **siffra** eller ett **specialtecken** (förutom understreck: **`_`**).   
* Man kan **inte** ha **mellanslag** eller i **minustecken** i variabelnamn.  
* **Undvik internationella tecken** i variabelnamn.   
* För mer seriösa program bör variabelnamnen vara på **engelska**.

#### **⏺ Omvandla mellan datatyper**

Man kan omvandla värden/variabler mellan olika datatyper. (Eng: *type conversion* eller *type casting.*)

```py
# Gör om ett värde till en textsträng
my_string = str(42)

# Gör om ett värde till ett heltal
my_int = int(13.3)	
		
# Gör om ett värde till ett decimaltal
my_float = float('3.14')	
```

#### **⏹ Ta reda på datatyp**

Med funktionen **`type()`** kan man ta reda på datatypen för en variabel.

```py
name = 'Markus'
print(type(name))

# → <class 'str'>
```

#### **⏺ Räkna med variabler**

Variabler kan användas i beräkningar. Parenteser **`()`** kan användas för att kringgå prioritetsregler.

```py
x = 100
my_sum = 100 + x
result = (20 + 10) * x
```

#### **⏺ Aritmetiska operatorer**

Tecken som används i beräkningar kallas för **aritmetiska operatorer**.

|  | Förklaring |
| :---: | :---- |
| **`+`** | Addition |
| **`-`** | Subtraktion |
| **`*`** | Multiplikation |
| **`/`** | Division |
| **`//`** | Division med avrundning nedåt. (*floor-division*) |
| **`**`** | Upphöjt |
| **`%`** | Modulo / rest från division |
| **`+=`** | Addera till |
| **`-=`** | Subtrahera från |

#### **⏺ Addera eller subtrahera variabler**

Teckenkombinationerna **\+=** och **\-=** kan användas för att (med mer kompaktare syntax) öka eller minska en variabels värde. (Eng. *increment* respektive *decrement*.)

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

#### **⏺ Skriva ut med `print()`**

Funktionen **`print()`** skriver ut text till terminalfönstret. 

```py
print('Hello World!')
```

#### **⏺ Skriv ut flera värden med kommatecknet**

Man kan ange flera värden att skriva ut med hjälp av kommatecknet. Man får då ett automatiskt mellanslag mellan värdena. (Det ingen roll vilken **datatyp** värdena är.)

```py
name = 'Markus'
score = 100

print('Hello', name, 'Your score:', score) 
# → 'Hello Markus Your score: 100'
```

#### **◆ Skriv ut utan att skapa en ny rad**

Om man vill skriva ut fler värden på samma rad kan man ange en tom sträng för argumentet **`end`** i print-funktionen.

```py
print('One ', end="")
print('Two ', end="")
print('Three')

# → 'One Two Three'
```

#### **⏺ Input-funktionen**

Funktionen **`input()`** pausar programmet och väntar på text-input från användaren. Den input man får lagrar man oftast i en variabel. 

**OBS\!** Den data man får från en input-funktion är alltid en textsträng/**`str`**.

```py
name = input('Vad heter du?')
```

#### **⏹ Typomvandla direkt från input-funktion**

Om man vill göra beräkningar eller numeriska jämförelser med datan från en input-funktion kan man konvertera den direkt till en annan datatyp.

```py
age = int(input('Hur gammal är du?'))
```

## **Textsträngar**

#### **⏺ Sätta ihop textsträngar**

Med plustecknet kan man sätta ihop flera textsträngar. Detta kallas **konkatenering**.

**OBS\!** Alla värden måste då vara textsträngar \- annars får man ett **`TypeError`**.

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

#### **⏹ Sträng-formatering med f-strings**

F-strängar (**f-strings**) är ett relativt nytt sätt att formatera strängar i Python. Med f-strängar kan man sätta in variabler (eller andra uttryck, till exempel beräkningar) direkt i en textsträng. Man kan också ange hur variablerna ska formateras vid utskrift (t.ex. antalet decimaler eller att ett värde ska anges som procenttal.)  
**OBS\!** F-strängar skapas genom att man sätter bokstaven **`f`** före textsträngens citattecken.

```py
product = 'kexchoklad'
price = 19.9
quantity = 4

print(f'Du har köpt {product} för {price * quantity:.2f} kr.')

# → 'Du har köpt kexchoklad för 79.60 kr.'
```

🔗[Python f-string: A Complete Guide | DataCamp](https://www.datacamp.com/tutorial/python-f-string)

| Typ | Exempel | Förklaring | Resultat |
| :---- | :---- | :---- | :---- |
| Decimaler | `f"{pi:.2f}"` | 2 decimaler | `"3.14"` |
| Begynnande nollor | `f"{11:4d}"` | Lägger till nollor så att strängen blir 4 tecken | "0011" |
| Procent | `f"{0.85:.0%}"` |  | `"85%"` |
| Tusentalsavgränsning | `f"{1234567:,}"` |  | `"1,234,567"` |

#### **◆ Linjera text med f-string**

Man kan även använda f-strings för att få utskrifter på flera rader att linjera snyggt. (Bra om man skriver ut tabelldata.) Man använder då tecknen **`<`** och **`>`** (för att linjera text vänster respektive höger) följt av en siffra för att ange avståndet.

```py
fav_icecreams = [
    ['Markus', 'Daimstrut'],
    ['Stina', 'Cornetto'],
    ['Nils', 'Piggelin'],
    ['Oskar', '88']
  ]

# Skriv ut på ett prydligt sätt med f-strings
for fi in fav_icecreams:
    print(f'{fi[0]:<8} {fi[1]:>8}')

# → Markus   Daimstrut
#    Stina    Cornetto
#    Nils     Piggelin
#    Oskar          88

```

#### **⏹ Ta ut delar av en sträng**

Strängar kan på många sätt hanteras som listor. Man kan till exempel nå delar av en sträng med hakklammer **`[]`** och kolon: **`:`**. Detta kallas för **slicing**.

```py
name = 'Markus'
first_three_letters = name[0:3] 

# first_three_letters → 'Mar'
```

#### **⏹ Ändra stora/små bokstäver**

```py
name = 'Markus'

big_name = name.upper()
# → 'MARKUS'

small_name = name.lower()
# →  'markus'

cap_name = small_name.capitalize()	
# 'markus' → 'Markus'
```

#### **⏹ Sök och ersätt i text**

```py
string = 'find and replace'
new_string = string.replace('find', 'replace')

# new_string → 'replace and replace'
```

#### **⏹ Ta bort tomrum (och ny-rad-tecken) från sträng**

```py
name = '    Markus      '
new_name = name.strip()	

# new_name → 'Markus'
```

#### **◆ Kedja metoder**

Metoder som returnerar ett resultat kan man kedja ihop för att göra flera operationer direkt efter varandra. (Resultatet från en metod skickas vidare till nästa i kedjan.)

```py
ugly_name = '  mAr_kUs   '

nice_name = ugly_name.strip().replace('_', '').capitalize()
print(nice_name)

# → 'Markus'
```

#### **◆ Konvertera sträng till lista**

```py
my_string = 'ABCDEF'
my_list = list(my_string)

# my_list → ['A', 'B', 'C', 'D', 'E', 'F']
```

## 

## **Listor**

Listor är den mest flexibla *samlingen* i Python och används för att lagra flera värden som hör samman med varandra. (En listas värden kallas även för *element* eller *items.*)

En lista skapar man som en variabel med värden separerade med kommatecken. Listans värden ramas in i klammerparenteser **`[]`**.

#### **⏺ Definiera en lista**

```py
menu = ['kebab', 'pizza', 'sushi']
```

#### **⏺ Nå ett listvärde**

För att nå ett värde i listan använder man ett positionsnummer. Positionsnummer kallas även **index**. Den första positionen har **index** **`0`**. 

```py
menu = ['kebab', 'pizza', 'sushi']
first_dish = menu[0]

# first_dish → 'kebab'
```

#### **⏹ Räkna bakifrån**

Med negativa positionsnummer räknar man bakifrån från sista positionen. 

```py
menu = ['kebab', 'pizza', 'sushi']
last_dish = menu[-1]

# last_dish → 'sushi'
```

#### **⏹ Välj delar av en lista**

Med kolon **:** kan man ange ett intervall av index som man vill nå. Detta kallas för **slicing**.

```py
menu = ['kebab', 'pizza', 'sushi', 'tacos']
first_three_dishes = menu[0:3]

# first_three_dishes → ['kebab', 'pizza', 'sushi']
```

#### **⏺ Tilldela ett värde till en viss position**

```py
menu[0] = 'meatballs'
```

#### **⏺ Lägga till ett värde till en lista**

```py
menu.append('thai-food')
```

#### **⏹ Ta reda på längden på en lista eller sträng**

```py
menu = ['kebab', 'pizza', 'sushi']
nr_of_dishes = len(menu)

# nr_of_dishes → 3
```

```py
name = 'Markus'
string_size = len(name)

# string_size → 5
```

#### **⏺ Gå igenom/iterera en lista ett värde i taget**

```py
menu = ['pizza', 'kebab', 'sushi']

for dish in menu:
    print(dish)
```

#### **⏹ Skapa en lista från en textsträng**

Med metoden **`split`** kan man dela upp en textsträng i en lista. Som *argument* anger man vilket tecken som ska användas för att dela upp strängen.

```py
menu_string = 'kebab, pizza, sushi, meatballs'
menu = menu_string.split(',')

# food_list → ['kebab', ' pizza', ' sushi', ' meatballs']
```

Man kan också använda funktionen **`list`** för att dela upp en sträng bokstav för bokstav:

```py
abc_list = list('abc')

# abc_list → ['a', 'b', 'c']
```

#### **⏹ Konvertera en lista till en sträng**

```py
menu = ['kebab', ' pizza', ' sushi', ' meatballs']
menu_string = ','.join(menu)

# menu_string → 'kebab, pizza, sushi, meatballs'
```

#### **⏹ Hitta index för ett värde**

List-metoden **`index`** returnerar **index**\-numret för första förekomsten av ett värde.

```py

[1,2,3].index(2) # → 1 
[1,2,3].index(4) # → ValueError

```

#### **⏹ Nästlade listor**

Det är inte ovanligt med nästlade listor, att listor i sin tur innehåller andra listor (eng. *nested lists*). Inom matematiken kan det fenomenet kallas för *matris.* För att nå värdena från de 'inre' listorna kan man använda dubbla set av hakparanteser:

```py
lessons = [
    ["Svenska", "Engelska", "Idrott"],  # Måndag
    ["Matematik", "Historia"],          # Tisdag
    ["Programmering", "Programmering"], # Onsdag
    ["Engelska", "Matematik"],          # Torsdag
    ["Programmering", "Idrott"]         # Fredag
]

print(lessons[3][1])

# → Matematik
```

Man kan också använda dubbla for-loopar för att gå igenom listorna:

```py
lessons = [
    ["Svenska", "Engelska", "Idrott"],  # Måndag
    ["Matematik", "Historia"],          # Tisdag
    ["Programmering", "Programmering"], # Onsdag
    ["Engelska", "Matematik"],          # Torsdag
    ["Programmering", "Idrott"]         # Fredag
]

for day in lessons:
    print('Denna dags lektioner:')
    for lesson in day:
        print(lesson)

```

#### **⏹ Sortera en lista**

```py
letters = ['B', 'D', 'C', 'A']
letters.sort()

# letters → ['A', 'B', 'C', 'D']

letters.sort(reverse=True)
# letters → ['D', 'C', 'B', 'A']
```

```py
numbers = [1, 5, 2.4, 0.3, 100]
numbers.sort()

# numbers → [0.3, 1, 2.4, 5, 100]
```

#### **⏹ Kopiera lista**

Metoden **`sort`** förändrar listan som man sorterar. Om man vill ha kvar orginallistan kan man kopiera listan först med metoden **`copy`**.

```py
letters = ['D', 'E', 'A', 'B', 'C']

sorted_letters = letters.copy()
sorted_letters.sort()

print(letters)
print(sorted_letters)

# → ['D', 'E', 'A', 'B', 'C']
# → ['A', 'B', 'C', 'D', 'E']

```

#### **⏹ Räkna förekomst i lista**

Med metoden **`count()`** kan man räkna förekomsten av ett värde i en lista.

```py
grades = ['D', 'C', 'A', 'D', 'F', 'D', 'A', 'E', 
          'B', 'D', 'E', 'E', 'F', 'E', 'B', 'F']

nr_of_a = grades.count('A')

print('Antal A:', nr_of_a)

# → 'Antal A: 2'
```

#### **⏹ Summera en lista**

```py
scores = [12, 34, 56, 12, 32, 34]
print(sum(scores))

# → 180
```

#### **⏹ Max- och min-värden**

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

#### **⏹ Medelvärde**

Här används **`sum()`** och **`len()`** i kombination för att räkna ut ett medelvärde.

```py
scores = [12, 34, 56, 12, 32, 34]
print(sum(scores) / len(scores))

# → 30.0
```

## **Villkor \- if-satser**

If-satser är en så kallad **kontrollstruktur** och används för att styra flödet i ett program. En if-sats testar att ett (eller flera) **villkor är uppfyllt** och utför viss kod endast om villkoren är uppfyllda. 

Den kod som ska utföras i if-satsen kallas för **kodblock** och har 4 mellanslags indrag. (*Indentering*)

**`else`** används för att ange vad som ska göras ifall villkoret **inte** uppfylls. **`elif`** används för att kedja flera villkorstester efter varandra.

### **⏺ Vanliga operatorer för villkor**

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

#### **⏺ Jämförelse av textsträngar**

```py
name = 'Markus'

if name == 'Markus':
   print('Welcome!')
else:
   print('Go away!')

# → 'Welcome!'
```

#### **⏺ Jämförelse av numeriska värden**

```py
age = 25

if age > 20:
   print('Hello!')
else:
   print('Goodbye')

# → 'Hello!'
```

#### **⏺ Flera villkor med `and`** 

Med **`and`** kan man ange flera villkor som alla måste vara sanna.

```py
username = 'marpet'
password = 'secret'

if username == 'marpet' and password == 'secret':
    print('Welcome!')
else:
    print('Access denied!')
```

#### **⏺  Flera villkor med `or`**

Med **`or`** kan man ange flera villkor. Det räcker med att ett av villkoren är sant.

```py
if username == 'marpet' or username == 'marpet2':
    print('Welcome!')
else:
    print('Access denied!')
```

#### **⏹ Else-if \- flera jämförelser**

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

#### **⏹ If och listor**

Med en if-sats kan man kontrollera ifall ett värde finns i en lista.

```py
menu = ['kebab', 'pizza', 'meatballs']

if 'pizza' in menu:
   print('Yes! Pizza!')
else:
   print('Nooooo..... I want pizza!')

# → 'Yes! Pizza!'
```

#### **⏹ If och strängar**

Med en if-sats kan man kontrollera ifall en textsträng innehåller viss text.

```py
text = 'Python is easy!'

if 'easy' in text:
   print('Correct!')
else:
   print('You are wrong! Practice more!')

# → 'Correct'
```

#### **◆ If och funktioner**

Funktioner som returnerar **`True`** eller **`False`** (booleska värden) kan användas direkt som villkor i if-satser.

```py
if is_logged_in():
   print('Welcome!')
else:
   print('Access denied!')
```

## 

## **Loopar**

Loopar används när man vill upprepa kod i sitt program. Den kod som ska utföras i loopen *indenteras* med 4 mellanslag.

#### **⏺ En `for`\-loop med `range()`**

För att ange hur många gånger en **`for`**\-loop ska köras är det vanligt att använda en räknare (variabeln **`i`**) och funktionen **`range()`** som skapar en talserie mellan två heltal.

```py
for i in range(0, 10):
   print('I can count to:', i)
```

#### **⏺ En `for`\-loop för att gå igenom en lista/sträng**

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

#### **⏹ While-loop**

En **`while`**\-loop körs så länge ett villkor är uppfyllt.

```py
i = 0

while i < 10:
    print('I can count to:', i)
    i += 1
```

#### **⏺ Evig `while`\-loop**

Om man anger ett villkor som alltid är sant, skapas en evig loop.

```py
while True:
    input('Are we there yet?')
```

#### **⏹ Avbryta en loop med `break`** 

Man kan använda **`break`** för att avbryta en loop.

```py
while True:
    answer = input('Are we there yet?')
    if answer == 'yes':
        print('Finally!')
        break
```

#### **◆ Skapa listor med `range()`**

Funktionen **`range()`** kan även användas för att skapa en lista av talserier. Funktionen tar även ett tredje argument som anger stegstorleken (differensen) mellan talen i talserien.

```py
my_list = list(range(0, 50, 10))
print(my_list)

# → [0, 10, 20, 30, 40]
```

## 

## **Funktioner**

En *funktion* är namngiven kod som man sedan kan anropa från sitt program. Med funktioner slipper man upprepa sig när man vill göra samma sak flera gånger. Funktioner är också ett sätt att dela upp ett större program i mindre, mer lätthanterliga delar. 

#### **⏺ Egen funktion**

```py
def hello():
    print('Hello!')
    print('Have a nice day!')

hello()
```

#### **⏺ Funktion som tar emot argument**

De värden som skickas in i en funktion kallas för **argument**.

```py
def hello(name):
    print('Hello', name)

hello('Markus')
```

#### **⏺ Flera argument \- returnera ett värde**

Det är vanligt att en funktion bearbetar information för att sedan skicka tillbaka ett resultat till huvudprogrammet \- funktionen **returnerar** ett värde.

```py
def triangle_area(base, height):
    area = base * height / 2
    return area
    
my_area = triangle_area(5, 7)
print(my_area)
```

#### **⏹ Returnera booleska värden**

Det är vanligt med funktioner som returnerar **`True`** eller **`False`** (*booleska* värden).

```py
def is_weekend(day):
    if day == 'saturday' or day == 'sunday':
        return True
    else:
        return False
```

Om funktionen bara testar ett eller flera villkor behöver man inte någon if-sats. Man kan istället returnera resultatet av villkorstestet direkt:

```py
def is_weekend(day):
    return day == 'saturday' or day == 'sunday'
```

#### **◆ Funktioner med keyword-arguments**

Om man vill göra sina funktioner tydligare och flexiblare kan man använda namngivna argument (**keyword-arguments**). Då namnger man argumenten som funktionen tar emot och anger även **standardvärden (**eng. *default values*) för argumenten.

Med namngivna argument behöver man inte hålla koll på ordningen för argumenten vid  anrop av funktionen. Och med standardvärden fungerar programmet även om man utelämnar ett argument.

```py
# Funktion med keyword-arguments och default-värden
def triangle_area(base=10, height=10):
    area = base * height / 2
    return area
    
# Funktionen anropas med de namngivna argumenten
my_area = triangle_area(base=5, height=7)

# Funktionen anropas utan argument - då används standardvärdena
my_area1 = triangle_area()
```

## 

## **Dictionary \- dict**

Datatypen **dictionary** (dict) är en *samling* precis som listor. Istället för att de olika elementen representeras av ett positionsnummer (0, 1, 2 etc.) används beskrivande namn. Namnen som identifierar positionerna kallas för **keys** (sv. nycklar).

#### **⏺ En enkel dictionary**

```py
car = {'brand': 'Volvo', 'color': 'black', 'max_speed': 280}

print(car['max_speed'])
```

#### **⏺ En dictionary på flera rader**

```py
car = {
    'brand': 'Volvo', 
    'color': 'black', 
    'max_speed': 280,
    'price': 200000,
    'model_year': 2018,
}
```

#### **⏺ En lista av dictionaries**

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

#### **⏹ Gå igenom en dictionary med en `for`\-loop**

Med metoden **`items()`** kan man iterera över både **nyckeln** (*key*) och **värdet** (*value*).

```py
car = {
    'brand': 'Volvo', 
    'color': 'black', 
    'max_speed': 280,
    'price': 200000,
    'model_year': 2018,
}

for key, value in car.items():
    print(key.capitalize(), ':', value)
```

## 

## **Tuplar och set**

**Tuplar** och **set** är samlingar (*collections*) och alternativ till listor. 

De viktigaste skillnaderna mot vanliga listor:

* **Tuplar** är inte ändringsbara (de är *immutable*). Man kan alltså inte ändra dess värden efter att tupeln är skapad.  
* **Set** kan endast innehålla unika värden. De kan alltså inte innehålla dubbletter. (Set kan liknas vid det matematiska begreppet *mängd*).

#### **⏹ Definiera en tupel**

```py
my_tuple = ('kebab', 'pizza', 'meatballs')
```

#### **⏹ Definiera ett set**

```py
my_set = {'kebab', 'pizza', 'meatballs'}
```

### **⏹ Skillnaderna mellan listor, tuplar och set**

| Egenskap | List (`list`) | Tuple (`tuple`) | Set (`set`) |
| :---- | :---- | :---- | :---- |
| **Ordning** | Bevaras | Bevaras | Ingen garanterad ordning |
| **Dubbletter** | Tillåts | Tillåts | Ej tillåtna (unika element) |
| **Ändringsbar** | Ja | Nej (immutable) | Ja (men endast unika element) |
| **Sökning (`x in ...`)** | Långsammare  | Långsammare  | Mycket snabb  |
| **Använd som dict-nyckel** | Nej | Ja | Nej |
| **Vanliga användningsområden** | Listor av data som kan ändras, ordning viktig | Koordinater, fasta värden, säkra datastrukturer | Unika värden, mängdoperationer (union, snitt, skillnad) |
| **Prestanda** | Flexibel men lite långsammare | Snabbare än listor | Snabb för medlemskap och mängdlogik |

## **Kommentera kod**

För att öka tydligheten i koden (för sig själv och för andra) bör man använda *kommentarer*. För mer komplexa program brukar kommenterar för funktioner och klasser vara mer utförlig och kommentarerna används även för att automatiskt generera dokumentation över koden. (Dokumentation \= text som i detalj beskriver hur koden fungerar.)

### **⏺ Riktlinjer för kommentarer**

 Se till att **uppdatera kommentarer** ifall koden ändras:

"Comments that contradict the code are worse than no comments. Always update comments if the code changes\!"

**Undvik överflödiga** kommentarer:

"Avoid comments that are obvious from the code itself."

Använd helst **engelska** i dina kommentarer:

"Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don’t speak your language."

### **⏺ Enrads-kommentarer**

"Comments should be complete sentences. If a comment is a phrase or sentence, its first word should be capitalized, unless it is an identifier or acronym."

```py
# Beräkna summan av alla tal i listan
total = sum(numbers)
```

Enrads-kommentarer bör placeras **på en egen rad** eller **på samma rad som koden**. Eftersom Pythonkod (i jämförelse med andra språk) är lätt att läsa och förstå bör man bara kommentera kod som verkligen behöver förklaras.

### **⏹ Blockkommentarer**

"Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space."  — [PEP 8, Comments](https://peps.python.org/pep-0008/)

```py
# Loopa igenom alla användare och
# skriv ut deras namn och ålder
for user in users:
    print(user.name, user.age)
```

### **⏹ Docstrings (dokumentationssträngar)**

Docstrings är mer utförliga kommentarer som förklarar en funktion, modul eller 

"Docstrings are denoted by triple quotes `"""` and are used to describe all public classes and functions."

```py
def add(a, b):
    """Returnerar summan av två tal."""
    return a + b
```

Eller ännu mer utförligt där även **parametrar** och **returvärden** dokumenteras:

```py
def add(a, b):
    """
    Returnerar summan av två tal.

    Parametrar:
    a (int eller float): Första talet
    b (int eller float): Andra talet

    Returnerar:
    int eller float: Summan av a och b
    """
    return a + b

```

Alla citat ovan kommer från Pythons officiella stilguide: PEP (Python Enhancment Proposals) — [PEP 8, Docstrings](https://peps.python.org/pep-0008/).

## 

## **Filer: läsa och skriv**

#### **⏺ Öppna och läs in en hel textfil**

```py
with open('names.txt') as file:
    content = file.read()

print(content)
```

#### **⏺ Läs en textfil rad för rad**

Med en **`for`**\-loop kan vi gå igenom textfilen rad-för-rad. Genom att använda metoden **`strip()`** tar vi bort tecknet för "ny rad" i slutet på varje textrad.

```py
with open('names.txt') as file:
    for line in file:
        print(line.strip())
```

#### **⏹ Läs in en textfil till en lista**

```py
with open('names.txt') as name_file:
    names = name_file.readlines()
```

#### **⏹ Skriv till en textfil**

Detta tar bort eventuellt tidigare innehåll.

```py
with open('textfile.txt', 'w') as textfile:
    textfile.write('Hello world!')
```

#### **⏹ Lägg till i befintlig fil**

```py
with open('textfile.txt', 'a') as textfile:
    textfile.write('Hello world!')
```

#### **⏹ Infoga ny rad med tecknen: `\n`**

Om man vill lägga till en radbrytning i texten som man skriver kan man använda teckenkombinationen: **`\n`**

```py
with open('textfile.txt', 'a') as textfile:
    textfile.write('Hello world!\n')
    textfile.write('Hello again!')
```

### **⏹ Lägeskoder vid öppning av filer**

| Lägeskod | Betydelse | Exempel | Kommentar |
| :---- | :---- | :---- | :---- |
| `"r"` | Läsning (read) | `open("fil.txt", "r")` | Filen måste redan finnas |
| `"w"` | Skrivning (write) | `open("fil.txt", "w")` | Skriver över hela filen |
| `"a"` | Append (lägg till) | `open("fil.txt", "a")` | Skriver i slutet av filen |
| `"b"` | Binärt läge | `open("bild.png", "rb")` | För filer som inte är text |
| `"x"` | Skapa ny fil | `open("nyfil.txt", "x")` | Fel om filen redan finns |

## 

## **Modulen random**

Med modulen **`random`** kan man använda slump i sina program.

#### **⏺ Importera moduler**

Moduler som **`random`** behöver importeras innan de används. Import av moduler görs högst upp i ens kod.

```py
import random
```

#### **⏺ Slumpar ett heltal mellan vissa värden**

```py
r2 = random.randrange(10, 20)
```

#### **⏺ Slumpar ett alternativ från en lista**

```py
menu = ["pizza", "kebab", "pasta"]
food = random.choice(menu)
```

#### **⏹ Slumpar ett decimaltal mellan 0 och 1**

```py
r1 = random.random()
```

#### **⏹ Deterministisk slump \- ange seed**

Om man vill återupprepa en slumpning kan man ange en så kallad **seed** för slumpningen. Om man använder samma seed får man alltid samma resultat för slumpfunktionerna.

```py
random.seed(10)
```

#### **◆ Slumpmässigt urval ur en lista**

Om man vill slumpa fram flera värden från en lista (utan risk för dubbletter) kan man använda metoden **`sample()`** \- det man får tillbaka är en lista med ett slumpmässigt urval.

```py
import random 

# Alla elever i klassen
students = ['Anna', 'Bertil', 'Ceasar', 'David', 
            'Erik', 'Frida', 'Gert', 'Henrietta']

# Tre slumpmässiga elever
volunteers = random.sample(students, 3)

print(volunteers)
```

#### **◆ Slumpa ordningen i en lista**

Om man vill blanda en lista (slumpa ordningen av dess värden) kan man använda metoden **`shuffle`**.

```py
import random 

# Alla elever i klassen
students = ['Anna', 'Bertil', 'Ceasar', 'David', 
            'Erik', 'Frida', 'Gert', 'Henrietta']

# Blanda listan med shuffle
random.shuffle(students)
print(students)
```

## 

## **Modulen datetime**

Modulen **`datetime`** används för att hantera tid och datum.

#### **⏺ Ta fram dagens datum**

```py
import datetime

today = datetime.date.today()
```

#### **⏺ Ta fram ett annat datum**

```py
christmas = datetime.date(2025, 12, 24)
```

#### **⏹ Ta fram ett datum från en sträng i iso-format**

```py
christmas = datetime.date.fromisoformat("2025-12-24")
```

#### **⏹ Ta fram veckodag för datum**

Metoden **`weekday()`** ger veckodagens nummer. Måndag \= 0, tisdag \= 1 etc.

```py
christmas = datetime.date(2025, 12, 24)
print(christmas.weekday())

# → 2
```

#### **⏹ Räkna med datum**

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

#### **⏹ Datetime \- datum och tid tillsammans**

```py
now = datetime.datetime.now()

print(now)
# → 2025-09-16 10:05:21.723942

print(now.time())
# → 10:05:21.723942

print(now.date())
# → 2025-09-16
```

### **⏹ Översikt över modulen datetime**

| Klass | Egenskaper (attribut) | Vanliga metoder |
| :---- | :---- | :---- |
| **`date`** | `year`, `month`, `day` | `today()`, `fromisoformat()`, `weekday()`, `isoweekday()`, `isoformat()`, `replace()` |
| **`datetime`** | `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond` | `now()`, `today()`, `utcnow()`, `fromtimestamp()`, `strftime()`, `strptime()`, `date()`, `time()`, `replace()` |
| **`time`** | `hour`, `minute`, `second`, `microsecond` | `isoformat()`, `replace()` |
| **`timedelta`** | `days`, `seconds`, `microseconds` | `total_seconds()` \+ stöder aritmetik med datum/tid (\+, \-) |

## **Modulen CSV**

**CSV** (comma separated values) är ett vanligt förekommande textformat för informationsutbyte mellan olika program och system. CSV passar bäst för tabell-data och man kan exportera CSV-filer från både Excel och Google Sheets.

I CSV representeras en tabellrad av en textrad och varje cell/kolumn separeras med ett komma (eller annat valfritt tecken). 

Ett kalkylark med följande innehåll:

| id | name | age | department | salary |
| ----- | :---- | ----- | :---- | ----- |
| 101 | Alice | 28 | Engineering | 70000 |
| 102 | Bob | 35 | Marketing | 65000 |
| 103 | Charlie | 22 | Sales | 40000 |
| 104 | Diana | 45 | HR | 80000 |
| 105 | Edward | 29 | Engineering | 72000 |

… ser ut så här i CSV-format:

```
id,name,age,department,salary
101,Alice,28,Engineering,70000
102,Bob,35,Marketing,65000
103,Charlie,22,Sales,40000
104,Diana,45,HR,80000
105,Edward,29,Engineering,72000
```

#### **⏺ Läsa och tolka CSV-fil som lista**

Med metoden **`reader()`** från modulen **`csv`** läses varje rad i CSV-filen in som en lista. Genom funktionen **`next()`** hoppas första raden över (som innehåller kolumnrubrikerna).

```py
import csv

with open('employees.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for employee in reader:
        print(employee[1])
```

#### **⏺ Läsa och tolka CSV-fil som dictionary**

Med klassen **`DictReader()`** från modulen **`csv`** läses varje rad in som en **dictionary**. 

```py
import csv

with open('employees.csv', newline="") as csvfile:
  reader = csv.DictReader(csvfile)
  for employee in reader:
    print(employee['name'])
    print(employee['salary'])
```

## 

## **Felhantering**

En viktig del i programmering är att hantera eventuella fel som kan uppstå i ens program. 

### **⏹ Tre typer av fel**

| Typ av fel | När det uppstår | Kan fångas med try/except? | Exempel |
| :---- | :---- | ----- | :---- |
| Syntaxfel | När programmet tolkas | ❌ Nej | Saknat kolon, fel indentering |
| Körningsfel (Exception) | Under körning | ✅ Ja | ZeroDivisionError, ValueError, NameError |
| Logiskt fel | Under körning (utan krasch) | ❌ Nej | Fel formel, fel algoritm |

Körningsfel (**exceptions**) kan fångas upp och hanteras med **`try`**/**`except`**.

#### **⏹ Try och except**

Den kod man misstänker kan utlösa ett körningsfel sätts i ett kodblock under `try`. Med **`except`** anger man vilket fel som förväntas och i ett kodblock under anger man hur felet ska hanteras.

```py
try:
  age = int(input("Hur gammal är du?"))
  
except ValueError:
  print("Du måste ange ett heltal!")
  exit()
```

#### **◆ Felaktig input \- försök igen**

Ett sätt att hantera felaktig input är att be användaren att försöka igen. Det går att göra med en evig loop som bryts (med **break**) **när inget fel** inträffar.

```py
while True:
  try:
    age = int(input("Hur gammal är du?"))
    break
    
  except ValueError:
    print("Du måste ange ett heltal.")

print(f"Du är {age} år gammal!")
```

### **◆ Några vanliga exceptions**

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

