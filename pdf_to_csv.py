
import tabula

pdf_file = "/mnt/c/Users/LENOVO/Downloads/apr22.pdf"
dfs = tabula.read_pdf(pdf_file,
                 pages = "all",
                 stream = True,
                 guess = True,
                 multiple_tables = True
        )


for i, df in enumerate(dfs):
    df.to_csv(f"table_{i}.csv", index=False)
    print(f"Saved Table table_{i}.csv")

