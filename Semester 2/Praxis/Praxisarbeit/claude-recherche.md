# Recherchedossier: KI-Agenten in Open-Source-LLM-Plattformen am Beispiel von Open WebUI

> **Zweck dieses Dokuments:** Dies ist *keine* fertige Praxisarbeit, sondern eine Recherche- und Strukturierungsgrundlage für dich. Es bündelt Fakten, Einordnungen, Quellen und konkrete Ressourcen zu allen Themen aus deiner Aufgabenstellung – inklusive der von dir gewünschten Tools (Claude, Claude Cowork, Pi, Hermes). Die eigentliche wissenschaftliche Ausarbeitung, Argumentation und Bewertung musst du selbst schreiben.
>
> **Stand:** Juni 2026. **Wichtiger Hinweis zur Quellenlage:** Das Themenfeld (Agenten, MCP, Open WebUI, AutoGen/Microsoft Agent Framework) verändert sich aktuell sehr schnell. Viele Online-Quellen zu diesen Themen sind SEO-optimierte Blogartikel unterschiedlicher Qualität – ich habe versucht, möglichst auf offizielle Dokumentation, GitHub-Repos und Primärquellen zurückzugreifen, habe das aber nicht überall geschafft. **Prüfe vor der Abgabe insbesondere Versionsnummern, Preise und Lizenzdetails noch einmal gegen die Primärquelle**, da sich diese laufend ändern.

---

## 0. Wie du dieses Dossier nutzen kannst

Das Dokument folgt grob der Struktur deiner Arbeitspakete:

1. **Grundlagenrecherche** (LLMs, Agenten, Tool/Function Calling, RAG, Multi-Agent, MCP)
2. **Markt- und Technologierecherche** (Open WebUI + Frameworks + deine Wunsch-Tools)
3. **Sicherheits- und Datenschutz-Einordnung** (Querschnittsthema, das du in Konzeption + Evaluation brauchst)
4. **Konzeption** (Architektur, Use Cases)
5. **Prototypische Umsetzung** (konkrete Schritt-für-Schritt-Ressourcen)
6. **Evaluation** (Kriterien & Vorgehen)
7. **Quellen & weiterführende Ressourcen**

Jeder Abschnitt enthält am Ende eine **„Einschätzung"** (meine Bewertung der Relevanz/Reife/Eignung) und **„Ressourcen"** (Links zum Weiterlesen). Stellen, an denen *du* eine Entscheidung triffst oder eigene Bewertung einbringen musst, sind mit **🎯 Für deine Arbeit** markiert.

---

## 1. Themenübersicht (Mindmap in Textform)

```
KI-Agenten in Open-Source-LLM-Plattformen
│
├── Grundlagen
│   ├── LLMs (Basis-Technologie)
│   ├── KI-Agenten / Agentensysteme (Architektur-Patterns)
│   ├── Tool Calling / Function Calling
│   ├── RAG → Agentic RAG
│   ├── Multi-Agent-Systeme
│   └── MCP (Model Context Protocol) ← zentrales Bindeglied 2025/26
│
├── Plattform: Open WebUI
│   ├── Architektur (Backend/Frontend, Functions, Tools, Pipelines)
│   ├── Native MCP-Unterstützung (seit v0.6.31)
│   ├── Lizenzfrage (BSD-3 → "Open WebUI License")
│   └── Community-Erweiterungen (z. B. Haervwe/open-webui-tools)
│
├── Agenten-Frameworks (Vergleichsobjekte)
│   ├── LangChain / LangGraph
│   ├── Microsoft Agent Framework (Nachfolger von AutoGen + Semantic Kernel)
│   ├── CrewAI
│   ├── Flowise
│   └── Dify
│
├── Deine Wunsch-Tools
│   ├── Claude / Claude API (Agent SDK, MCP-Connector, Managed Agents)
│   ├── Claude Cowork (agentische Wissensarbeit, Research Preview)
│   ├── Hermes Agent (Nous Research) ← überraschend direkt relevant für Open WebUI!
│   └── Pi (Inflection AI) ← thematisch eher Randnotiz, dazu unten mehr
│
├── Sicherheit & Datenschutz
│   ├── OWASP Top 10 for Agentic Applications (2026)
│   ├── MCP-Sicherheitsmodell (Konsens, OAuth 2.1, Sandboxing)
│   └── Open WebUI Admin-Gating für MCP-Server
│
└── Konzeption, Prototyp, Evaluation
    ├── Use Cases (Code-Review, Wissensdatenbank, Doku, Ticket, DevOps)
    ├── Architekturentscheidung (welches Framework + welcher Agent in Open WebUI?)
    └── Evaluationskriterien (Funktionalität, Performance, Wartbarkeit, …)
```

---

## 2. Grundlagenrecherche (Arbeitspaket 1)

### 2.1 Large Language Models – kurzer Rahmen

Für deine Arbeit reicht hier ein knapper, gut zitierter Grundlagenabschnitt (Transformer-Architektur, Pretraining/Fine-Tuning/RLHF, Context Window, Inferenz). Das ist gut etabliertes Wissen, das sich nicht wöchentlich ändert – du musst hier nicht tagesaktuell recherchieren, sondern kannst dich an Standardwerken/Übersichtsartikeln orientieren (z. B. "Attention Is All You Need", aktuelle Surveys zu LLMs). Wichtiger für deine Bewertung ist der Kontextbezug: **1M-Token-Kontextfenster** sind 2026 bei Spitzenmodellen (z. B. Claude Opus 4.6) Realität geworden – das beeinflusst direkt, ob man "klassisches RAG" oder eher direktes Kontext-Stuffing braucht (siehe 2.4).

**🎯 Für deine Arbeit:** Hier würde ich nur so viel schreiben, wie du brauchst, um Tool Calling/Agenten verständlich herzuleiten – nicht in die Tiefe der Modellarchitektur gehen, das ist nicht der Fokus deiner Fragestellung.

### 2.2 KI-Agenten und Agentensysteme

**Kernidee:** Ein "Agent" im aktuellen Sprachgebrauch (2024–2026) ist ein LLM, das in einer Schleife läuft: *Wahrnehmen (Kontext/Tool-Ergebnisse) → Planen → Handeln (Tool-Aufruf) → Beobachten → wiederholen*, bis ein Ziel erreicht ist oder ein Abbruchkriterium greift. Wichtige Architektur-Patterns, die du in der Literatur findest:

- **ReAct** (Reason + Act) – abwechselnd Denken und Handeln, Klassiker-Pattern, das die meisten heutigen Agent-Loops noch implizit nutzen.
- **Plan-and-Execute** – erst vollständigen Plan erstellen, dann Schritt für Schritt abarbeiten (robuster bei langen Aufgaben, weniger reaktiv).
- **Reflexion/Self-Critique** – Agent bewertet eigene Zwischenergebnisse und korrigiert sich.
- **Orchestrator-Worker / Supervisor-Pattern** – ein "Master"-Agent delegiert an spezialisierte Sub-Agenten (siehe Multi-Agent, 2.5).

Im 2026er-Sprachgebrauch wird oft zwischen **einfachen Tool-Use-Loops** (ein Modell, ein paar Tools, kurzer Task) und **"Deep Agents"/long-horizon agents** (lange, mehrstufige Aufgaben mit Sub-Agenten, Checkpointing, Wiederaufnahme nach Unterbrechung) unterschieden. Letzteres ist z. B. die Kategorie, in die Claude Code, Claude Cowork oder Hermes Agent fallen.

**Einschätzung:** Für deine wissenschaftliche Fragestellung lohnt es sich, früh eine klare Terminologie festzulegen (z. B. nach Konzepten von LangChain/LangGraph oder nach einer Survey), weil der Begriff "Agent" in der Praxis sehr unscharf verwendet wird – manchmal ist ein simpler Prompt-Wrapper mit einem Tool gemeint, manchmal ein vollautonomes System mit Gedächtnis und eigenem Terminal-Zugriff (wie Hermes Agent). Diese Unschärfe explizit zu benennen ist selbst ein legitimer wissenschaftlicher Beitrag deiner Arbeit.

### 2.3 Tool Calling / Function Calling

