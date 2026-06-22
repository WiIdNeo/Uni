# Agentic AI in Unternehmensumgebungen unterschiedlicher Sicherheitsstufen: Übersichtsplan

## Executive Summary  
Agentische KI-Systeme – autonome Agenten, die Aufgaben mit LLMs ausführen – gelten als nächste Innovationsstufe für Unternehmen. Sie ermöglichen adaptive, mehrstufige Problemlösungen (z. B. Recherche, Automatisierung, Planung), erhöhen aber zugleich die Angriffsfläche. Autonomie und Persistenz der Agenten sowie deren Zugriff auf interne Systeme bergen neue Risiken: manipulierte Eingaben (Prompt Injection) können zu Datenexfiltration führen (siehe Exploit EchoLeak), Toolnutzung (APIs, Kalender etc.) kann missbraucht werden, und Multi-Agent-Orchestrierungen vergrößern die Komplexität. 

Dieser Überblick erarbeitet mögliche Forschungsfragen und eine Gliederung für eine 20-seitige Arbeit. Er definiert wichtige Grundlagen (Agentic AI, LLMs, Agent-Loop, ReAct, Tool-Use, Memory, Multi-Agent-Systeme, Prompt Injection, Kontextfenster, RBAC, ISO-27001-Datenklassifikation) und identifiziert Anwendungsszenarien mit konkreten Threat-Modellen je Schutzklasse (Public, Intern, Confidential, High Security). Außerdem vergleicht er Architektur-Designs (Cloud vs. lokal vs. Hybrid; stateless vs. stateful; Single- vs. Multi-Agent) mit Vor- und Nachteilen sowie Sicherheitsmaßnahmen pro Klasse. Ein technischer Abschnitt listet kostenlose, lokal einsetzbare LLM-Stacks auf (LLM, Laufzeitumgebung, Agent-Framework, Memory, Tools) samt Installationsaufwand, Datenschutzbewertung, Performance und Limitierungen – ergänzt durch Vergleichstabellen und Beispiel-Stacks (Minimal, Multi-Agent, Enterprise). Inklusive sind Beispiel-Architekturdiagramme (Mermaid) für „Confidential“ und „High Security“-Umgebungen sowie Links zu Open-Source-Tools (Ollama, llama.cpp, Hugging Face, LangChain, AutoGen/MAF, CrewAI, Semantic Kernel, ChromaDB, FAISS) mit Nutzungshinweisen. Schließlich werden Governance- und Kontrollmaßnahmen (Logging, Audit, Human-in-the-loop, Prompt-Filtering, Tool-Permissioning, RBAC, Air-Gapping, Data-Exfil-Prevention) erörtert und offene Forschungsfragen sowie Evaluationsansätze (Experimente, Metriken, Benchmarks) aufgezeigt.

## Mögliche Forschungsfragen (Varianten)  
- **RQ1: Wie lassen sich agentische KI-Systeme sicher in Unternehmen mit unterschiedlichen Schutzklassen einsetzen?**  
  *Vorteile:* Umfassende Perspektive auf Architektur, Risiko und Governance. *Nachteile:* sehr breit; kann zu oberflächlichen Ergebnissen führen.  
- **RQ2: Welche Architekturmodelle (Cloud vs. on-prem vs. Hybrid) sind für Agentic-AI-Lösungen in vertraulichen oder hochsicheren Umgebungen geeignet?**  
  *Vorteile:* Speziell auf Architektur und Deployment fokussiert; praktisch relevant. *Nachteile:* Vernachlässigt Risikoanalyse und Governance-Aspekte.  
- **RQ3: Welche Risiken und Threat-Modelle ergeben sich durch den Einsatz von Agentic AI in Unternehmen verschiedener Schutzstufen (Public, Internal, Confidential, High-Security)?**  
  *Vorteile:* Klarer Fokus auf Sicherheitsbedenken; Grundlage für Schutzmaßnahmen. *Nachteile:* Technischer Lösungsbezug könnte fehlen.  
- **RQ4: Wie können Agenten-Frameworks (z.B. LangChain, AutoGen/MAF, CrewAI, Semantic Kernel) in Bezug auf Datenschutz, Sicherheit und Performance im Unternehmenskontext bewertet werden?**  
  *Vorteile:* Praxiserprobt; viele konkrete Open-Source-Implementierungen. *Nachteile:* Weniger Fokus auf organisatorische Schutzklassen.  
- **RQ5: Wie müssen Governance- und Kontrollmaßnahmen (Audit, RBAC, Filter) gestaltet sein, um agentische KI in hochsicheren Umgebungen vertrauenswürdig zu machen?**  
  *Vorteile:* Konzentriert auf Richtlinien und Prozesse. *Nachteile:* Technik-Details bleiben abstrakt.  

