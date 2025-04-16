
from gooey import Gooey, GooeyParser
import pandas as pd
import os

# ------------------------------------------------------------------------------
# Convertisseur Relevé Bancaire BNC pour QuickBooks
# Copyright (C) 2025 Rémi Maglione
#
# Ce programme est un logiciel libre : vous pouvez le redistribuer et/ou le modifier
# selon les termes de la Licence Publique Générale GNU publiée par la Free Software Foundation,
# soit la version 3 de la licence, soit (à votre choix) toute version ultérieure.
#
# Ce programme est distribué dans l'espoir qu'il sera utile,
# mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de
# QUALITÉ MARCHANDE ou d'ADÉQUATION À UN USAGE PARTICULIER.
# Voir la Licence Publique Générale GNU pour plus de détails.
#
# Vous devriez avoir reçu une copie de la Licence Publique Générale GNU
# avec ce programme. Si ce n'est pas le cas, consultez <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

@Gooey(
    program_name="Convertisseur Relevé Bancaire BNC pour QuickBooks",
    language='french',
    default_size=(700, 600),
    advanced=True,
    tabbed_groups=False
)
def main():
    parser = GooeyParser(description="Convertir un relevé bancaire BNC en CSV compatible Quickbooks")

    #Groupe principal
    main_group = parser.add_argument_group("Relevé à convertir (format .xlsx)")
    main_group.add_argument(
        "fichier_excel",
        widget="FileChooser",
        help="Note: le fichier Excel peut être obetenu depuis le relevé pdf par une conversion avec Acrobat Pro"
    )
    
    # Groupe renommé "À propos" avec un champ stylisé
    about_group = parser.add_argument_group("À propos")
    about_group.add_argument(
        "© 2025 Rémi Maglione",
        help="GNU GPL v3",
        default="https://www.gnu.org/licenses/gpl-3.0.html",
        widget="TextField"
    )

    args = parser.parse_args()
    input_path = args.fichier_excel
    output_path = os.path.splitext(input_path)[0] + "_quickbooks.csv"

    df_excel = pd.read_excel(input_path, sheet_name=0, skiprows=5)

    df_clean = df_excel.rename(columns={
        df_excel.columns[0]: "MM",
        df_excel.columns[1]: "JJ",
        df_excel.columns[2]: "DESCRIPTION",
        df_excel.columns[7]: "DEBIT",
        df_excel.columns[9]: "CREDIT",
        df_excel.columns[10]: "SOLDE"
    })

    df_clean = df_clean[df_clean["MM"].apply(lambda x: str(x).isdigit())]

    df_clean["MM"] = df_clean["MM"].astype(float).astype(int).astype(str).str.zfill(2)
    df_clean["JJ"] = df_clean["JJ"].astype(float).astype(int).astype(str).str.zfill(2)

    df_clean["Date"] = pd.to_datetime(
        "2024-" + df_clean["MM"] + "-" + df_clean["JJ"],
        format="%Y-%m-%d"
    ).dt.strftime("%d/%m/%Y")

    df_clean["Amount"] = df_clean.apply(
        lambda row: -row["DEBIT"] if pd.notnull(row["DEBIT"]) else row["CREDIT"], axis=1
    )

    df_clean = df_clean[df_clean["DESCRIPTION"].str.upper().str.strip() != "SOLDE PRECEDENT"]

    df_output = df_clean[["Date", "DESCRIPTION", "Amount"]].rename(columns={"DESCRIPTION": "Description"})

    df_output.to_csv(output_path, index=False, encoding='utf-8-sig')

    print(f"✅ Conversion réussie ! Fichier exporté : {output_path}")

if __name__ == "__main__":
    main()