Technisch: Das LLM bekommt eine Liste verfügbarer "Tools" (Name, Beschreibung, JSON-Schema der Parameter) im Kontext. Es entscheidet anhand der Nutzeranfrage, ob und welches Tool es mit welchen Argumenten aufrufen möchte; die Antwort wird als strukturiertes Objekt (meist JSON) zurückgegeben, vom Host-System ausgeführt, das Ergebnis wieder in den Kontext zurückgespielt. Anbieter-Implementierungen (OpenAI Function Calling, Anthropic Tool Use, Google Function Calling) sind sich im Grundprinzip sehr ähnlich, unterscheiden sich aber im Detail (parallele Tool-Calls, "strict mode"/Schema-Validierung, Streaming von Tool-Calls).

Wichtig für deine Arbeit: **MCP (siehe 2.6) ist kein Ersatz für Function Calling**, sondern eine Standardisierungsschicht *darüber* – MCP definiert, wie Tools/Daten/Prompts zwischen einem Host (z. B. Open WebUI) und einem Server (z. B. einem Datenbank-Connector) ausgetauscht werden; das eigentliche Function Calling zum LLM hin bleibt davon unberührt.

### 2.4 Retrieval Augmented Generation (RAG) → Agentic RAG

**Klassisches RAG (2023):** Dokumente chunk-en → embedden → in Vektordatenbank ablegen → bei Anfrage Top-k ähnliche Chunks abrufen → in den Prompt einfügen → Modell generiert Antwort. Ein statischer, einmaliger Retrieval-Schritt.

**Agentic RAG (2025/26):** Das Modell entscheidet selbst, *ob*, *was* und *wie oft* es retrieved – RAG wird zu einem Tool im Agenten-Loop statt einer festen Pipeline-Stufe. Damit verschmilzt RAG technisch mit dem Tool-Calling-Konzept aus 2.3. Aktuelle Spielarten, die 2026 diskutiert werden: **Adaptive RAG** (Query-Klassifikator wählt Retrieval-Strategie je nach Komplexität), **Graph-RAG** (Wissensgraphen für Multi-Hop-Reasoning), **Self-RAG** (Modell bewertet eigene Retrieval-Ergebnisse und entscheidet über Nachbesserung).

Ein für deine Arbeit besonders relevanter Spannungsbogen: Durch 1M-Token-Kontextfenster (z. B. Claude Opus 4.6) stellt sich praktisch die Frage, **wann sich der Aufwand für eine RAG-Pipeline überhaupt noch lohnt** vs. wann man Dokumente einfach direkt in den Kontext gibt. Das ist ein guter Diskussionspunkt für deine Konzeptions- und Evaluationskapitel, gerade bezogen auf Open WebUI, das eine native, recht einfache Knowledge/RAG-Funktion mitbringt (siehe 3.1).

### 2.5 Multi-Agent-Systeme

Grundmuster, die in (fast) allen Frameworks wiederkehren:

| Pattern | Beschreibung | Typisches Framework |
|---|---|---|
| **Sequential** | Agent A → Agent B → Agent C, linear | LangGraph, Microsoft Agent Framework |
| **Hierarchical/Supervisor** | Ein "Manager"-Agent delegiert an Spezialisten | CrewAI (hierarchical process), Microsoft Agent Framework |
| **Group Chat / Conversational** | Agenten "diskutieren" in einem gemeinsamen Chat-Verlauf | (klassisches) AutoGen GroupChat |
| **Handoff** | Ein Agent übergibt explizit die volle Kontrolle an einen anderen | OpenAI Agents SDK, Microsoft Agent Framework |
| **Concurrent/Parallel** | Mehrere Agenten arbeiten gleichzeitig an Teilaufgaben | LangGraph, Claude Agent SDK (Subagents) |

Für deine Use Cases (z. B. "Ticketanalyse-Agent" oder "DevOps-Assistent") ist meist ein **Supervisor-Pattern mit 2–4 Spezialisten-Subagenten** plus klar abgegrenzten Tools die pragmatischste Wahl – das hält die Komplexität für eine Praxisarbeit überschaubar, zeigt aber Multi-Agent-Konzepte konkret.

### 2.6 MCP – Model Context Protocol (zentrales Querschnittsthema)

Das ist vermutlich das wichtigste Einzelthema für deine Arbeit, weil es Open WebUI, alle Frameworks *und* Claude/Hermes verbindet.

**Was es ist:** Ein offener, von Anthropic im November 2024 veröffentlichter Standard, der definiert, wie eine "Host"-Anwendung (z. B. Open WebUI, Claude Desktop, Cursor) über "Clients" mit "Servern" spricht, die **Tools** (ausführbare Aktionen), **Resources** (lesbare Kontextdaten) und **Prompts** (wiederverwendbare Templates) bereitstellen. Die Analogie, die praktisch überall verwendet wird: *"USB-C für KI"* – ein Server wird einmal gebaut und funktioniert mit jedem MCP-fähigen Host.

**Wichtige Entwicklungen, die du kennen solltest:**

- **November 2024:** Initiale Veröffentlichung durch Anthropic, inkl. Referenz-Servern (GitHub, Slack, Google Drive, Postgres, Puppeteer).
- **März 2025:** Spezifikation 2025-03-26 bringt **Streamable HTTP** (Remote-Server, nicht mehr nur lokal über stdio) und ein **OAuth-2.1-basiertes Autorisierungsframework**.
- **Juni 2025:** Update klassifiziert MCP-Server explizit als OAuth-Resource-Server, neue Primitive wie **Elicitation** (Server kann Host/User proaktiv um zusätzliche Informationen bitten).
- **Juli 2025:** Formalisierter Governance-Prozess mit *Specification Enhancement Proposals (SEPs)* und Working Groups.
- **November 2025 (Spezifikation 2025-11-25):** aktueller stabiler Stand.
- **Dezember 2025:** Anthropic übergibt MCP an die neu gegründete **Agentic AI Foundation (AAIF)**, einen "directed fund" innerhalb der Linux Foundation, mitgegründet von Anthropic, Block und **OpenAI** – ein wichtiger Beleg dafür, dass MCP inzwischen tatsächlich herstellerübergreifend ist (OpenAI hatte MCP bereits ab März 2025 in eigene Produkte integriert).
- **2026:** Roadmap fokussiert auf Transport-Skalierbarkeit, Agent-zu-Agent-Kommunikation, Governance-Reife und Enterprise-Readiness (Audit-Trails, SSO-Auth, Gateway-Verhalten). Ein Release Candidate für **2026-07-28** bringt einen grundlegenden Umbau auf ein **zustandsloses Protokoll** (stateless), ein formales **Extensions-Framework** sowie eine verbindliche **Deprecation-Policy** (mind. 12 Monate zwischen Deprecation und Removal).

**Architekturbegriffe, die du in der Arbeit definieren solltest:** Host (App, die Kontext orchestriert) – Client (1:1-Verbindung pro Server) – Server (kapselt eine Fähigkeit) – Transport (stdio für lokal, Streamable HTTP für remote) – Tools/Resources/Prompts (die drei Primitive).

**Sicherheitsmodell von MCP (wichtig für dein Konzeptions-/Sicherheitskapitel):** MCP selbst erzwingt Sicherheit nicht auf Protokollebene, empfiehlt aber explizit: robuste Consent-/Autorisierungs-Flows, klare Dokumentation der Sicherheitsauswirkungen jedes Tools, Zugriffskontrollen und Datenschutzüberlegungen beim Server-Design. Tool-Beschreibungen/Annotationen eines nicht vertrauenswürdigen Servers sollen als **nicht vertrauenswürdig** behandelt werden – das ist ein zentraler Hebel gegen Prompt-Injection über Tool-Metadaten (siehe Kapitel 4).

**Einschätzung:** MCP ist 2026 de facto der Standard, an dem sich *alle* in deiner Aufgabenstellung genannten Frameworks (LangChain/LangGraph, Microsoft Agent Framework, CrewAI, Flowise, Dify) sowie Open WebUI und Claude orientieren. Es lohnt sich, MCP nicht nur als "ein Thema unter vielen" in der Grundlagenrecherche zu behandeln, sondern es als **roten Faden** durch die ganze Arbeit zu ziehen – das würde auch deine Architekturentscheidung im Konzeptionsteil natürlich motivieren ("Warum MCP als Integrationsschicht zwischen Open WebUI und dem gewählten Agenten?").

