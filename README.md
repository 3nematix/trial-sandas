# Book Library

Fizinės knygų bibliotekos sistema, realizuota naudojant OOP Python kalba.

## Funkcionalumas

- Knygos kūrimas (pavadinimas, autorius, metai)
- Knygos kopijos įsigijimas — prideda naują kopiją į kolekciją
- Knygos kopijos skolinimas — pažymi kopiją kaip pasiskolintą
- Knygos kopijos grąžinimas — pažymi kopiją kaip prieinamą
- Paieška — randa kopijas pagal tikslų autoriaus/pavadinimo atitikimą, surūšiuotas pagal metus (naujausios pirmos)

## Reikalavimai

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Pradžia

```bash
make uv       # Jei uv dar neįdiegtas
make project
```

## Komandos

```
make help     - Rodyti galimas komandas
make uv       - Įdiegti uv paketų tvarkyklę
make project  - Sukurti venv ir įdiegti priklausomybes
make install  - Įdiegti paketą redagavimo režimu
make freeze   - Rodyti įdiegtas bibliotekas
make test     - Paleisti testus
make lint     - Paleisti ruff linterį
make format   - Automatiškai taisyti lint klaidas
make run      - Paleisti demo skriptą
```

## Struktūra

```
library/
├── __init__.py    # Eksportai
├── models.py      # Book, BookCopy, BookStatus
└── library.py     # Library klasė
tests/
├── test_models.py
└── test_library.py
main.py            # Demo skriptas
```
