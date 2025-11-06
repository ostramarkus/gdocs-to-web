# Utvecklingsmiljö och verktyg

## **Git, GitHub och GitHub Codespaces**

### **Vad är git?**

**Git** är ett **versionshanteringssystem** som används för att spara och hålla ordning på förändringar i kod. Det gör det möjligt att se tidigare versioner, jämföra ändringar och samarbeta med andra utan att skriva över varandras arbete. Git används ofta tillsammans med plattformar som **GitHub** eller **GitLab** för att dela och samarbeta kring kod online.

### **GitHub Codespaces**

GitHub Codespaces är en **molnbaserad utvecklingsmiljö** – du programmerar direkt i webbläsaren (eller i VS Code) och har redan **Git** och **GitHub** färdigintegrerat.  
Du kan börja jobba med versionhantering direkt utan att installera något.

### **Kom igång med GitHub och Codespaces**

### **1\. Skapa ett GitHub-konto**

Gå in på [https://github.com](https://github.com/) och skapa ett nytt konto. Använd gärna din edu-adress.

### **2\. Skapa ett nytt GitHub-repo**

Ett **repo** (kort för *repository*) är i GitHub **en plats där all din kod och dess historik sparas**. Det är alltså både en mapp med filer och en logg över alla ändringar som har gjorts i dessa filer.

1. Klicka på **`+`** knappen uppe till höger (Create new) och välj New Repository. (Eller gå direkt till [github.com/new](https://github.com/new))  
2. Ge projektet ett namn (t.ex. **`python-projekt`** eller **`webbapp`**) (och eventuellt en kort beskrivning).  
3. Klicka på **Create repository**

### **3\. Öppna i Codespaces**

När ditt repo är skapat:

1. Klicka på den gröna knappen “\<\> Code”

2. Välj fliken **Codespaces**

3. Klicka på “**Create codespace on main**”

Detta skapar en virtuell maskin och öppnar en **VS Code-liknande miljö i webbläsaren** – med Git och Python installerat.

### **4\. Spara och versionshantera med Git**

När du ändrar filer i Codespaces kan du använda Git direkt i den inbyggda terminalen eller via det grafiska gränssnittet i VS Code.

### **Alternativ 1: Via terminal**

#### **Se vilka filer som ändrats:**

```shell
git status
```

#### **Lägg till filerna du vill spara:**

```shell
git add .
```

#### **Skapa en commit (en sparad version):**

```shell
git commit -m "Lade till min första Python-fil"
```

#### **Skicka ändringarna till GitHub:**

```shell
git push
```

### **Alternativ 2: Via VS Code-gränssnittet**

1. Klicka på **Source Control-ikonen** (med gren-symbol) i vänstermenyn. Du ser en lista med ändrade filer.  
2. Klicka på **\+** för att lägga till (stage) filerna.  
3. Skriv ett **commit-meddelande** överst, t.ex. *“Lade till index.html”*.  
4. Klicka på **Commit** (eller `Ctrl+Enter`).  
5. Klicka på **Sync Changes** (🔁) för att pusha till GitHub.

## **Avancerat: arbeta i grenar (branches)**

Att skapa grenar är lika enkelt i Codespaces.

#### **Skapa en ny branch med terminalen**

```shell
git checkout -b ny-funktion
```

Du är nu i en ny gren. Gör dina ändringar, committa, och skicka upp till GitHub:

#### **Skicka en ny branch till GitHub**

```shell
git push --set-upstream origin ny-funktion
```

### **Med VS Code-gränssnittet:**

1. Klicka på branch-namnet längst ner i statusfältet (oftast “main”).

2. Skriv in ett nytt namn för din gren, t.ex. **`ny-funktion`**.

3. Tryck Enter – Codespaces byter automatiskt gren.

När du är klar kan du gå till **GitHub-sidan** för projektet och skapa en **Pull Request** för att slå ihop din gren med **`main`**.

### **Hämta uppdateringar**

Om någon annan ändrat något i projektet:

```shell
git pull
```

eller klicka på **Sync Changes** igen.

### **Vanligt arbetsflöde i Codespaces**

| Steg | Vad du gör | Kommando / Knapp |
| ----- | :---- | :---- |
| **1\.** | Gör ändringar i filer | – |
| **2\.** | Kolla status | **`git status`** |
| **3\.** | Lägg till filer | **`git add`** **`.`** eller “+” i Source Control |
| **4\.** | Skriv commit-meddelande | **`git commit -m "Beskriv ändringen"`** |
| **5\.** | Skicka till GitHub | **`git push`** eller “Sync Changes” |
| **6\.** | Hämta ny kod | **`git pull`** eller “Sync Changes” |
| **7\.** | Testa idéer i ny gren | **`git checkout -b gren-namn`** |

## **Linux och terminalen**

De flesta servrar kör operativsystemet Linux (där den populäraste varianten är [Ubuntu](https://ubuntu.com/)). Servrarna har oftast inte grafiska gränssnitt utan man interagerar med systemet med hjälp av textkommandon. Textgränssnittet benämns med flera olika namn: *terminal, kommandotolk* eller *konsolen* (och även **shell** eller **bash**).

### **Vanliga kommandon**

#### ***För att navigera***

| `ls` | Visa filer och mappar i aktuell mapp |
| :---- | :---- |
| **`ls -l`** | Visa detaljerad lista över filer och mappar |
| **`ls -lR`** | Visa alla filer och mappar i underliggande mappar |
| **`cd mapp`** | Gå in i undermapp |
| **`cd ..`** | Gå upp ur mappen (upp ett steg) |
| **`cd`** | Gå till hemkatalog |
| **`cd /`** | Går till rotkatalogen |
| **`pwd`** | Skriver ut sökvägen till den aktuella mappen |
| **`clear`** | Rensar skärmen |
| **`man kommando`** | Visar manualsidorna för ett kommando/program |
| **`exit`** | Loggar ut |

#### ***Git \- versionshantering***

| `git status` | Visar vilka filer som har ändrats |
| :---- | :---- |
| **`git add .`** | Lägg till alla ändrade filer till *stage-*area |
| **`git commit -m 'Meddelande'`** | Skapar en *sparpunkt*. Meddelandet bör beskriva vad man gjort |
| **`git push`** | Skicka ändringar till ens repository |
| **`git pull`** | Hämta eventuella uppdateringar från ens repository |

#### ***För att skapa/redigera filer/mappar***

| `mkdir mappnamn` | Skapar en mapp (kallas för *directory* i Linux) |
| :---- | :---- |
| **`touch filnamn`** | Skapar en tom textfil (eller uppdaterar tidsstämpel för en existerande fil eller mapp) |
| **`rm filnamn`** | Raderar en fil |
| **`rmdir`** | Raderar en (tom) mapp |
| **`rm -rf`** | Raderar mappen och allt innehåll |
| **`chmod XXX fil`** | Ändrar rättigheterna till filen/mappen – [verktyg för att skapa kod](http://www.onlineconversion.com/html_chmod_calculator.htm) |
| **`nano filnamn`** | Öppnar textredigeraren nano |
| **`cat filnamn`** | Skriver ut innehållet i en fil |
| **`chown användarnamn filnamn`** | Ändrar ägaren till en fil |

#### ***Textredigeraren nano***

| `nano filnamn` | Öppnar filen i textredigeraren nano |
| :---- | :---- |
| **`Ctrl+o`** | Sparar fil |
| **`Ctrl+x`** | Stäng |

#### ***ctrl-d, ctrl-z och ctrl-c***

| `ctrl-d` | Avslutar input (t.ex. ett meddelande, mail, chatt etc) |
| :---- | :---- |
| **`ctrl-z`**  | Stoppar/pausar ett program/kommando tillfälligt |
| **`ctrl-c`** | Avslutar ett program/kommando |

####  ***Övriga kommandon***

| date | Visar aktuellt datum och tid |
| :---- | :---- |
| **groups** | Visar vilka grupper den man tillhör |

## **Pakethantering och virtualenv**

## **Unit testing/enhetstestning**

## **Notebooks**