**Ressourcen:**
- Offizielle Spezifikation: https://modelcontextprotocol.io/specification/2025-11-25
- Roadmap 2026: https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- GitHub (Spec-Repo): https://github.com/modelcontextprotocol/modelcontextprotocol
- Release-Candidate-Ankündigung (Juli 2026): https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/

---

## 3. Markt- und Technologierecherche (Arbeitspaket 2)

### 3.1 Open WebUI – die Zielplattform

**Was es ist:** Ein selbst-hostbares, browserbasiertes Frontend für LLMs (lokal über Ollama oder per API z. B. zu OpenAI/Anthropic), entstanden als Nebenprojekt von Timothy Baek, inzwischen mit mehreren Zehntausend GitHub-Stars eines der bekanntesten Open-Source-Projekte in diesem Bereich.

**Erweiterbarkeits-Bausteine, die du für die Konzeption/Umsetzung brauchst:**

| Baustein | Zweck | Wann nutzen |
|---|---|---|
| **Native Features** | Eingebaute Systemfunktionen: Web Search, URL-Fetching, Bildgenerierung, Memory, Knowledge/RAG | Sofort nutzbar, kein Code |
| **Workspace Tools** | Python-Code, der *in-process* in Open WebUI läuft | Eigene Logik, eng integriert, am wenigsten Einschränkungen |
| **Functions/Pipes/Filters** | Plugin-API für tieferen Zugriff auf Request/Response-Lifecycle | Custom Auth, Kostenkontrolle, Routing, Post-Processing |
| **OpenAPI-Tool-Server** | Externer HTTP-Service mit OpenAPI-Spec, jeder Endpoint wird ein Tool | Bestehende REST-APIs einbinden, auch durch normale User (mit Berechtigung) |
| **MCP (Streamable HTTP)** | Nativ ab v0.6.31, nur Admin-konfigurierbar | Stateful, mächtige externe Capabilities (z. B. Dateisystem, DB) |
| **MCPO (Proxy)** | Bridged stdio-MCP-Server (die meisten Community-Server) zu OpenAPI | Wenn du einen bestehenden stdio-MCP-Server einbinden willst |
| **Pipelines** | Eigener, ausgelagerter Prozess für rechenintensive/komplexe Workflows | Nur bei fortgeschrittenen Setups nötig – laut Doku „meist nicht notwendig" |
| **Open Terminal** | Always-on, isolierter Docker-Container mit echter Shell/Dateisystem | Code-Ausführung, Datei-Handling für Agenten |

**Wichtige Detail-Erkenntnisse für dein Sicherheits-/Architekturkapitel:**

