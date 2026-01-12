// ========== PRÄSENTATIONS-TEMPLATE (16:9) ==========

// Globale Seiteneinrichtung für ein 16:9-Format.
// Wir verwenden mm für eine präzise Steuerung.
#set page(
  width: 160mm,
  height: 90mm,
  margin: (top: 7mm, bottom: 7mm, x: 10mm)
)

// Globale Texteinstellungen (Basisgröße)
#set text(size: 11pt)

// --- 1. Titelfolien-Funktion ---
// Eine dedizierte Funktion für die erste Folie.
#let title_slide(title, author, date) = {
  // Setzt den Text für diese spezifische Seite zurück
  set text(size: 11pt)
  
  // Eigener Seitenhintergrund nur für die Titelfolie
  page(
    margin: (top: 0mm, bottom: 0mm, x: 10mm) // Volle Höhe nutzen
  )[
    #v(1fr) // Vertikal zentrieren (flexibler Leerraum)
    #align(center)[
      #text(size: 24pt, weight: "bold")[#title]
      #v(1.5em)
      #text(size: 16pt)[#author]
      #v(0.5em)
      #text(size: 14pt)[#date]
    ]
    #v(1.2fr) // Etwas mehr Platz unten
  ]
}

// --- 2. Haupt-Theme-Funktion ---
// Diese Funktion kapselt die Regeln für alle Inhaltsfolien.
#let presentation_theme(body) = {
  // Setzt die Standard-Textgröße für alle Inhaltsfolien
  set text(size: 13pt)

  // Keine Nummerierung für Überschriften
  set heading(numbering: none)

  // WICHTIG: Die "Show Rule" für Folientitel.
  // Jede Überschrift der Ebene 1 (= Titel) startet eine neue Folie.
  show heading.where(level: 1): it => {
    // Schwacher Seitenumbruch (verhindert leere Startseite)
    pagebreak(weak: true)

    // Layout für den Folientitel
    align(center)[
      #text(size: 18pt, weight: "bold", fill: rgb("#333333"))[
        #it.body
      ]
      #line(length: 100%, stroke: 1pt + rgb("#CCCCCC"))
      #v(1em) // Abstand nach dem Titel
    ]

    // Alle Absätze auf Folien linksbündig (nicht Blocksatz)
    set par(justify: false)
  }

  // Standard-Styling für Aufzählungen
  set list(indent: 1.5em)
  show list.item: it => [
    #text(size: 1.2em, fill: rgb("#005A9C"))[• ] // Benutzerdefinierter Bullet
    #it.body
  ]

  // Hier wird der gesamte Inhalt (body) der Präsentation eingefügt
  body
}


// ========== VERWENDUNG DES TEMPLATES ==========

// 1. Aufruf der Titelfolie
#title_slide(
  "3D-Druck und OpenSCAD",
  "Colin Hanschmann",
  "18. November 2025"
)

// 2. Anwendung des Themes auf alle folgenden Inhalte
#presentation_theme[
  
  = Gliederung
  

  - 3D-Druck \
  - OpenSCAD


/*  Dies ist der Text auf der ersten Inhaltsfolie. Das Layout wird durch die `presentation_theme` Funktion gesteuert.

//  * Jede `= Überschrift` erzeugt eine neue Folie.
//  * Der Text ist linksbündig.*/

= 3D-Druck (Additive Fertigung)
- 3D-Modell \
- Schicht für Schicht gefertigt \
- 
/*#figure(
  image("", width: 80%),
  caption: [
    A step in the molecular testing
    pipeline of our lab.
  ],
)*/


  /*#columns(2, gutter: 8mm)[
    == Spalte 1 (H2)
    Inhalte für die linke Spalte.

    * Punkt A
    * Punkt B
    
    #colbreak()
    
    == Spalte 2 (H2)
    Inhalte für die rechte Spalte.
    
    Man kann hier Bilder, Code oder beliebigen anderen Inhalt platzieren.
  ]*/

= OpenSCAD

- Programm für 3D-Modelling
- 


]
