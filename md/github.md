# GitHub Codespaces och Git

## **GitHub Codespaces**

GitHub Codespaces är en **molnbaserad utvecklingsmiljö** – du programmerar direkt i webbläsaren (eller i VS Code) och har redan **Git** och **GitHub** färdigintegrerat.  
Det betyder att du kan börja jobba med versionhantering direkt utan att installera något.

## **Kom igång med GitHub och Codespaces**

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

#### **Alternativ 1: Via terminal**

Se vilka filer som ändrats:

```shell
git status
```

Lägg till filerna du vill spara:

```shell
git add .
```

Skapa en commit (en sparad version):

```shell
git commit -m "Lade till min första Python-fil"
```

Skicka ändringarna till GitHub:

```shell
git push
```

#### **Alternativ 2: Via VS Code-gränssnittet**

Klicka på **Source Control-ikonen** (📁 med gren-symbol) i vänstermenyn.  
Du ser en lista med ändrade filer.  
Klicka på **\+** för att lägga till (stage) filerna.  
Skriv ett **commit-meddelande** överst, t.ex. *“Lade till index.html”*.  
Klicka på **Commit** (eller `Ctrl+Enter`).  
Klicka på **Sync Changes** (🔁) för att pusha till GitHub.

## **Avancerat: arbeta i grenar (branches)**

Att skapa grenar är lika enkelt i Codespaces.

#### **Terminal:**

```shell
git checkout -b ny-funktion
```

Du är nu i en ny gren. Gör dina ändringar, committa, och skicka upp till GitHub:

```shell
git push --set-upstream origin ny-funktion
```

#### **Med VS Code-gränssnittet:**

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

## **Vanligt arbetsflöde i Codespaces**

| Steg | Vad du gör | Kommando / Knapp |
| :---- | :---- | :---- |
| 1\. | Gör ändringar i filer | – |
| 2\. | Kolla status | **`git status`** |
| 3\. | Lägg till filer | **`git add`** **`.`** eller “+” i Source Control |
| 4\. | Skriv commit-meddelande | **`git commit -m "Beskriv ändringen"`** |
| 5\. | Skicka till GitHub | **`git push`** eller “Sync Changes” |
| 6\. | Hämta ny kod | **`git pull`** eller “Sync Changes” |
| 7\. | Testa idéer i ny gren | **`git checkout -b gren-namn`** |