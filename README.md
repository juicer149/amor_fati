# Amor Fati

Amor Fati är ett personligt projekt som syftar till att skapa ett system för att logga och vikta aktiviteter över tid, baserat på deras inverkan på personlig utveckling och välmående.

Projektet är under aktiv utveckling och kommer att utvecklas i flera större versioner, där 1.0 fokuserar på grundläggande funktionalitet.

---

## Projektstruktur

amor_fati/ ├── config/activities/ # YAML-filer som definierar aktiviteter ├── src/amorfati/ # Applikationskod │ ├── core/ # Kärnmodeller (Activity, Factory etc) │ ├── features/ # Funktionalitet som score-kalkylering │ ├── storage/ # Hantering av data/repository │ ├── utils/ # Hjälpmoduler som YAML-hantering │ └── cli/ # Command Line Interface (CLI) ├── templates/ # Mallar för att skapa nya YAML-aktiviteter ├── tests/ # Enkla tester för kodbasen ├── Makefile # Hjälper till att köra återkommande kommandon └── project.toml # (för framtida verktyg som Poetry)


Planerade större versioner

    v1.0: Grundfunktionalitet (logging och beräkning av aktivitetspoäng)

    v1.5: Förbättrad CLI och intern logik, utökad testning

    v2.0: Dynamiska aktiviteter, baserade på fysiologisk och emotionell data

    v3.0: AI-modul för mönsterigenkänning och adaptiva rekommendationer


Om Projektet

Detta projekt är starkt personligt inspirerat och reflekterar en strävan att integrera filosofi (Amor Fati - "älska ditt öde"), träning, medveten närvaro och datadriven utveckling i ett och samma system.

Projektet utvecklas främst som ett showcase för personlig utveckling inom programmering, systemarkitektur och AI.