- MCP-Server können in Open WebUI **nur von Administratoren** hinzugefügt werden (nicht von normalen Usern) – bewusste Design-Entscheidung, weil ein MCP-Server stateful ist und mit vollem Scope des verbindenden Users laufen kann (Sampling, Elicitation, ggf. Shell-Befehle über stdio). Das ist ein direkter Bezug zu deiner Fragestellung „Datenschutz und Erweiterbarkeit" – mehr Mächtigkeit = mehr Admin-Kontrolle nötig.
- Ein offener Community-Feature-Request (Issue #24117 im open-webui-Repo) zeigt explizit das Szenario, das dich interessieren dürfte: **Hermes Agent** (von Nous Research, MIT-lizenziert, MCP-nativ) möchte Open WebUI nicht nur als MCP-*Client*, sondern Open WebUI selbst als MCP-*Server* ansprechen können, um z. B. Live-Status, Kosten oder Health-Daten direkt ins Open-WebUI-Interface zu pushen. Aktuell unterstützt Open WebUI MCP nur als Client (es kann nach außen verbinden, ist selbst aber kein MCP-Server) – eine konkrete Lücke, die du in deiner Konzeption als „noch offene Integrationsrichtung" benennen könntest.
- **Default Mode vs. Native (Agentic) Mode:** Open WebUI hat einen alten, Prompt-Injection-basierten Tool-Calling-Fallback ("Default Mode"), der mittlerweile als Legacy gilt und keine neuen Features mehr bekommt. Für deinen Prototyp solltest du explizit **Native Mode** mit einem Modell verwenden, das echtes Function Calling unterstützt.

**🎯 Lizenzfrage – wichtig für deine Bewertung „Open-Source-Plattform":** Open WebUI war ursprünglich BSD-3-Clause, wechselte aber im April 2025 (ab v0.6.6) zu einer **eigenen, nicht OSI-zugelassenen Lizenz** mit einer Branding-Schutzklausel: Du darfst Open WebUI weiterhin frei nutzen/verändern/weitergeben, musst aber das „Open WebUI"-Branding sichtbar lassen – außer bei (a) ≤ 50 Nutzern in 30 Tagen, (b) als anerkannter Substantial Contributor mit schriftlicher Erlaubnis, oder (c) mit einer bezahlten Enterprise-Lizenz. Code bis v0.6.5 bleibt BSD-3 (daher existieren Forks ab diesem Stand). Diese Änderung war in der Community umstritten (u. a. Diskussion auf Hacker News/Lobsters) und wird von manchen Wettbewerbern explizit als „nicht mehr richtig Open Source" bzw. „verhindert sinnvolle Forks" kritisiert.

Das ist ein **sehr guter, konkreter Diskussionspunkt** für deine wissenschaftliche Fragestellung, die explizit „Open-Source-Plattformen" thematisiert – du kannst hier zeigen, dass „Open Source" in der Praxis ein Spektrum mit echten rechtlichen Grauzonen ist (vgl. auch Dify in 3.2, das ebenfalls eine modifizierte Apache-2.0-Lizenz mit Multi-Tenant-Einschränkung nutzt).

**Einschätzung:** Open WebUI ist als Zielplattform gut gewählt – es ist die Plattform mit derzeit wohl breitester Community, größter Tool-Vielfalt und (mit Einschränkungen) echter MCP-Unterstützung. Für den Unternehmenseinsatz solltest du die Lizenzfrage und das Admin-Gating von MCP explizit in der Konzeption thematisieren.

**Ressourcen:**
- Doku-Übersicht: https://docs.openwebui.com/features/
- MCP-Integration: https://docs.openwebui.com/features/extensibility/mcp/
- Tools/Functions: https://docs.openwebui.com/features/extensibility/plugin/tools/
- Lizenz-FAQ: https://docs.openwebui.com/license/
- Community-Toolkit (Beispiel für fortgeschrittene Agenten-Integration): https://github.com/Haervwe/open-webui-tools
- Feature-Request „Open WebUI als MCP-Server" (sehr lesenswert für Architekturdiskussion): https://github.com/open-webui/open-webui/issues/24117

### 3.2 Agenten-Frameworks im Vergleich

#### 3.2.1 LangChain / LangGraph

- **LangChain**: Breites Komponenten-Baukasten-Framework (Modelle, Tools, Retriever, Document Loader), gut für lineare Pipelines/RAG/Prototyping, ca. 100k+ GitHub-Stars, sehr große Integrations-Bibliothek (1000+).
- **LangGraph**: Eigenes, niedrig-levelliges Orchestrierungs-Framework *auf* LangChain, modelliert Agentenabläufe als gerichteten (zyklischen) Graphen mit explizitem State, Checkpointing (→ Time-Travel-Debugging, Resume nach Fehlern), Human-in-the-Loop-Unterbrechungen. Erreichte 2025 die Version 1.0 und gilt in mehreren 2026er-Vergleichsartikeln als die meistgenutzte Multi-Agent-Orchestrierung überhaupt.
- Beide sind MIT-lizenziert (Framework), **LangSmith** (Observability/Tracing) ist das dazugehörige kommerzielle Zusatzprodukt.
- Gängige Faustregel aus mehreren Quellen: *LangChain für lineare/einfache Flows und schnelles Prototyping, LangGraph wenn Schleifen, Verzweigungen, Wiederaufnahme nach Fehlern oder Multi-Agent-Koordination nötig sind.*

#### 3.2.2 Microsoft Agent Framework (Nachfolger von AutoGen)

**Wichtig für deine Arbeit:** Falls deine Quellen/Dozenten noch "AutoGen" als aktuelles Framework erwarten – das hat sich geändert und ist ein guter Beleg für die Schnelligkeit dieses Feldes:

- **AutoGen** befindet sich seit Anfang 2026 im **Maintenance Mode** (nur noch Bugfixes/Security-Patches, keine neuen Features, community-verwaltet). Microsoft empfiehlt explizit neuen Projekten, stattdessen das **Microsoft Agent Framework (MAF)** zu nutzen.
- **AG2** (ag2ai/ag2) ist ein Community-Fork, der den alten AutoGen-v0.2-GroupChat-Stil weiterführt – relevant, falls du in älterer Literatur/Tutorials noch darauf stößt.
- **Microsoft Agent Framework**: Verschmilzt AutoGens Multi-Agent-Orchestrierungs-Patterns mit den Enterprise-Eigenschaften von **Semantic Kernel** (das ebenfalls in Maintenance Mode ist). Erreichte im Frühjahr 2026 Version **1.0 GA**. Bietet: deklarative YAML-Agentendefinitionen, Workflows (sequential/concurrent/handoff/group-chat/Magentic-One), native **MCP**- und **A2A** (Agent-to-Agent-Protokoll)-Unterstützung, Multi-Provider-Support inkl. **Anthropic Claude**, .NET- und Python-Laufzeit.

**🎯 Für deine Arbeit:** Wenn dein Themenvorschlag „AutoGen" als Beispiel nennt, lohnt sich eine kurze, explizite Anmerkung, dass du dich (mit Begründung: Maintenance Mode) für die Untersuchung des Nachfolgers Microsoft Agent Framework entschieden hast – das zeigt aktuelles Marktverständnis und ist genau die Art von Erkenntnis, die in einer guten Markt- und Technologierecherche gut ankommt.

#### 3.2.3 CrewAI

- Open-Source-Kern (MIT-lizenziert) + kommerzielle Schicht (**CrewAI AMP**, gehostete Cloud-Plattform; **CrewAI Factory**, containerisierte Self-Hosted-Variante für Unternehmen mit Datenschutzanforderungen).
- Zentrale Konzepte: **Crews** (Teams von Agenten mit Rollen/Zielen/"Backstory", die sequenziell, hierarchisch oder parallel zusammenarbeiten) und **Flows** (event-getriebene, zustandsbehaftete Workflow-Schicht darüber).
- Native MCP-Unterstützung sowie Sandbox-Integrationen (E2B, Daytona) für sichere Code-Ausführung.
- Sehr breite Adoption – laut eigenen (mit Vorsicht zu lesenden) Angaben Nutzung bei über 60 % der Fortune-500-Unternehmen.
- Lernkurve gilt als niedriger als LangGraph, dafür weniger granulare Kontrolle über den Ausführungsfluss.

#### 3.2.4 Flowise

- Open-Source (Apache 2.0), **Low-Code/No-Code visueller Builder** auf Basis von LangChain.js, drei Bausteine: **Assistant** (einfachster Einstieg), **Chatflow** (Single-Agent/RAG, flexibler), **Agentflow** (Superset, Multi-Agent + komplexe Workflows mit Verzweigung/Loop).
- Self-hostbar (Node.js/Docker), explizit für Teams gedacht, die Datenkontrolle wollen, aber keinen reinen Code-Ansatz.
- MCP-Unterstützung vorhanden (sowohl Custom-MCP-Client-Knoten als auch ein dediziertes Sicherheits-Hardening für MCP-Konfigurationen in jüngeren Releases) – allerdings zeigen die GitHub-Release-Notes auch eine Reihe sicherheitsrelevanter Fixes (Mass-Assignment-Schwachstellen, IDOR, Credential-Leaks), was für deinen Sicherheitsabschnitt ein gutes Beispiel ist, dass auch etablierte Tools laufend Schwachstellen patchen müssen.
- SSO/Enterprise-Features sind kostenpflichtig (Enterprise-only).

#### 3.2.5 Dify

- Open-Source-Plattform (**modifizierte Apache-2.0-Lizenz**, genannt „Dify Open Source License"), visuelle Workflow-Engine + eigene RAG-Pipeline (gilt in mehreren Quellen als eine der stärksten Out-of-the-box-RAG-Implementierungen unter den Low-Code-Tools) + Agentenfähigkeiten (Function Calling oder ReAct) + Backend-as-a-Service (jede App bekommt automatisch eine API).
- **Wichtige Lizenz-Einschränkung** (ähnlich wie bei Open WebUI ein guter Diskussionspunkt für deine Arbeit): Die Community Edition ist funktional vollständig und kostenlos selbst hostbar, **verbietet aber explizit den Betrieb als Multi-Tenant-Service** ohne kommerzielle Lizenz – relevant, falls dein Unternehmen Dify z. B. als Mandanten-Service für mehrere interne Abteilungen anbieten wollte.
- Seit 2026 **bidirektionale MCP-Unterstützung**: Dify kann sowohl als MCP-Client externe Server ansprechen als auch eigene Workflows/Agenten als MCP-Server nach außen exponieren (d. h. ein in Dify gebauter Agent wird z. B. von Claude Code aus aufrufbar) – ein konzeptionell sehr interessanter Kontrast zu Open WebUI, das (Stand jetzt) nur MCP-Client, nicht MCP-Server ist.
- Plus: **Human-Input-Node** für explizite Human-in-the-Loop-Unterbrechungen in Workflows.

#### 3.2.6 Vergleichstabelle (Ausgangspunkt für deine eigene Bewertungsmatrix)

| Kriterium | Open WebUI (+Agent) | LangGraph | Microsoft Agent Framework | CrewAI | Flowise | Dify |
|---|---|---|---|---|---|---|
| Lizenz Kern | „Open WebUI License" (BSD-3 + Branding-Klausel, nicht OSI) | MIT | MIT/Open Source | MIT (Kern) | Apache 2.0 | modif. Apache 2.0 (Multi-Tenant-Klausel) |
| Code-/No-Code | Plugin-System (Python) | Code (Python/JS) | Code (.NET/Python) | Code (Python) | Visuell (Low-Code) | Visuell (Low-Code) |
| MCP-Unterstützung | Client (Streamable HTTP, Admin-only) | über Adapter/Custom | Nativ (Client/Server) | Nativ | Nativ (Client) | Nativ, bidirektional (Client+Server) |
| Multi-Agent | über Community-Tools/Subagenten | Stark (Kernfeature) | Stark (mehrere Patterns) | Stark (Kernfeature) | Mittel (Agentflow) | Mittel |
| Self-Hosting/Datenschutz | Ja, primärer Use Case | Ja | Ja | Ja (Factory) | Ja | Ja (Community Edition) |
| Lernkurve | Niedrig (UI) bis hoch (Plugin-Dev) | Hoch | Mittel–Hoch | Mittel | Niedrig | Niedrig |
| Enterprise-Reife/Governance | Branding-/Lizenzfragen offen | Hoch (LangSmith) | Hoch (Azure/Foundry-Anbindung) | Hoch (Factory/AMP) | Mittel (SSO nur Enterprise) | Hoch (eigenes Lizenzmodell) |

**🎯 Für deine Arbeit:** Diese Tabelle ist ein Rohgerüst – du musst sie an die in deiner Aufgabenstellung genannten Kriterien (Installationsaufwand, Erweiterbarkeit, Tool-Integration, MCP-Unterstützung, Lokaler Betrieb, Datenschutz, Ressourcenbedarf, Benutzerfreundlichkeit) anpassen und **selbst** mit einer nachvollziehbaren Methodik (z. B. gewichtete Scorecard, Nutzwertanalyse) bewerten – das ist ein klassischer, von Prüfern gern gesehener Baustein für den Marktvergleich.

**Ressourcen:**
- LangGraph: https://www.langchain.com/langgraph
- Microsoft Agent Framework Übersicht: https://learn.microsoft.com/en-us/agent-framework/overview/
- AutoGen → MAF Migrationsguide: https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/
- CrewAI Doku: https://docs.crewai.com/en/introduction
- Flowise Doku: https://docs.flowiseai.com/
- Dify GitHub: https://github.com/langgenius/dify
- Dify-Lizenz (Volltext): https://github.com/langgenius/dify/blob/main/LICENSE

### 3.3 Deine Wunsch-Tools im Detail

#### 3.3.1 Claude / Claude API – Agent SDK, MCP-Connector, Managed Agents

Anthropic bietet für Agentenintegration mehrere, unterschiedlich tief gehende Bausteine – wichtig, dass du diese in deiner Arbeit klar unterscheidest:

1. **Tool Use (Messages API):** Grundlegendes Function-Calling-Feature der Claude-API – du definierst Tools mit JSON-Schema, Claude entscheidet, wann/wie es sie aufruft.
2. **MCP-Connector (Beta-Feature der Messages API):** Erlaubt es, MCP-Server **direkt aus der Messages API heraus** anzusprechen (per `mcp_servers`-Parameter), ohne einen eigenen MCP-Client zu implementieren – unterstützt aktuell nur Tool-Calls (nicht das volle MCP-Featureset), erfordert öffentlich erreichbare HTTP/SSE-Server (kein lokales stdio).
3. **Claude Agent SDK** (vormals „Claude Code SDK", umbenannt im September 2025): Das eigentliche Agenten-Framework von Anthropic – dieselbe Engine, die Claude Code antreibt. Bietet: vollwertige MCP-Unterstützung (lokal via stdio **und** In-Process-SDK-Server für eigene Tools), Subagenten, Hooks (deterministisches Eingreifen in den Agent-Loop), Skills, Permission-Handling, Sessions. Verfügbar für Python und TypeScript.
4. **Managed Agents API** (Beta, 2026): Eine noch höhere Abstraktionsebene – du deklarierst einen Agenten (inkl. MCP-Server-Liste) einmalig, und „Sessions" liefern dann zur Laufzeit erst die Auth-Credentials (Trennung von Agent-Definition und Secrets, praktisch für Multi-Tenant-Szenarien).

**Warum das für deine Arbeit relevant ist:** Du hast hier drei sinnvolle Integrationsoptionen, je nach Architekturentscheidung:
- **Direkt über die API + MCP-Connector**, wenn Open WebUI selbst (als Backend-Modell-Provider) Claude anspricht und Claude eigene MCP-Tools nutzen soll.
- **Über den Claude Agent SDK als eigenständigen "Agenten-Dienst"**, den Open WebUI z. B. über einen OpenAPI-Tool-Server oder eine eigene Pipeline anspricht (Open WebUI selbst bleibt das Chat-Frontend, der eigentliche Agentenverstand liegt im SDK-Prozess).
- **Claude als Modell-Backend** in einem der Frameworks aus 3.2 (LangChain/LangGraph, CrewAI, Microsoft Agent Framework unterstützen alle Anthropic-Modelle als Provider).

**Ressourcen:**
- MCP-Connector: https://docs.claude.com/en/docs/agents-and-tools/mcp-connector
- Agent SDK – MCP verbinden: https://platform.claude.com/docs/en/agent-sdk/mcp
- Agent SDK – Custom Tools: https://platform.claude.com/docs/en/agent-sdk/custom-tools
- Agent SDK Python (GitHub): https://github.com/anthropics/claude-agent-sdk-python
- Managed Agents – MCP Connector: https://platform.claude.com/docs/en/managed-agents/mcp-connector

#### 3.3.2 Claude Cowork

Ein im Januar/Februar 2026 als **Research Preview** gestarteter dritter Modus von Claude Desktop (neben Chat und Code), gedacht für **nicht-technische Wissensarbeit**: Claude bekommt Zugriff auf einen vom User freigegebenen lokalen Ordner und erledigt mehrstufige Aufgaben selbstständig (Dateien sortieren/umbenennen, Berichte aus Quelldateien zusammenstellen, Recherchen synthetisieren) – baut auf derselben Agenten-Architektur/SDK wie Claude Code auf, nur mit vereinfachter, nicht-CLI-Oberfläche.

**Relevante technische/konzeptionelle Punkte für deine Arbeit:**
- Läuft auf dem **Claude Agent SDK** (siehe 3.3.1) – das verdeutlicht den Baukasten-Charakter: derselbe Unterbau treibt Claude Code, Claude Cowork und (potenziell) deinen eigenen Prototyp an.
- Unterstützt **Plugins** (Bündel aus Skills/Connectors/Slash-Commands/Sub-Agenten für bestimmte Rollen), die Anthropic teils open-source zur Verfügung stellt (`anthropics/knowledge-work-plugins`).
- **Wichtige Einschränkungen** (Stand Research Preview, relevant für deine Sicherheits-/Reifegrad-Einordnung): kein geräteübergreifendes Memory, Sessions enden mit Schließen der Desktop-App, aktuell **nicht für regulierte Daten empfohlen** (keine Audit-Logs/Compliance-API/Data-Export), Vorsicht bei vagen Prompts (kann unbeabsichtigt Dateien löschen), Prompt-Injection über Dateiinhalte als ungelöstes Risiko explizit benannt.
- Nur macOS, nur Claude-Max-Abo, Stand der Recherche.

**Einschätzung:** Claude Cowork ist **kein** Open-Source-Tool und läuft nicht "in" Open WebUI – es ist trotzdem ein hervorragendes **Referenzbeispiel** in deiner Arbeit für: (a) wie ein kommerzieller Anbieter dieselbe Agenten-Architektur für verschiedene Zielgruppen verpackt, und (b) wie ernst Anthropic die Risiken von Dateisystem-Zugriff durch Agenten nimmt (explizite Warnungen zu Prompt Injection und destruktiven Aktionen) – guter Vergleichspunkt zu deinem eigenen Sicherheitskapitel.

**Ressourcen:**
- Produktseite: https://claude.com/product/cowork
- Anthropic-Ankündigung: https://www.anthropic.com/product/claude-cowork
- Offene Plugin-Sammlung: https://github.com/anthropics/knowledge-work-plugins
- YouTube-Demo (von dir verlinkt): https://www.youtube.com/watch?v=MgOgyJf16GU

#### 3.3.3 Hermes Agent (Nous Research) – überraschend hohe Relevanz

**Wichtig:** Unterscheide klar zwischen **Hermes-LLMs** (offene Gewichte/Modelle von Nous Research, z. B. via Ollama/GGUF lokal lauffähig) und **Hermes Agent** (separates, im Februar 2026 veröffentlichtes Agenten-Framework). Hermes Agent nutzt standardmäßig die Hermes-Modelle, ist aber modellagnostisch und läuft auch mit Claude, GPT, Gemini oder lokalen Ollama-Modellen.

**Eigenschaften, die für deine Arbeit besonders interessant sind:**
- **MIT-lizenziert, vollständig self-hosted**, läuft als persistenter Daemon auf eigener Infrastruktur (auch auf einem 5-€-VPS).
- **Persistentes Gedächtnis über Sessions hinweg** (FTS5-Volltextsuche + LLM-Summarization) – löst explizit ein Problem, das viele session-basierte Agenten (auch Claude Code) noch nicht lösen.
- **Selbst-verbessernde "Skills"**: Nach jeder Aufgabe bewertet der Agent den Erfolg und speichert wiederverwendbare Lösungsmuster als Markdown-Dateien ab; laut Herstellerangaben dadurch ca. 40 % schnellere Bearbeitung ähnlicher Folgeaufgaben (Stand: ungeprüfte Eigenangabe, für die Arbeit als solche kennzeichnen!).
- **Spricht MCP nativ** – sowohl als Client als auch (laut dem oben genannten GitHub-Issue #24117) potenziell als Gegenstück für Open WebUI als MCP-Server.
- Eingebauter Cron-Scheduler, Anbindung an 16+ Messaging-Plattformen, sechs Terminal-Backends (lokal, Docker, SSH, Singularity, Modal, Daytona), explizit auch als Plattform zur Generierung von Trainingsdaten/RL-Trajektorien gedacht (Atropos-Integration).

**🎯 Für deine Arbeit – konkreter Vorschlag:** Hermes Agent wäre ein hervorragender Kandidat für deinen **Prototyp-Use-Case**, weil es (anders als Pi, siehe unten) tatsächlich (a) Open-Source, (b) self-hostbar, (c) explizit MCP-nativ und (d) bereits in der Open-WebUI-Community als Integrationsidee diskutiert ist. Ein realistischer Demonstrator wäre z. B.: Hermes Agent als MCP-Server/-Client-Gegenstück, das über MCPO/OpenAPI oder eine eigene Bridge mit Open WebUI verbunden wird, um z. B. einen "Wissensdatenbank-Agent" oder "DevOps-Assistenten" (aus deiner Aufgabenstellung) mit persistentem Gedächtnis zu realisieren.

**Ressourcen:**
- GitHub: https://github.com/NousResearch/hermes-agent
- Offizielle Doku: https://hermes-agent.nousresearch.com/docs
- Install-Skript: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Open-WebUI-Integrationsdiskussion: https://github.com/open-webui/open-webui/issues/24117

#### 3.3.4 Pi (Inflection AI) – Einordnung & Erwartungsmanagement

**Ehrliche Einschätzung, weil das für deine Themenwahl wichtig ist:** Pi ist ein **proprietärer, konsumentenorientierter Companion-Chatbot** ("emotional intelligente KI"), kein Agenten-Framework, nicht Open Source, nicht für Unternehmens- oder Entwickler-Integration in dem Sinne gedacht, wie deine Fragestellung es braucht. Hintergrund: Inflection AI verlor 2024 große Teile des Gründerteams an Microsoft (Mustafa Suleyman, Karén Simonyan wechselten zu Microsoft AI); Pi existiert 2026 weiter als Consumer-App (iOS/Android/Web), wird aber laut mehreren – mit Vorsicht zu lesenden, teils werblichen – Quellen primär als persönlicher, empathischer Assistent positioniert, nicht als Tool-/Agent-Plattform. Es gibt zwar eine "Enterprise"-Variante mit API und "Persona Plugins", aber keine belastbaren Hinweise auf MCP-Unterstützung, Tool-Calling-Ökosystem oder Open-Source-Charakter.

**🎯 Für deine Arbeit:** Ich würde Pi **nicht** als vollwertigen Vergleichskandidaten in der Marktanalyse führen, sondern höchstens in einem Satz als **Negativ-Abgrenzung** nutzen: "Im Gegensatz zu den untersuchten Agenten-Frameworks/-Plattformen ist Pi ein geschlossenes, konsumentenorientiertes System ohne relevante Tool-/MCP-Integration und fällt damit aus dem Betrachtungsrahmen dieser Arbeit." Das ist legitim und zeigt, dass du eine bewusste Abgrenzung getroffen hast, statt das Thema einfach zu ignorieren.

**Ressourcen (zur Einordnung, mit Vorsicht zu lesen):**
- Offizielle Seite: https://pi.ai / https://inflection.ai/
- Hintergrund zur Microsoft-Übernahme: https://spectrum.ieee.org/inflection-ai-pi

### 3.4 Zusammenfassende Einschätzung Kapitel 3

Für deine Aufgabenstellung (Unternehmenseinsatz, Datenschutz, Erweiterbarkeit, Entwicklungsaufwand) zeichnet sich aus der Recherche ein klarer Favoritenkreis ab:

- **Plattform:** Open WebUI (vorgegeben) – mit klar benannter Lizenz-Einschränkung.
- **Integrationsschicht:** MCP – durchgängig unterstützt von praktisch allen relevanten Akteuren (Open WebUI als Client, alle Frameworks, Claude, Hermes Agent).
- **Agenten-Implementierung für den Prototyp – zwei sinnvolle Pole:**
  - *"Framework-Pol":* LangGraph oder Microsoft Agent Framework für ein sauberes, gut dokumentiertes Multi-Agent-Konzept mit Anthropic-Claude als Modell-Backend.
  - *"Tool-Pol" (innovativer, näher an deinen Wunsch-Tools):* Hermes Agent als self-hosteter, MCP-nativer Agent, der via MCPO/OpenAPI-Bridge an Open WebUI angebunden wird – das wäre fachlich näher an dem, was du ursprünglich mit Claude/Hermes andeuten wolltest, und zugleich ein noch nicht "ausgelutschtes" Vergleichsbeispiel in der Literatur.

**🎯 Diese Wahl triffst du** – aber beide Pole sind durch die Recherche oben mit konkreten Quellen/Repos unterlegt.

---

## 4. Sicherheit, Datenschutz, Einfachheit – Querschnitts-Einordnung

Deine Aufgabenstellung verlangt explizit eine Sicherheitsbetrachtung in der Konzeption – hier die wichtigsten 2026er-Eckpunkte, geordnet nach Relevanz für deine Arbeit:

### 4.1 OWASP Top 10 for Agentic Applications (2026)

Im Dezember 2025 veröffentlicht, ergänzt die seit Jahren etablierte **OWASP Top 10 for LLM Applications** um Risiken, die erst durch Autonomie, Tool-Nutzung und Multi-Agent-Interaktion entstehen. Zentrale, für deine Arbeit zitierfähige Kategorien:

- **ASI01 – Agent Goal Hijack:** Eine erfolgreiche Prompt-Injection wirkt nicht mehr nur auf eine einzelne Antwort, sondern kann Planung und mehrstufiges Verhalten des gesamten Agenten umlenken (z. B. andere Tools auswählen lassen als beabsichtigt).
- **Tool Misuse & Exploitation:** Missbrauch/Manipulation von Tool-Aufrufen, z. B. über manipulierte Tool-Beschreibungen (→ direkter Bezug zum MCP-Sicherheitshinweis aus 2.6, dass Tool-Annotationen nicht vertrauenswürdiger Server als nicht vertrauenswürdig zu behandeln sind).
- **Memory/Context Poisoning:** Persistentes Gedächtnis (z. B. bei Hermes Agent, Claude Cowork, Open-WebUI-Memory-Feature) wird zur Angriffsfläche, wenn vergiftete Informationen über Sessions hinweg "haften bleiben".
- **Multi-Agent-spezifische Risiken:** Agenten vertrauen sich gegenseitigen Nachrichten oft implizit ("interne Angriffsfläche ohne externen Angreifer nötig") – relevant, wenn du ein Supervisor-/Multi-Agent-Konzept umsetzt.
- Ergänzend relevant: Die **OWASP GenAI Security Project**-Berichte für 2026 dokumentieren inzwischen reale CVEs/Vorfälle statt nur theoretischer Risiken – u. a. wird explizit auf Coding-Agenten (Claude Code, Cline, etc.) als größte Kategorie realer Vorfälle verwiesen, sowie auf das **NIST AI Agent Standards Initiative** (Februar 2026) als erstes US-Regierungsframework speziell für autonome KI-Agenten.

### 4.2 MCP-spezifische Sicherheitsaspekte (Vertiefung zu 2.6)

- Tool-Aufrufe sind **beliebige Codeausführung** – das ist eine explizite, wörtliche Warnung der MCP-Spezifikation selbst, kein übertriebenes Risiko-Framing.
- Open WebUI reagiert darauf mit **Admin-only MCP-Konfiguration** (siehe 3.1) – ein konkretes, sehr gut zitierbares Beispiel dafür, wie eine Plattform das abstrakte MCP-Sicherheitsmodell in eine konkrete Rollen-/Rechte-Architektur übersetzt.
- Auth-Optionen in der Praxis (Open WebUI als Beispiel): "None" (nur für vertrauenswürdige interne Netze), Bearer-Token, OAuth 2.1 (mit/ohne Dynamic Client Registration) – guter Anknüpfungspunkt, um in deiner Konzeption ein konkretes Auth-Modell für deinen Prototyp zu begründen.

### 4.3 Datenschutz/DSGVO-Perspektive (für den Unternehmenseinsatz)

Hier wird die wissenschaftliche Arbeit von dir eigene Einordnung verlangen – die Recherche liefert dir aber die Bausteine:

- **Self-Hosting (Open WebUI + lokales/eigenes LLM via Ollama, oder Hermes Agent + lokales Modell)** = Datenhoheit bleibt im Unternehmen, aber Betriebsverantwortung (Patching, Verfügbarkeit, Skalierung) liegt vollständig bei dir.
- **Cloud-API-Nutzung (z. B. Claude-API)** = Datenschutzfragen verschieben sich auf Auftragsverarbeitungsverträge, Datenresidenz (Anthropic bietet z. B. eine "US-only inference"-Option), Modelltraining-Ausschluss-Klauseln etc. – das wäre ein Punkt, den du über die **product-self-knowledge**-würdigen offiziellen Anthropic-Quellen (Trust Center/Datenschutzrichtlinien) selbst nachschlagen solltest, falls du konkrete vertragliche Aussagen treffen willst.
- **Hybrid (lokales Frontend Open WebUI, aber Cloud-Modell als Backend)** ist in der Praxis der häufigste Kompromiss – auch das ist ein guter Diskussionspunkt für deine Konzeption.

### 4.4 "Einfachheit" / Usability als Bewertungsdimension

Aus der Recherche lässt sich eine grobe Reifegrad-/Einfachheits-Hierarchie ableiten, die du in deiner Bewertungsmatrix nutzen kannst:

1. **Am einfachsten (No-Code):** Flowise/Dify visuelle Builder, Open WebUI native Features.
2. **Mittel (Low-Code/Konfiguration):** Open WebUI Tools/OpenAPI-Server, CrewAI (deklarative Rollen/Tasks).
3. **Anspruchsvoller (Code-first):** LangGraph, Microsoft Agent Framework, Claude Agent SDK.
4. **Am voraussetzungsreichsten (Infrastruktur + Betrieb):** Hermes Agent (eigener Daemon, VPS/Hosting, Terminal-Backends), produktionsreife MCP-Server mit OAuth.

**Ressourcen:**
- OWASP Top 10 Agentic Applications – Übersichtsartikel: https://secops.group/blog/securing-agentic-ai-the-owasp-top-10-and-beyond/
- Praktischer Leitfaden mit Risiko-Details: https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications
- Aktuelle Vorfallslage (2026): https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/
- NIST/weitere Vorfälle, gut referenziert: https://www.lumenova.ai/blog/agentic-ai-risks-owasp-nist/

---

## 5. Konzeption – Architektur & Use Cases (Arbeitspaket 3)

Deine Aufgabenstellung nennt fünf Beispiel-Use-Cases. Hier eine erste architektonische Einordnung, die du vertiefen kannst:

| Use Case | Sinnvoller Agenten-Zuschnitt | Typische Tools/MCP-Server | Bezug zu deinen Wunsch-Tools |
|---|---|---|---|
| **Code-Review-Agent** | Single-Agent mit Git-/Linting-Tools, ggf. Subagent für Sicherheits-Scan | GitHub-MCP-Server, statische Analyse-Tools | Claude Agent SDK ist hierfür quasi der Referenzfall (Basis von Claude Code) |
| **Wissensdatenbank-Agent** | Agentic-RAG über Open WebUI Knowledge + externer Vektor-DB | Open WebUI native RAG, ggf. Graph-RAG-MCP-Server | Hermes Agent (persistentes Gedächtnis) als Alternative/Ergänzung |
| **Dokumentations-Agent** | Plan-and-Execute: Quellen sammeln → strukturieren → Dokument erzeugen | Filesystem-/Confluence-MCP-Server | Claude Cowork als Inspirationsquelle für den Workflow |
| **Ticketanalyse-Agent** | Supervisor + Klassifikations-/Routing-Subagent | Jira/Zendesk-MCP- oder OpenAPI-Server | CrewAI (rollenbasiert: "Analyst", "Router") gut geeignet |
| **DevOps-Assistent** | Multi-Agent mit Terminal-/Monitoring-Zugriff, hohe Sicherheitsanforderungen | Open Terminal (Open WebUI), SSH/Docker-MCP-Server | Hermes Agent (Terminal-Backends) sehr passend, aber höchste Sicherheitsanforderung |

**🎯 Für deine Arbeit:** Wähle **einen** Use Case für den Prototyp aus und begründe die Wahl explizit mit den Kriterien aus deiner Aufgabenstellung (Datenschutz, Erweiterbarkeit, Entwicklungsaufwand). Der **Wissensdatenbank-Agent** oder **Dokumentations-Agent** sind erfahrungsgemäß am realistischsten in der für eine Praxisarbeit verfügbaren Zeit umsetzbar (kein produktiver Zugriff auf kritische Systeme nötig), zeigen aber trotzdem RAG, Tool-Calling und MCP konkret.

**Architekturskizze (textuell, als Ausgangspunkt für ein Diagramm in deiner Arbeit):**

```
[Open WebUI – Frontend/Chat]
        │  (Native Mode, Function Calling)
        ▼
[Modell-Backend: lokal via Ollama  ODER  Cloud via Claude-API]
        │
        ▼
[MCP-Verbindung: Admin-konfigurierter MCP-Server ODER OpenAPI-Tool-Server]
        │
        ▼
[Agenten-Logik: z. B. eigener MCP-Server, der intern Hermes Agent / LangGraph / Claude Agent SDK aufruft]
        │
        ▼
[Externe Systeme: Wissensdatenbank, Filesystem, Ticketsystem, Terminal, …]
```

---

## 6. Prototypische Umsetzung – konkrete Schritt-für-Schritt-Ressourcen (Arbeitspaket 4)

Hier die konkreten, technisch belastbaren Einstiegspunkte, je nach Architekturentscheidung:

### 6.1 Open WebUI lokal aufsetzen
- Schnellstart per Docker (offizielle Doku, Versionsangaben prüfen): https://docs.openwebui.com/
- Wichtig: Mindestversion **v0.6.31** für native MCP-Unterstützung; `WEBUI_SECRET_KEY` setzen (sonst brechen OAuth-verbundene Tools bei jedem Neustart).

### 6.2 Eigenen MCP-Server bauen und anbinden
- Offizielle MCP-Schnellstart-SDKs (Python/TypeScript/C#/Java/Swift): https://modelcontextprotocol.io/
- Referenz-/Beispiel-Server (Filesystem, Git, Postgres, Memory) als Vorlage: https://github.com/open-webui/openapi-servers (zeigt zusätzlich den Bridge-Weg MCP ↔ OpenAPI, falls dein Server stdio-basiert ist)
- Einbindung in Open WebUI: Admin Settings → External Tools → "+" → Type "MCP (Streamable HTTP)".

### 6.3 Claude als Modell-Backend + eigene Tools
- Tool-Use-Tutorial (Einstieg): https://platform.claude.com/docs/en/agents-and-tools (Doku-Map zuerst aufrufen, da sich Pfade/Versionen ändern)
- Agent-SDK-Schnellstart (Python-Beispiel mit MCP-Server): https://code.claude.com/docs/en/agent-sdk/overview

### 6.4 Hermes Agent self-hosted aufsetzen (falls du diesen Pol wählst)
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
- Danach: Provider konfigurieren (z. B. eigener Ollama-Endpoint oder Anthropic-API-Key), MCP-Tools/Skills aktivieren, optional als systemd-Service für Dauerbetrieb.
- Doku: https://hermes-agent.nousresearch.com/docs

### 6.5 Framework-Variante (falls du LangGraph/CrewAI/MAF wählst)
- LangGraph Quickstart/Academy-Kurs (kostenlos): über https://www.langchain.com/langgraph verlinkt
- CrewAI Doku/Quickstart: https://docs.crewai.com/en/introduction
- Microsoft Agent Framework Quickstart (Python/.NET): https://learn.microsoft.com/en-us/agent-framework/overview/

**🎯 Für deine Arbeit:** Dokumentiere im Prototyp-Kapitel explizit **Versionsnummern** aller verwendeten Komponenten (Open WebUI-Version, Modell-Version, ggf. Framework-Version) – bei einem derart schnell wandelnden Themenfeld ist das für die Nachvollziehbarkeit/Reproduzierbarkeit deiner Arbeit besonders wichtig (und wird in der Verteidigung sicher nachgefragt).

---

## 7. Evaluation – Kriterien & Vorgehen (Arbeitspaket 5)

Deine Aufgabenstellung nennt: Funktionalität, Qualität der Ergebnisse, Performance, Erweiterbarkeit, Wartbarkeit, Eignung für Unternehmenseinsatz, Vergleich mit mind. einer Alternativlösung. Konkretisierungsvorschläge je Kriterium:

| Kriterium | Mögliche Messgröße/Vorgehen |
|---|---|
| Funktionalität | Definierte Testfälle/User Stories pro Use Case, Erfolgsquote |
| Qualität der Ergebnisse | Stichprobenbewertung (z. B. Rubric/Scoring-Schema), ggf. LLM-as-Judge mit Begründung der Methodik |
| Performance | Latenz (Time-to-first-token, Time-to-completion), Tool-Call-Anzahl pro Aufgabe, Token-/Kostenverbrauch |
| Erweiterbarkeit | Aufwand (LOC/Zeit), um einen zusätzlichen Tool/Use-Case anzubinden |
| Wartbarkeit | Versionsstabilität (Maintenance-Mode-Beispiel AutoGen!), Abhängigkeitsgraph, Dokumentationsqualität |
| Unternehmenseignung | Lizenzmodell, Datenschutz/Self-Hosting-Fähigkeit, Auth/RBAC, Auditierbarkeit |
| Alternativvergleich | Mindestens einer der Frameworks aus 3.2 als Kontrastfolie zur gewählten Lösung |

**Einschätzung:** Da OWASP/NIST 2026 explizit auf **reale Vorfälle statt nur Theorie** verweisen (siehe 4.1), wäre ein eigener, kleiner **Security-Self-Assessment-Abschnitt** (z. B. anhand der OWASP-Top-10-Agentic-Kategorien als Checkliste auf deinen Prototyp angewendet) ein sehr starker, aktueller Beitrag im Evaluationskapitel – das hebt deine Arbeit von rein funktionalen Bewertungen ab.

---

## 8. Gesamteinschätzung & Empfehlung für den weiteren Weg

Kurz zusammengefasst, meine ehrliche Einschätzung als Lese-/Recherchehilfe (keine Bewertung, die du übernehmen musst – aber als Diskussionsgrundlage gedacht):

1. **MCP als roter Faden** über die ganze Arbeit zu ziehen, ist inhaltlich naheliegend und durch die Marktentwicklung (AAIF-Übergabe, OpenAI-Adoption, Unterstützung in *allen* untersuchten Tools) gut belegbar.
2. **Open WebUIs Lizenzänderung** und **Difys Multi-Tenant-Klausel** sind zwei konkrete, gut zitierbare Beispiele, um "Open Source" in deiner Arbeit kritisch zu hinterfragen, statt es unreflektiert vorauszusetzen – das wird in einer wissenschaftlichen Arbeit positiv auffallen.
3. Von deinen vier Wunsch-Tools sind **Claude (API/Agent SDK)** und **Hermes Agent** inhaltlich am tragfähigsten für eine echte Integration/einen Prototyp. **Claude Cowork** ist ein gutes *Referenz-/Vergleichsbeispiel*, aber kein Bestandteil einer Open-WebUI-Integration. **Pi** würde ich, wie oben begründet, nur als kurze Abgrenzung erwähnen.
4. AutoGen als in deiner Aufgabenstellung genanntes Beispiel ist **technisch überholt** (Maintenance Mode) – die Untersuchung des Nachfolgers (Microsoft Agent Framework) statt des Namens aus der Aufgabenstellung zeigt aktuelles Marktverständnis und sollte explizit begründet werden.
5. Die **Sicherheitsbetrachtung** lässt sich 2026 auf eine ungewöhnlich konkrete Evidenzbasis stützen (OWASP Top 10 Agentic 2026, NIST-Initiative, dokumentierte CVEs) – nutze das, um über generische "Prompt Injection ist ein Risiko"-Aussagen hinauszukommen.

---

## 9. Konsolidiertes Quellenverzeichnis

**Modell Context Protocol**
- https://modelcontextprotocol.io/specification/2025-11-25
- https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- https://github.com/modelcontextprotocol/modelcontextprotocol
- https://www.webfuse.com/mcp-cheat-sheet

**Open WebUI**
- https://docs.openwebui.com/features/
- https://docs.openwebui.com/features/extensibility/mcp/
- https://docs.openwebui.com/features/extensibility/plugin/tools/
- https://docs.openwebui.com/features/extensibility/pipelines/
- https://docs.openwebui.com/license/
- https://github.com/open-webui/open-webui/issues/24117
- https://github.com/open-webui/openapi-servers
- https://github.com/Haervwe/open-webui-tools
- https://deepwiki.com/open-webui/docs/6.1-licensing-and-governance
- https://news.ycombinator.com/item?id=43901575 (Diskussion Lizenzänderung)

**Frameworks**
- https://www.langchain.com/langgraph
- https://learn.microsoft.com/en-us/agent-framework/overview/
- https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/
- https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/
- https://github.com/microsoft/autogen
- https://docs.crewai.com/en/introduction
- https://crewai.com/open-source
- https://en.wikipedia.org/wiki/CrewAI
- https://docs.flowiseai.com/
- https://github.com/FlowiseAI/Flowise
- https://github.com/langgenius/dify
- https://github.com/langgenius/dify/blob/main/LICENSE

**Claude / Anthropic**
- https://docs.claude.com/en/docs/agents-and-tools/mcp-connector
- https://platform.claude.com/docs/en/agent-sdk/mcp
- https://platform.claude.com/docs/en/agent-sdk/custom-tools
- https://github.com/anthropics/claude-agent-sdk-python
- https://platform.claude.com/docs/en/managed-agents/mcp-connector
- https://www.anthropic.com/product/claude-cowork
- https://claude.com/product/cowork
- https://github.com/anthropics/knowledge-work-plugins
- https://www.anthropic.com/news/claude-opus-4-6

**Hermes Agent / Nous Research**
- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/docs (in obiger Recherche referenziert)

**Pi / Inflection AI**
- https://inflection.ai/
- https://spectrum.ieee.org/inflection-ai-pi

**Sicherheit**
- https://secops.group/blog/securing-agentic-ai-the-owasp-top-10-and-beyond/
- https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications
- https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/
- https://www.lumenova.ai/blog/agentic-ai-risks-owasp-nist/
- https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/

**RAG/Agentic RAG**
- https://aimultiple.com/agentic-rag
- https://www.techment.com/blogs/rag-architectures-enterprise-use-cases-2026/

---

## 10. Weiterführende Ressourcen zum Selbststudium

**Communities/Foren (für aktuellen Stand, nicht als Zitierquelle für die Arbeit gedacht, aber gut zum Mitlesen):**
- MCP Contributor Discord (verlinkt von https://blog.modelcontextprotocol.io)
- Open WebUI Discord/GitHub Discussions: https://github.com/open-webui/open-webui/discussions
- r/LocalLLaMA, r/LangChain (Reddit) – guter Praxis-Pulsmesser, aber nicht zitierfähig

**Kurse/Tutorials:**
- LangChain Academy (kostenloser LangGraph-Kurs, verlinkt von https://www.langchain.com/langgraph)
- Anthropic Academy / Skilljar-Kurse zu Claude/Cowork: https://anthropic.skilljar.com/

**Offizielle Dokumentations-Einstiegspunkte (immer zuerst hier nach aktuellem Stand schauen):**
- https://docs.claude.com (Claude API/Agent SDK)
- https://docs.openwebui.com
- https://modelcontextprotocol.io
- https://docs.crewai.com
- https://docs.flowiseai.com
- https://docs.dify.ai (Dify, nicht im Detail oben verlinkt – direkt prüfen)
- https://learn.microsoft.com/en-us/agent-framework

**Zur Selbstrecherche bei Abgabe-Nähe nochmal aktualisieren:**
- MCP-Spezifikationsstand (RC für 28.07.2026 – könnte bei Abgabe bereits final sein)
- Open-WebUI-Versionsstand und etwaige weitere Lizenzänderungen
- Microsoft Agent Framework GA-Status / Process-Framework-Termin
- Claude-Modellversionen (Modellbezeichnungen ändern sich regelmäßig)

---

*Dieses Dossier wurde am 24. Juni 2026 mithilfe von Web-Recherche zusammengestellt. Es ersetzt nicht das eigene kritische Prüfen der Primärquellen – insbesondere bei Lizenz-, Preis- und Versionsangaben, die sich schnell ändern können.*s