Jede Frage hat spezifische *Vorzüge* (z.B. breites Überblicksthema vs. fokussierte technische Prüfung) und *Nachteile* (z.B. geringe Tiefe in anderen Aspekten). Idealerweise verbindet die Arbeit Elemente mehrerer Fragen: z.B. Architekturentscheidung und Risikomodelle verknüpfen (RQ2+RQ3), oder Framework-Bewertung und Operationale Kontrolle (RQ4+RQ5).

## Detaillierte Gliederung für eine ~20-seitige Arbeit  

1. **Einleitung & Motivation** (ca. 2 Seiten)  
   - Kontext: Agentic AI in Unternehmens-IT  
   - Relevanz in verschiedenen Schutzklassen (Public/Internal/Confidential/High)  
   - Ziel und Aufbau der Arbeit  

2. **Zielsetzung und Forschungsfragen** (ca. 1 Seite)  
   - Übersicht potenzieller Forschungsfragen (siehe oben)  
   - Abgrenzung des Untersuchungsschwerpunkts  

3. **Grundlagen** (ca. 5 Seiten)  
   - **Agentic AI & LLMs:** Definition, Entwicklung, Beispiele (AutoGPT, GPT-4o, etc.). Agenten-Konzept: Autonomie, Zielorientierung, Planen.  
   - **Agent-Loop (Observe–Reason–Act):** Funktionsweise eines Agentenzyklus (Beobachten, Schlussfolgern, Handeln). Erwähnung von ReAct-Paradigma, das „Reasoning“ (Argumentation) und „Acting“ (Werkzeugaufrufe) kombiniert.  
   - **LLM-Kernprinzipien:** Transformermodelle, Kontextfensterbeschränkung, In-Context Learning vs. Feinabstimmung. Begrenzter Speicher im Kontext (≈65k Token bei GPT-4o, sonst typ. 4k–32k) führt zu Bedarf an externem Memory.  
   - **ReAct (Reason+Act):** Kurz erläutern, wie LLMs abwechselnd „Denkschritte“ und externe Aktionen (API, DB, Websuche) durchführen. Vorteile: geringere Halluzination durch Tool-Abfragen.  
   - **Werkzeug-Nutzung (Tool Use):** Agenten rufen Werkzeuge auf (APIs, Kommandozeile, Datenbanken). Ermöglicht Zugriff auf aktuelle Daten/Services. Dabei sind Schnittstellen (z.B. HTTP-Clients, Datenbanktreiber) kritisch.  
   - **Gedächtnis/Memory:** Notwendigkeit persistenter Speicher: z.B. Chat-Verläufe, Vektordatenbanken, Ereignis-Logs. Neuere Ansätze („Agentic Memory“) integrieren Lang- und Kurzzeitgedächtnis als Aktionen.  
   - **Multi-Agent-Systeme:** Kooperation mehrerer spezialisierter Agenten (z.B. Team aus Recherche-, Analyse-, Planungs-Agent). Vorteile: Aufgabenverteilung, fehlertolerant. Nachteile: komplexe Kommunikation und Koordination. *Bedrohungen:* Agenten können einander manipulieren oder kompromittiert werden.  
   - **Prompt-Injektion:** Hauptgefährdungsszenario. Dabei schaltet ein bösartiger Prompt die Rolle des Benutzers um und bringt den Agenten dazu, unerlaubte Aktionen durchzuführen oder Informationen preiszugeben. Lupinacci et al. zeigen, dass fast alle modernen LLM-Agenten dafür anfällig sind. Angriffe können direkt (ungebunden im Prompt) oder indirekt (eingebettet in externe Datenquellen) erfolgen.  
   - **Kontextfenster-Begrenzung:** LLMs können nur eine begrenzte Anzahl Tokens im Kontext berücksichtigen. Das Limitiert den Umfang kurzzeitiger Gedächtnisse. *Lösung:* Periodische Zusammenfassungen, spezialisierte Kontextmanagement-Agenten.  
   - **Zugriffsrechte (RBAC) und Data Classification:** Rolle-basierte Zugriffskontrolle definiert, welche Agenten auf welche Ressourcen (APIs, Datenbanken) zugreifen dürfen. ISO-27001 fordert Datenklassifikation; typisches Schema: „Öffentlich – Intern – Vertraulich – Streng Vertraulich“ (entsprechend Public/Internal/Confidential/High-Restricted). Jede Schutzklasse hat eigene Anforderungen:  
     - *Öffentlich:* Allgemeine Informationen, keine Geheimhaltung (z.B. Marketingtexte).  
     - *Intern:* Betriebsinterne Daten, geringe Einschränkungen (Firmen-Intranet).  
     - *Vertraulich:* Geschäftsgeheimnisse, personenbezogene Daten – nur zugelassene Mitarbeiter.  
     - *Streng vertraulich (High-Security):* Höchste Geheimhaltung (z.B. Staatsgeheimnisse, kritische Forschung).  

