from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

doc = SimpleDocTemplate("/mnt/data/Formelsammlung_aktualisiert.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

text = """
<b>Aktualisierte Formelsammlung – mit Anmerkungen</b>

--------------------------------------------
<b>1. Kreisbewegung mit konstanter Winkelbeschleunigung</b>
α = Δω / Δt  
ω(t) = ω₀ + α t  
v = ω r  
Δφ = ω₀ t + 1/2 α t²  
φ_end = φ_start + Δφ  

<i>Anmerkung: ω₀ = –α t ist nicht allgemein gültig. Verwende die Standardgleichung ω(t)=ω₀+α t.</i>

--------------------------------------------
<b>2. Zwei-Massen-System auf schiefer Ebene</b>
Kräfte auf m₁:  
  F_g = m₁ g sinα  
  F_r = μ m₁ g cosα  
Kräfte auf m₂:  
  F_g = m₂ g  

Gesamtgleichung:  
m₂ g – (m₁ g sinα + μ m₁ g cosα) = (m₁ + m₂) a  

a = [m₂ g – m₁ g (sinα + μ cosα)] / (m₁ + m₂)

<i>Anmerkung: gültig bei masselosem Seil/Rolle. Reibung wirkt entgegen Bewegung. Haftreibung separat prüfen.</i>

--------------------------------------------
<b>3. Feder-Masse-System mit Dämpfung</b>
k = F / Δx  
ω₀ = sqrt(k/m)  
ω_d = 2π f_d  

Dämpfung (viskos):  
ω_d = sqrt(ω₀² – (c / 2m)²)  

<i>Anmerkung: δ = sqrt(ω₀² − ω_d²) ist korrekt, wenn δ = c/(2m). Standardnotation: Dämpfungsverhältnis ζ = c/(2√(mk)).</i>

--------------------------------------------
<b>4. Proton im elektrischen Feld</b>
Beschleunigung durch Spannung:  
v_x = sqrt(2 q U_B / m)  

Flugzeit:  
t = L / v_x  

Beschleunigung im Feld:  
a_y = qE / m  
v_y = a_y t  
y = 1/2 a_y t²  

<i>Anmerkung: Gültig nicht-relativistisch; bei großen U_B relativistische Korrekturen nötig.</i>

--------------------------------------------
<b>5. Elektromagnetische Welle</b>
H = E / Z  
I = E_eff² / Z  (für RMS-Werte)

<i>Anmerkung: Für Spitzenwerte gilt I = E_peak² / (2Z). E- und H-Felder sind transversal.</i>

--------------------------------------------
<b>6. Dipol & Wellenausbreitung</b>
λ = c / f  
T = 1 / f  
l = λ/2  

Ausbreitung im Medium:  
v = c / sqrt(ε_r)  
λ' = v / f  
l' = λ'/2  

<i>Anmerkung: Die Frequenz bleibt beim Übergang ins Medium unverändert (f' = f). Nur λ ändert sich.</i>
"""

for line in text.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 6))

doc.build(story)

"/mnt/data/Formelsammlung_aktualisiert.pdf"
