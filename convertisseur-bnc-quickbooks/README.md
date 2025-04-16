# COnvertisseur de RElevé BAncaire BNC pour QUickBooks

Ce petit utilitaire vous permet de convertir un relevé bancaire BNC exporté en Excel (depuis un PDF via Acrobat Pro) en un fichier CSV compatible avec QuickBooks.

## 🧰 Fonctionnalités

- Interface graphique simple (Gooey)
- Import d’un fichier `.xlsx` converti depuis un relevé PDF
- Export automatique d’un fichier `.csv` prêt à l'importation
- Attribution GNU GPL v3

## 📝 Utilisation

1. Exporte ton relevé PDF en Excel (format tableau) via Acrobat Pro
2. Lance l'application
3. Sélectionne le fichier `.xlsx`
4. Clique sur `Start` — le fichier `.csv` est généré automatiquement

## 📦 Dépendances

```bash
pip install pandas gooey openpyxl
```

## 🔐 Licence

Ce programme est un logiciel libre : vous pouvez le redistribuer et/ou le modifier
selon les termes de la Licence Publique Générale GNU publiée par la Free Software Foundation, soit la version 3 de la licence, soit (à votre choix) toute version ultérieure.

© 2025 Rémi Maglione
