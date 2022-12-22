import pandas as pd
import re

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi():

    # Read the Excel file
    df = pd.read_excel('./Excel/01_Baden-Württemberg_2017-2018_20210630_ch_sp.xlsx')

    allowed_formats = [
        r"^\d+(\.\d+)?$",  # Integer or integer with decimal places
        r"^k\.A\.$",  # k.A.
        r"^\d+\,\d+$",  # 13,00
        r"^A1$",  # A1
        r"^A2$",  # A2
        r"^A3$",  # A3
        r"^D2$",  # D2
        r"^A4$",  # A4
        r"^B2$",  # B2
        r"^D3$",  # D3
        r"^C1$",  # C1
        r"^B4$",  # B4
        r"^C4$",  # C4
        r"^B3$",  # B3
        r"^D1$",  # D1
    ]

    df = df.iloc[13:, 7:]

    for i, row in df.iterrows():
        for j, value in row.items():
            # Check if the value is in an invalid format
            if not any(bool(re.match(pattern, str(value))) for pattern in allowed_formats):
                print(f"Found invalid value in row {i + 1}, column {j}: {value}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
