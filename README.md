# Amor Fati

Amor Fati är ett personligt projekt som syftar till att skapa ett system för att logga och vikta aktiviteter över tid, baserat på deras inverkan på personlig utveckling och välmående.

Projektet är under aktiv utveckling och kommer att utvecklas i flera större versioner, där 1.0 fokuserar på grundläggande funktionalitet.

---

## Projektstruktur

## Projektstruktur

amor_fati/
├── config/activities/                # YAML-filer som definierar aktiviteter
│   ├── alcohol.yaml
│   ├── cold_shower.yaml
│   ├── meditation/
│   │   └── free_breathing.yaml
│   ├── sauna.yaml
│   └── training/
│       ├── mobility.yaml
│       ├── prehab.yaml
│       ├── strenght_training.yaml
│       └── trail_running.yaml
├── src/amorfati/                     # Applikationskod
│   ├── core/                         # Kärnmodeller (Activity, Factory etc)
│   │   ├── activity.py
│   │   └── factory.py
│   ├── features/                     # Funktionalitet som score-kalkylering
│   │   └── score_calculator.py
│   ├── storage/                      # Hantering av data/repository
│   │   └── repository.py
│   ├── utils/                        # Hjälpmoduler som YAML-hantering
│   │   ├── __pycache__/
│   │   ├── create_activity.py
│   │   ├── loader.py
│   │   └── yaml_handler.py
│   └── cli/                          # Command Line Interface (CLI)
│       └── main.py
│
├── templates/                        # Mallar för att skapa nya YAML-aktiviteter
│   └── activity_template.yaml
├── tests/                            # Enkla tester för kodbasen
│   └── test_activity.py
├── Makefile                          # Hjälper till att köra återkommande kommandon
├── project.toml                      # För framtida verktyg som Poetry
└── README.md                         # Dokumentation av projektet


Planerade större versioner

    v1.0: Grundfunktionalitet (logging och beräkning av aktivitetspoäng)

    v1.5: Förbättrad CLI och intern logik, utökad testning

    v2.0: Dynamiska aktiviteter, baserade på fysiologisk och emotionell data

    v3.0: AI-modul för mönsterigenkänning och adaptiva rekommendationer


Om Projektet

Detta projekt är starkt personligt inspirerat och reflekterar en strävan att integrera filosofi (Amor Fati - "älska ditt öde"), träning, medveten närvaro och datadriven utveckling i ett och samma system.

Projektet utvecklas främst som ett showcase för personlig utveckling inom programmering, systemarkitektur och AI.