## Einsatzszenarien und Risiken nach Schutzklasse  

- **Public (Öffentlich):** Agentic AI kann hier von Cloud-LLMs profitieren, da Daten nicht vertraulich sind. Beispiel: Automatische Generierung von Marketingtexten, Chatbot für Kundenanfragen. *Risiken:* Fehlleitungen des Agenten (z.B. Erstellung irreführender Inhalte), Missbrauch der Agenten zur Verbreitung von Fehlinformationen. Prompt-Injektionen können zu „Trolling“ führen, sind aber inoffiziell weniger kritisch. Hier sind Verfügbarkeit und Skalierbarkeit wichtiger als strenge Sicherheit.  

- **Internal (Intern):** Einsatz für interne Prozesse wie Dokumentensuche, Helpdesk-Assistenz, Datenanalyse. Agenten könnten z.B. automatisch Berichte aus SAP- oder CRM-Systemen extrahieren. *Risiken:* Interne Informationen (Mitarbeiterdaten, Geschäftsprozesse) könnten bei Kompromittierung ausgeleitet werden. Beispiel-Threat-Modelle: Ein manipuliertes Agenten-Plugin füttert den Agenten mit falschen Firmenrichtlinien; ein Prompt-Injection bringt den Agenten dazu, interne Berichte unverschlüsselt zu versenden. Angreifer könnten versuchen, Agenten-Jailbreaks oder Backdoors in genutzten Tools einzuschleusen.  

- **Confidential (Vertraulich):** Kritische Firmendaten (Prototypendaten, Kundenlisten) dürfen das Gelände nicht verlassen. Lösungen laufen lokal (on-premises). Agenten dürfen nur auf interne, vertrauenswürdige Quellen zugreifen. Beispiel: Ein Agent durchsucht interne Enzyklopädien oder plant Produktionsabläufe. *Risiken:* Selbst lokal können Speicher („Memory“) oder Zwischenergebnisse ausspioniert werden. Bösartige Prompts könnten autorisierten Tools (z.B. E-Mail) unautorisierte Daten entlocken. Die Kombination mehrerer Agenten erhöht die Komplexität: Ein kompromittierter Agent könnte andere ausnutzen. Maßnahmen: strenge RBAC (z.B. Agent A hat nur Leserechte auf DB, Agent B nur Schreibrechte), Input-Filter (keine ausführbaren Befehle im Prompt), Logging aller Agentenaktivitäten.  

- **High Security (Hochsicherheit):** Höchstmögliche Schutzstufe: Air-Gapped-Umgebungen ohne Netzwerkschnittstellen, nur kleinste, explizit geprüfte LLM-Modelle im Einsatz. Mögliche Szenarien: Geheimhaltung von Forschungsdaten, Steuerung kritischer Infrastrukturen durch Agenten. *Risiken:* Hier ist vor allem Sabotage gefährlich. Ein physischer Insider könnte einen Agenten manipulieren, daher sind harte Kontrollen nötig: Alle Datenzugriffe und Agenten-Aktionen werden offline auditiert. Jeglicher Fernzugriff ist ausgeschlossen. Jegliche Agentenkommunikation (auch untereinander) ist streng reglementiert.  

_In jedem Fall_ stellt die Prompt-Injektion eine zentrale Gefahr dar: Experimentelle Befunde zeigen, dass >94 % aller LLM-Agenten dafür anfällig sind. Weitere relevante Angriffsarten: *Speer-Phishing* durch Agenten (automatisierte Lockvogel-Mails), *Memory Poisoning* (subtile Manipulation der Agenten-Erinnerung über viele Sessions) sowie *identitätsbasierte Angriffe* (z.B. ein Agent imitiere einen legitimen Service). In Threat-Models muss berücksichtigt werden, dass Agenten API- und Systemtools ansprechen – ein kompromittierter Agent mit z.B. Kalender-Zugriff könnte Termine manipulieren oder Daten exfiltrieren.

## Architekturvergleich  

