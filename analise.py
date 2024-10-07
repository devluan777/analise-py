import csv

def analisar_dados():
    with open('taxa-cdi.csv', mode='r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        taxas = [float(row['taxa']) for row in reader]

    media_taxa = sum(taxas) / len(taxas)
    print(f'Média da taxa CDI: {media_taxa:.2f}')

if __name__ == "__main__":
    analisar_dados()
