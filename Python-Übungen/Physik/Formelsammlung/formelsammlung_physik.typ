#set page(width: 210mm, height: 297mm, margin: 20mm)
#set heading(numbering: "1.")

#let note(text) = block[
  set fill: luma(95%)
  set inset: 6pt
  set radius: 4pt
  set stroke: 0.5pt + luma(70%)
  text
]


= Kreisbewegung mit konstanter Winkelbeschleunigung

Die grundlegenden Gleichungen lauten:

$α = "Δω" / "Δt"$
$ω(t) = ω_0 + α t$
$v = ω r$
$"Δφ" = ω_0 t + 1/2 α t^2$
$"φ_end" = "φ_start" + "Δφ"$

#note[
*Hinweis:*  
Die häufig genannte Form $ω_0 = -α t$ ist **nicht allgemein gültig**.  
Die Standardform ist $ω(t) = ω_0 + α t$.
]

----------------------------------------------------

= Zwei-Massen-System auf schiefer Ebene

Kräfte auf Masse $m_1$:

$F_g = m_1 g sin(α)$  
$F_r = μ m_1 g cos(α)$

Kräfte auf Masse $m_2$:

$F_g = m_2 g$

Die Bewegungsgleichung:

$m_2 g - (m_1 g sin(α) + μ m_1 g cos(α)) = (m_1 + m_2) a$

Daraus folgt die Beschleunigung:

$ a = (m_2 g - m_1 g (sin(α) + μ cos(α))) / (m_1 + m_2) $

#note[
*Hinweis:*  
Gültig für masseloses, reibungsfreies Seil und Rolle.  
Bei Haftreibung muss separat geprüft werden, ob Bewegung stattfindet.
]

----------------------------------------------------

= Feder-Masse-System mit Dämpfung

$k = F / "Δx"$  
$ω_0 = sqrt(k / m)$  
$ω_d = 2π f_d$

Viskose Dämpfung:

$ ω_d = sqrt(ω_0^2 - (c / (2m))^2 ) $

#note[
*Hinweis:*  
Die Größe $δ = sqrt(ω_0^2 - ω_d^2)$ ist korrekt, wenn $δ = c / (2m)$.  
In der Fachliteratur wird meist das Dämpfungsverhältnis  
$ ζ = c / (2 sqrt(m k)) $ verwendet.
]

----------------------------------------------------

= Proton im elektrischen Feld

== Beschleunigung durch eine Spannung

$ v_x = sqrt(2 q U_B / m) $

== Flugzeit im Kondensator

$ t = L / v_x $

== Beschleunigung im Feld

$ a_y = "qE" / m $

$ v_y = a_y t $

$ y = 1/2 a_y t^2 $

#note[
*Hinweis:*  
Gültig im nicht-relativistischen Regime.  
Bei hohen Spannungen müssen relativistische Korrekturen beachtet werden.
]

----------------------------------------------------

= Elektromagnetische Welle

Zusammenhang der Felder:

$ H = E / Z $

Intensität (mittlere Leistung pro Fläche, RMS-Werte):

$ I = "E_{eff}"^2 / Z $

#note[
*Hinweis:*  
Für Spitzenwerte gilt:  
$ I = "E_{peak}"^2 / (2 Z) $.  
Elektromagnetische Wellen sind transversal.
]

----------------------------------------------------

= Dipol und Wellenausbreitung

Im Vakuum:

$ λ = c / f $  
$ T = 1 / f $  
$ l = λ / 2 $

Im Medium:

$ v = c / sqrt(ε_r) $  
$ λ' = v / f $  
$ l' = λ' / 2 $

#note[
*Hinweis:*  
Die Frequenz bleibt beim Eintritt ins Medium **immer unverändert**.  
Nur die Wellenlänge ändert sich.
]

----------------------------------------------------

#align(center)[*Ende der Formelsammlung*]