- **Cloud vs. Lokal vs. Hybrid:**  
  - *Cloud:* Externe LLM-APIs (z.B. OpenAI, Amazon Bedrock). Vorteile: einfache Skalierung, stets aktuelle Modelle, schneller Einstieg. Nachteile: Sensible Daten verlassen das Unternehmen, Abhängigkeit vom Provider. Unternehmen vermeiden oft Cloud-Lösungen für vertrauliche oder hochsichere Daten.  
  - *Lokal (On-Premises):* Eigene Server oder Edge-Geräte betreiben die Modelle (z.B. mit Ollama, llama.cpp, Hugging Face auf eigenem GPU-Cluster). Vorteile: Maximale Datenhoheit, volle Kontrolle über Updates und Sicherheit. Nachteile: Höherer Initialaufwand (Hardware, Administration), evtl. geringere Rechenleistung. Bei Skalierung können Kosten dank selbstbetriebener Infrastruktur sinken.  
  - *Hybrid:* Kritische Teile (LLM oder Datenbankspeicher) bleiben lokal, weniger sensible Aufgaben können in die Cloud ausgelagert. Komplexer, aber erlaubt eine Balance aus Flexibilität und Sicherheit. Beispiel: Preprocessing lokal, finale Anfrage an Cloud-LLM (mit Datenanonymisierung).  

- **Stateless vs. Stateful:**  
  - *Stateless Agent:* Jeder Aufruf ist unabhängig, das Modell hat kein längerfristiges Gedächtnis außer Eingabe-Kontext. Einfach zu betreiben, da keine persistente Storage nötig. Aber Unfähigkeit, über Sessions hinweg zu „lernen“.  
  - *Stateful Agent:* Verfügt über persistente Erinnerung (z.B. Datenbanken, Vektorspeicher). Kann Erfahrungen kumulieren und über Langzeitaufgaben konsistent sein. Erhöht Leistungsfähigkeit (laufende Aufgaben, personalisierte Interaktion), aber erschwert das Zurücksetzen bei Fehlern und erfordert sicheren Speicher (Risk: Memory Poisoning).  

- **Single-Agent vs. Multi-Agent:**  
  - *Einzelagent-System:* Ein Agent führt Aufgaben sequenziell durch. Weniger Fehlerquellen, leichter nachvollziehbar. Geringere Komplexität (nur ein Entscheidungsflow).  
  - *Multi-Agent-System:* Verschiedene spezialisierte Agenten (z.B. *Recherche-Agent*, *Analyse-Agent*, *Planungs-Agent*) arbeiten parallel/kooperativ. Besser geeignet für komplexe Tasks (Arbeitsteilung, Redundanz). Nachteilig: überproportional erhöhte Angriffsoberfläche (Kommunikationsprotokolle, Vertrauen der Agenten untereinander). Beispiel: Ein infizierter Agent könnte anderen böswillige Instruktionen senden. Lupinacci et al. fanden, dass 100 % der getesteten Multi-Agenten-Frameworks für „Inter-Agent Trust“-Angriffe anfällig sind.  

**Sicherheitsmaßnahmen je Architektur:** In öffentlichen Umgebungen genügen Standardmaßnahmen (TLS, Authentifizierung). In internen/confidential-Umgebungen sind zusätzliche Kontrollen nötig: *Least-Privilege-RBAC* für Agententools, *Input-Sanitizer* (Prompt-Filter), *strenge Audit-Logs*, *Endpoint-Security* für Workstations, *DLP-Systeme* (Data Loss Prevention) zur Erkennung ungewöhnlicher Exfiltration. In High-Security-Umgebungen kommen zusätzlich Air-Gapping, Whitelisting (nur zugelassene Prozesse), physische Zugangskontrollen und evtl. hardwareseitige Verschlüsselung zum Einsatz.

## Kostenlose, lokale Open-Source-Implementierungen  

Es existieren diverse Open-Source-Bausteine für einen lokalen Agenten-Stack. Wichtige Komponenten: **LLM-Modelle** (meist kleiner als kommerzielle GPTs), **Inferenz-Engines/Laufzeit** (z.B. C++-Implementierungen, PyTorch), **Agent-Frameworks**, **Memory-Store** (Vektordatenbanken) und **Tool-Layer** (APIs, Systemzugriffe). Für jeden Ansatz gilt: *Daten bleiben lokal*, was die Privatsphäre verbessert, jedoch sind Rechenlast und Speicher begrenzt.

