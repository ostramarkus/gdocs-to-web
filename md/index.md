## Programmering med Python

### **Vad är programmering?**

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

Python innehåller också ett stort antal **inbyggda moduler** – färdiga kodbibliotek som kan användas för vanliga uppgifter utan att du behöver skriva all kod själv. Exempel är `random` för slumpmässiga tal, `math` för matematiska funktioner, och `datetime` för datum och tid. 

Dessutom finns **externa moduler** som du kan installera, till exempel `Pillow` för bildhantering, `Flask` för webbappar och `NumPy` och `Pandas` för dataanalys. Genom att använda moduler kan man bygga kraftfulla program snabbare och dra nytta av andras färdiga lösningar.

Genom att kombinera dessa byggstenar kan man skapa allt från enkla beräkningar till avancerade program och system.

##  **Varför Python?**

**Python** är ett av världens mest använda programmeringsspråk. Det är känt för att vara **enkelt att läsa och förstå**, vilket gör det särskilt lämpligt för nybörjare, men det används också professionellt inom många olika områden.

Python används bland annat till:

* Dataanalys och artificiell intelligens (t.ex. med biblioteken *Pandas*, *NumPy*, *TensorFlow*).  
* Webbutveckling (t.ex. med *Flask* eller *Django*).  
* Automatisering och scripting (för att bearbeta filer eller hantera data).  
* Grafik, visualisering och spelutveckling.  
* Vetenskapliga beräkningar och forskning.

## **Om denna guide**

I denna guide ligger fokus på tydliga kodexempel \- förklarande texter hålls korta. Syftet är att guiden ska kunna användas praktiskt som en referens eller "kokbok" när det gäller programmering med Python.

### **Guidens fyra delar**

* **Grunder** \- här tas grunderna i Python upp: variabler, datatyper, if-satser, loopar, funktioner etc. Här finns också exempel från modulerna datetime, csv och random.  
* **Fortsättning** \- denna del bygger vidare med exempel på hur man skapar egna moduler, hanterar JSON-data, objektorienterad programmering, list comprehensions och mer avancerad list-bearbetning. Här tas också datatypen set upp och hur man arbetar med mängder.  
* **Tillämpning** \- denna del visar hur man kan använda programmeringen i praktiska tillämpningar: bildbearbetning, skapa webbappar, dataanalys, visualisering, web scraping etc.  
* **Verktyg** \- denna del tar upp de verktyg som används inom programmering, versionshantering med Git och GitHub, virtuella maskiner i Github Codespaces, vanliga kommandon i Linux-terminalen etc.

### **Färgkoder för att visa nivån**

De flesta delar av guiden är färgkodade för att visa svårighetsnivån på innehållet:  

⏺ **Grönt** står för att det är grundläggande kunskap som man bör vara väl förtrogen med. Det här är sådant som man troligtvis vill lära sig utantill för att kunna arbeta effektivt med programmering.

**⏹ Gult** betyder att exemplet är lite mer avancerat, eller att det som exemplet tar upp inte är lika grundläggande. Man bör förstå dessa exempel, men det är inget som man behöver kunna utantill.

**◆ Rött** betyder att det som tas upp är ännu mer avancerat, eller är något som inte är så vanligt förekommande inom Python på nybörjarnivå.

