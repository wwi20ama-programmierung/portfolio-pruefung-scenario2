# Portfolio-Prüfung für Programmierung 1: Die Reise des Kolumbus (2. Scenario)

## Hintergrund
Der italienische Seefahrer und Entdecker Christoph Kolumbus brach am 3. August 1492 mit seinem Schiff "Santa Maria" zu einer Reise auf, die die Entdeckung eines alternativen Seewegs nach Indien zum Ziel hatte. Auf dieser Reise mussten er und seine Besatzung mit vielen Widrigkeiten kämpfen, unter anderem einer teils stark eingeschränkten Sicht, die die Navigation der Schiffe erschwerte.

Trotzdem hatte Kolumbus es sich zum Ziel gesetzt, bei jeder Sichtung eines Hafens diesen anzufahren, um möglichst viele Informationen, die für die weitere Reise relevant sein könnten, von den dort lebenden Menschen zu sammeln.

Zum 529. Jubiläum seiner Reise soll eine Simulation präsentiert werden, mit deren Entwicklung Sie beauftragt wurden. Dabei hat Ihr Auftraggeber bereits einen Python-Prototyp entwickelt, der Ihnen als Vorlage für die Funktionalität dienen soll - das endgültige Programm soll allerdings in Java implementiert werden.

## Aufgabenstellung
Machen Sie sich mit der Funktionsweise des Python-Programms vertraut. "Übersetzen" Sie anschließend dieses Programm in ein objektorientiertes Java-Programm. Übernehmen und erweitern Sie auf dieser Basis die im Grundgerüst vorhandenen Klassen mit dem zur Erfüllung der Anforderungen des Auftragsgebers nötigen Logik.

**Hinweis:** Ihr Auftraggeber möchte das Programm nach Fertigstellung von unabhängiger Stelle überprüfen lassen - dabei wird auch die Codequalität beachtet! Zudem soll das Schiff auf die unterschiedlichsten Situationen und Karten reagieren können und **immer** alle Häfen besuchen.

## Organisatorisches

### Abstimmungstermin
- Pro Gruppe ein Termin, bei dem der jeweilige Zwischenstand besprochen wird
- Ziel: Prüfung der Eigenständigkeit sowie andererseits wollen wir Tipps bzw. Beratung durch den Dozenten
- Der Zeitpunkt darf von der Gruppe selbst bestimmt werden.
- Die Bearbeitung muss zu diesem Zeitpunkt noch nicht vollständig sein.
- Jedes Gruppenmitglied muss teilnehmen und etwas (sinnvolles) zur Diskussion beitragen

### Abgabe
- Spätestens am **26.03.2021 um 23:59 Uhr (CET)** über Moodle
- ZIP-Datei mit Quellcode (`.java`-Dateien) und Dokumentation (PDF)
- Moodle-Abgabe (ein/e Verantwortliche/r pro Team)
- Namen und Matrikelnummern der Teammitglieder auf Deckblatt der Dokumentation nennen

## Bewertungskriterien

### Dokumentation
- **Sprache:** Deutsch
- **Deckblatt:** Namen und Matrikelnummern der Teammitglieder
- **Umfang:** Keine Vorgabe für minimale oder maximale Seitenanzahl, ca. 10 Seiten sind realistisch
- **Ziel:** Gesamtkonzept beschreiben
  - Klassendiagramm (UML) mit Klassen, Attributen, Methoden, Sichtbarkeiten und Beziehungen
  - Vorgehen und Umsetzung von Steuerungslogik des Schiffes beschreiben und erklären
  - Entscheidungen (z. B. für Datenstrukturen) erklären

### Funktionalität
Es sind mehrere Karten mit unterschiedlicher Schwierigkeit in Form von Textdateien vorgegeben.
Ihr Java-Programm sollte möglichst viele dieser Test-Karten lösen können.
Außerdem werden wir Ihre Abgabe mit weiteren, ähnlichen, Karten testen.

Im Detail wird in der in Java vorgegebenen Main-Methode ein Schiff, eine Umgebung und ein Logbuch erzeugt. Das Schiff-Objekt ist dabei die Steuerungsentität, es entscheidet selbst, wann es alle Häfen angefahren hat.

Das Schiff soll bei jeder Bewegung die zu fahrende Differenz in x- und y-Richtung liefern, wobei es immer nur erlaubt ist, eine Bewegung in jede Richtung zu machen.
Es wird erwartet, dass durch das Schiff ein Weg angegeben wird (und am Ende im Logbuch steht), der alle Häfen auf der Karte anfährt (siehe Python-Vorgabe).

→ Details ergeben sich aus Python-Code. Das Verständnis des vorgegebenen Codes gehört zur Aufgabe dazu!

| Symbol | Beschreibung |
| :--- | :--- |
| ` ` | Wasser |
| `H` | Hafen |
| `#` | Land |
| `S` | Schiff |

### Codequalität
- Einheitliche Formatierung (Klammern, Einrückung usw.)
- Sinnvolle Kommentare im Code
  - Kurzbeschreibungen der wichtigsten Methoden ("**was** macht die Methode?")
  - an komplizierten Stellen Erklärungen der Funktionsweise ("**wie** wird das in der Methode umgesetzt?")
- (Sinnvolle) Anwendung von Prinzipien der Objektorientierung
- Verwendung adäquater Datentypen
- Sinnvolle Attributs- und Methodennamen
- Namenskonventionen und Schreibweisen beachten


## Deadlines
- Start der Bearbeitung ist **Montag, 01.03.2021, 00:00 Uhr (CET)**
- Terminvereinbarung zu **verpflichtendem** Abstimmungstermin bis spätestens 14.03.2021
- Abgabe von Dokumentation und Code spätestens am **26.03.2021 um 23:59 Uhr (CET)** über Moodle