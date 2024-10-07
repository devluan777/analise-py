import csv
import matplotlib.pyplot as plt

def visualizar_dados():
    datas = []
    taxas = []

    with open('taxa-cdi.csv', mode='r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datas.append(row['data'])
            taxas.append(float(row['taxa']))

    plt.plot(datas, taxas, marker='o')
    plt.xlabel('Data')
    plt.ylabel('Taxa CDI')
    plt.title('Taxa CDI ao longo do tempo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualizar_dados()