- **LLM-Modelle & Laufzeiten:** Beispiele für frei nutzbare Modelle sind LLaMA-Varianten (2B–40B Parameter), Gemma (3B, 7B), Mistral, Dolly, Falcon, etc. Engines: *llama.cpp* (C++-Implementierung, bietet schnelles Inferenz auf CPUs/GPU-Quantisierung), *Ollama* (CLI für Modelle wie Gemma, Qwen etc. lokal), *Hugging Face Transformers* (Python-Bibliothek mit 1 M+ vortrainierten Modellen).  
- **Agent-Frameworks:** *LangChain* (Python, modular, beliebt für Agententwicklung), *LangGraph* (niedriger Level), *Microsoft Agent Framework (Nachfolger von AutoGen)*, *CrewAI* (no-code/CI-Plattform für multi-agentische Workflows), *Semantic Kernel* (Microsoft, SDK für C#/.NET & Python, steuerbare KI-Agenten). AutoGen (Python) war ein frühes MS-Tool, ist aber inzwischen „maintenance only“; MS empfiehlt den neuen Agent Framework (MAF).  
- **Gedächtnis und Datenbank:** *ChromaDB* – Open-Source-Vektor-DB (Serverless, PLA2), *FAISS* – Bibliothek für Vektor-Similarity-Search (von Meta), auch *Milvus*, *Weaviate* etc. Key-Value-Stores oder relationale DBs können für einfache Zustände genutzt werden.  
- **Tool-Layer:** Oft „übergeben“ Agenten Schnittstellen, z.B. zum Dateisystem, Web-APIs (z.B. REST-Anfragen via Python), Kalkulation (Shell-Kommandos), E-Mail-Klienten. Frameworks bieten häufig integrierte Tool-Adapter (z.B. Web-Browser via Playwright/MCP, Datenbank-Connectoren). Diese müssen mit starken Berechtigungen versehen werden (siehe RBAC unten).

Tabelle 1 (Vergleich frei-lokaler Implementierungsvarianten):

| **Stack-Variante**      | **LLM-Modell (Größe)**             | **Laufzeit/Framework**                       | **Memory-Store**          | **Tools / Schnittstellen**           | **Install/Betrieb**         | **Datenschutz/Security**        | **Leistung/Limitierungen**          |
|-------------------------|-----------------------------------|----------------------------------------------|---------------------------|--------------------------------------|-----------------------------|-------------------------------|------------------------------------|
| **Minimal**             | Gemma-3B, LLaMA 2 7B             | llama.cpp (C++) oder HuggingFace (Python)   | Keine oder einfacher JSON | Terminal, lokale Dateien (Filesystem) | Einfach (kein GPU nötig)    | Daten bleiben lokal; geringes Risiko | Niedrige Latenz auf CPU, begrenzter Kontext (wenige 1.000 Tokens), schlechtere Qualität bei komplexen Tasks |
| **Multi-Agent**         | LLaMA 2 13B, Mistral 7B (oder gemischte Modelle) | PyTorch/Llama.cpp, AutoGen/MAF oder CrewAI   | ChromaDB oder FAISS       | REST-APIs, Web (Headless), DB-Zugriff | Mittel (GPU empfohlen, Container) | Verbesserung durch RBAC; intra-agent Kommunikation muss gesichert sein | Höherer Rechenbedarf, synchronisationsaufwändig, kann Latenz erhöhen |
| **Enterprise-like**     | LLaMA 3 34B+, Gemma 1.3B         | HuggingFace (TGI), MAF, LangChain           | Kombination (Vektordb + SQL) | Integrierte Unternehmens-APIs, S3, ERP | Komplex (Cluster, CI/CD, Skalierung) | Vollständige Kontrolle, End-to-End-Verschlüsselung möglich | Sehr leistungsfähig (GPU/Cluster), teuer und aufwendig einzurichten |

*(Install: qualitativ, Datensicherheit: On-Premises-Datenhaltung, aber Angriffsfläche steigt mit Komplexität, Performance: je nach Modell-Größe und Hardware.)*

## Beispiel-Architekturdiagramme (Mermaid)  

### Beispiel: Lokal betriebener Agent (Schutzklasse *Confidential*)  
```mermaid
flowchart TB
  subgraph Agent-System
    A[LLM-Agent (on-prem)] 
    M[(Gedächtnis / Vektor-DB)]
    T[(Interne Tools/APIs)]
  end
  subgraph Infrastruktur
    R[RBAC / Auth] 
    L[Audit & Logging] 
    F[Interne Firewall]
  end
  A -->|Speichern/Abrufen| M
  A -->|Aufruf| T
  T -->|Datenzugriff| DB[(Interne Datenbank)]
  R -.-> A
  L -.-> A
  F -.-> T
```
*Beschreibung:* Der lokale Agent (A) mit integriertem LLM nutzt einen internen Memory Store (M) sowie zugelassene interne Tools/APIs (T). RBAC-Module (R) autorisieren Aktionen, Firewalls (F) begrenzen Netzwerkkonnektivität, und Audit-Logging (L) erfasst Entscheidungen. Alle Komponenten bleiben innerhalb der internen Infrastruktur (kein Internet).  

### Beispiel: Lokal betriebener Agent (Schutzklasse *High Security*)  
```mermaid
flowchart TB
  subgraph Secure-Agent
    A2[Air-Gapped LLM-Agent]
    M2[(Isolierter Memory-Speicher)]
    T2[(Physikalische Tools & DB)]
  end
  subgraph Hohe Sicherheit
    R2[Striktes RBAC]
    L2[Audit-Log]
    G[Physikalisches Gehäuse (Air Gap)]
  end
  A2 --> M2
  A2 --> T2
  R2 -.-> A2
  L2 -.-> A2
  G --- A2
```
*Beschreibung:* Der Agent (A2) läuft in einer abgeschotteten Umgebung. Er greift nur auf hocheingeschränkte, interne Tools (T2) zu, und alle Zugriffe werden streng durch RBAC (R2) kontrolliert. Ein physikalisches Air-Gap (G) trennt ihn vom Restnetzwerk. Sämtliche Aktionen werden im Audit-Log (L2) verzeichnet.  

## Konkrete Implementierungsanleitungen und Links  

- **Ollama**: [Dokumentation](https://docs.ollama.com) – Einfaches CLI-Tool für lokale LLM (unterstützt OpenClaw, Gemma, Qwen u. a.). Installation per Skript oder Download. Empfehlenswert für schnellen Einstieg mit moderaten Modellen.  
- **llama.cpp**: [GitHub](https://github.com/ggml-org/llama.cpp) – C/C++-Bibliothek für effiziente LLaMA-Inferenz auf CPU/GPU. Viele Modelle unterstützt (LLaMA-3, Falcon, Mixtral, etc.). Installation via `brew/conda/Docker` oder Kompilierung. Gut für Offline-Einsatz kleiner bis mittlerer Modelle.  
- **Hugging Face Transformers**: [Docs](https://huggingface.co/docs/transformers) – Python-Framework für viele vortrainierte Modelle (Text, Bild, etc.). Bietet Pipelines für einfache Inferenz, Trainer API für Feintuning. Einsatz sowohl lokal (PyTorch) als auch in der Cloud möglich. Perfekt für vielfältige Anwendungsfälle.  
- **LangChain & LangGraph**: [Docs](https://docs.langchain.com) – Populäres Python-Framework zur Erstellung von LLM-gestützten Anwendungen und Agenten. Integriert Tool-Nutzung, Prompts, Memory-Management. **LangSmith** (Firmenplattform) ergänzt Deployment und Monitoring.  
- **Microsoft Agent Framework (ehem. AutoGen)**: [GitHub](https://github.com/microsoft/autogen) – Python-Framework für Multi-Agent-Systeme. Ursprünglich “AutoGen”; derzeit in Wartungsmodus. **Microsoft Agent Framework (MAF)** ist der Nachfolger für Enterprise-Anwendungen (stabile APIs, Multi-Provider-Modelle, plattformübergreifend). Beispiel-Code findet sich in den Repos.  
- **CrewAI**: [Dokumentation](https://docs.crewai.com) – Production-ready Plattform zum visuellen Entwerfen und Ausführen von Agenten („Crews“) mit Guardrails, Memory, Knowledge und Monitoring. Unterstützt Flows, Events und Team-RBAC. Install per `pip install crewai`. Gut geeignet für Geschäftsanwender ohne tiefe Coding-Kenntnisse.  
- **Semantic Kernel**: [MS Learn](https://learn.microsoft.com/semantic-kernel/overview/) – Leichtgewichtiges SDK (.NET, Python, Java) zur schnellen Erstellung von KI-Agenten. Ermöglicht „Function Calling“ (Aufruf interner APIs) und über OpenAPI-Anbindung (z.B. Microsoft 365) die nahtlose Integration. Bietet eingebaute Sicherheit (Telemetrie, Filter). Ideal für Microsoft-Stacks.  
- **ChromaDB**: [Docs](https://docs.trychroma.com) – Open-Source Vektor-Datenbank (Apache2) für Embeddings. Hohe Performance für Milliarden von Datensätzen, skaliert serverless. Installation via `pip install chromadb`. Nützlich als Agenten-Memory oder Knowledge-Store.  
- **FAISS**: [GitHub](https://github.com/facebookresearch/faiss) – Bibliothek für effiziente Ähnlichkeitssuche (Nearest Neighbor) in dichten Vektoren. C++/Python (CUDA-unterstützt) für große Embedding-Suchindizes. Installation über `conda` oder Kompilierung. Einsatz, um in Memory-Stores (z.B. bei RAG) schnelle Retrieval-Aktionen zu realisieren.  

*(Weitere Beispiele: [llama.cpp Models](https://github.com/ggml-org/llama.cpp#models) für unterstützte Modelle; [Hugging Face Hub](https://huggingface.co/models) zum Finden passender LLMs; Tool-Integrationen in LangChain/GPTAgent etc.)*  

## Governance & Betriebskontrollen  

- **Logging & Audit:** Lückenlose Protokollierung aller Agentenentscheidungen und Werkzeugaufrufe. Ermöglicht nachträgliche Analyse von Fehlverhalten. Idealerweise sollten Logs manipulationssicher gespeichert werden (z.B. append-only). Semantic Kernel bietet integriertes Telemetrie-Logging.  
- **Human-in-the-Loop:** Menschliche Überprüfung kritischer Aktionen, z.B. vor dem Senden von E-Mails oder Freigeben großer Transaktionen. KI-Empfehlungen werden erst nach Bestätigung ausgeführt. Dadurch können Fehlhandlungen abgefangen und Verantwortlichkeiten geklärt werden.  
- **Prompt-Filtering:** Vor- bzw. nachgeschaltete Filter prüfen Eingabeaufforderungen auf sensible Inhalte oder unerlaubte Befehle (Blacklist/Whitelist). Beispielsweise kann vermieden werden, dass Agenten systemrelevante Shell-Befehle erhalten. Inhaltliche Filter verhindern bösartige Instruktionen.  
- **Tool-Permissioning:** Nur ausdrücklich genehmigte Werkzeuge dürfen von Agenten aufgerufen werden. Agents laufen in isolierten Containern oder Sandboxes. Beispiel: Die Agenten-Policy definiert, dass API-Aufrufe zu Drittanbietern blockiert und nur interne Datenspeicher zugänglich sind. CrewAI etwa erlaubt Feineinstellungen für Tool-Berechtigungen.  
- **RBAC (Role-Based Access Control):** Strikte Rollentrennung für Agenten und Benutzer. Jeder Agent bzw. jede Rolle erhält nur minimale Rechte, die für seine Aufgabe nötig sind (Least-Privilege-Prinzip). Crews/Flows können Team-Mitglieder mit RBAC verwalten. Zugriffe auf Datenbanken und Dateien sind auth-basiert abgegrenzt.  
- **Air-Gapping & Netztrennung:** In hochsicheren Umgebungen werden Agenten physisch isoliert (no network, only internal subnets). USB-/Bluetooth-Ports gesperrt, Kommunikation nur via geprüften Kanälen. Alle externen Interfaces (Webzugriffe, E-Mail) sind entweder deaktiviert oder streng begrenzt.  
- **Data Exfiltration Prevention:** Technische Maßnahmen, um unautorisierte Datenübertragung zu erkennen und zu verhindern: DLP-Software, Upload-Filter oder gesicherte Proxies für Netzverkehr. Beispiel: Der Agent darf nur Daten mit Endpunkt „internal.company.local“ erreichen; externe Domains sind verboten.  
- **Kontinuierliches Monitoring:** Einsatz von IDS/IPS (Intrusion Detection/Prevention) und SIEM-Systemen, die Agenten-Aktivitäten überwachen. Anomalien (z.B. ungewöhnlich viele Datenbankabfragen) lösen Alarm aus.  

Diese Governance-Schichten reduzieren das Risiko von Fehlverhalten deutlich. Besonders wichtig ist die Kombination: Ein Prompt-Filter kann unautorisierte Anweisungen blockieren, während Audit-Logs sicherstellen, dass jede Aktion später nachvollziehbar ist. Systeme wie Semantic Kernel legen explizit Telemetrie-Kanäle und Hook-Mechanismen an, um solche Kontrollen umzusetzen.

## Ausblick: Offene Forschungsfragen & Evaluationsansätze  

- **Resilienz-Metriken:** Wie misst man die Sicherheit eines Agentic-Systems? Mögliche Metriken: Prozentsatz erkannter Prompt-Attacken, Grad der Datenexfiltration bei simulierten Angriffen, Erfolgsrate der Aufgaben im Verhältnis zu Angriffen.  
- **Simulationsplattformen:** Entwicklung von Benchmarks/Simulationen für Agenten-Angriffe (z.B. Penetrationstests mit künstlichen Angreifern). Man könnte z.B. einen *Red-Team-Agenten* konzipieren, der Prompt-Injections und Memory-Poisonings testet.  
- **Benutzereinbindung:** Untersuchung, wie Benutzer/Aufsichtspersonen in die Agentenschleife eingebunden werden können (z.B. wie viel Kontrolle braucht es, um Vertrauen herzustellen?). Empirische Studien könnten testen, wie „sehfähig“ Agenten sein müssen (Granularität der Rückmeldung).  
- **Rechtliche und ethische Bewertung:** Wie passt Agentic AI zur DSGVO, BSI-Grundschutz etc.? Müssen z.B. Agenten als datenverarbeitende Systeme registriert werden?  
- **Skalierung und Kosten:** Wie skaliert Agentic AI in der Praxis? Benchmarks zu Antwortzeiten (Idle vs. Peak), Ressourcenverbrauch für Multitasking-Agenten. Vergleiche: Zentrale GPU-Server vs. verteilte Edge-Agents.  
- **Tool-Ökosystem-Vergleich:** Evaluation verschiedener Open-Source-Stacks anhand von Kriterien (Aufwand, Stabilität, Sicherheit). Z.B. könnte man prototypisch einen Fall „Geheimen Projektbericht zusammenfassen“ mit LangChain+HuggingFace vs. MAF durchführen.  
- **Anpassung von Standards:** Übertragung bestehender Security-Standards (z.B. NIST SP 800-53, ISO 27001/27002) auf Agenten-Use-Cases. Welche fehlenden Kontrollen ergeben sich?  

Empirische Evaluationsmethoden umfassen kontrollierte Experimente (z.B. mehrere Agenten einsetzen und Angriffe planen), Metriken zur Fehlerrate, Nutzerbefragungen (zur Einschätzung des Nutzens/Risikos), sowie Simulationen in Cloud-Umgebungen. Zudem sind Case Studies in Industrieunternehmen wertvoll: Implementierung in einem Pilotprojekt, um reale Einsatzhürden und Sicherheitslücken zu identifizieren.

## Literatur- und Quellenliste  

- Abdullah et al.: *“Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges”* (ArXiv 2025) – Umfassende Survey zu Risiken agentischer KI.  
- Lupinacci et al.: *“Enabling Multi-Agent Security: Evaluating the Trust of LLM Agents”* (Conference Paper 2025) – Untersuchung von Prompt Injection, Trust-Exploits. Zitiert in.  
- Peter Cihon: *“Security and Safety Taxonomy for Agentic AI Systems”* (IEEE USA 2026) – Definition von Agenten-Failure-Modes (Memory Poisoning, Agent Compromise).  
- OWASP & Okta Blog: *“AI Agent Security Checklist”* (2026) – Praxisnahe Sicherheitskontrollen (RBAC, Auditing, Least Privilege).  
- Allganize Blog: *“Cloud vs On-Prem: AI Deployment Models”* (2026) – Vergleich von Cloud- und On-Prem-Lösungen.  
- SEC4YOU (DE-Blog): *“Klassifizierung & Schutzbedarf von Daten”* – Typische Schutzklassen (öffentlich, intern, vertraulich, streng vertraulich).  
- HighTable Consulting: *“Data Classification (ISO 27001)”* – Vier-Stufen-Modell (Public, Internal, Confidential, Highly Restricted).  
- IBM Think Blog: *“What Is Agentic Architecture?”* (2024) – Einführung in Architekturagentischer KI.  
- Ollama Dokumentation: *“Getting started with large language models”*.  
- GitHub: **olllama/ollama** – Open-Source-LLM-CLI mit Modellen wie Gemma, Qwen.  
- GitHub: **ggml-org/llama.cpp** – Leichtgewichtige LLM-Inferenz (C/C++).  
- Hugging Face Docs: *Transformers* – Framework für State-of-the-Art-LLMs (über 1M Model-Checkpoints).  
- Microsoft Docs: *Semantic Kernel Overview* – KI-Agenten-SDK für Enterprise (C#/Python).  
- GitHub: **microsoft/autogen** – (Maintenance) Framework für Multi-Agent-Anwendungen.  
- CrewAI Docs: *Intro CrewAI* – Plattform für kollaborative Agenten und Flows.  
- ChromaDB Docs: *Chroma – Open-source search infrastructure* – Vektor-DB für KI.  
- GitHub: **facebookresearch/faiss** – Bibliothek für effiziente Vektor-Suche.  
- Medien: Fachartikel und Konferenzbeiträge zu Multi-Agent AI (z.B. Stanford Generative Agents, Yu et al. 2026 “Agentic Memory”).  
- NIST und EU: *Generative AI Guidelines & AI Act* – Regulierungshinweise für KI-Systeme (als Diskussionsgrundlage).  

***Besonders zitierfähige Quellen*** sind die wissenschaftlichen Arbeiten und offiziellen Dokumentationen (ArXiv-Papers, Fachkonferenzen, offizielle Whitepaper und Repos) wie oben markiert. Die genannten GitHub-Links und offiziellen Docs bieten weiterführende Details.

