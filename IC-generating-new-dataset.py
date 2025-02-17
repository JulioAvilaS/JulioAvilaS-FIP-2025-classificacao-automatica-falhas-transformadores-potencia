import random
import csv

def generate_gas_values_for_case(case):
    if case == 'PD': 
        return {'C2H2': 0, 'C2H4': random.uniform(1, 10), 'CH4': random.uniform(0, 0.09), 'H2': random.uniform(1, 10), 'C2H6': random.uniform(0, 0.19)}
    elif case == 'D1':  
        return {'C2H2': random.uniform(1, 10), 'C2H4': random.uniform(0.1, 1), 'CH4': random.uniform(0.1, 0.5), 'H2': random.uniform(1, 10), 'C2H6': random.uniform(1, 10)}
    elif case == 'D2':  
        return {'C2H2': random.uniform(0.6, 2.5), 'C2H4': random.uniform(1, 10), 'CH4': random.uniform(0.1, 1), 'H2': random.uniform(1, 10), 'C2H6': random.uniform(2, 10)}
    elif case == 'T1':  
        return {'C2H2': 0, 'C2H4': random.uniform(1, 10), 'CH4': random.uniform(1.01, 10), 'H2': random.uniform(1, 10), 'C2H6': random.uniform(0, 0.99)}
    elif case == 'T2':  
        return {'C2H2': random.uniform(0, 0.09), 'C2H4': random.uniform(1, 10), 'CH4': random.uniform(1.01, 10), 'H2': random.uniform(1, 10), 'C2H6': random.uniform(1, 4)}
    elif case == 'T3': 
        return {'C2H2': random.uniform(0, 0.19), 'C2H4': random.uniform(1, 10), 'CH4': random.uniform(1.01, 10), 'H2': random.uniform(1, 10), 'C2H6': random.uniform(4.01, 10)}

def calculate_ratios(gases):
    ratios = {
        'C2H2/C2H4': gases['C2H2'] / gases['C2H4'] if gases['C2H4'] != 0 else float('inf'),
        'CH4/H2': gases['CH4'] / gases['H2'] if gases['H2'] != 0 else float('inf'),
        'C2H4/C2H6': gases['C2H4'] / gases['C2H6'] if gases['C2H6'] != 0 else float('inf'),
    }
    return ratios

def write_to_csv(results, filename="gas_faults.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Caso", "C2H2", "C2H4", "CH4", "H2", "C2H6", "C2H2/C2H4", "CH4/H2", "C2H4/C2H6"])
        for case, gases, ratios in results:
            writer.writerow([
                case,
                f"{gases['C2H2']:.2f}",
                f"{gases['C2H4']:.2f}",
                f"{gases['CH4']:.2f}",
                f"{gases['H2']:.2f}",
                f"{gases['C2H6']:.2f}",
                f"{ratios['C2H2/C2H4']:.2f}",
                f"{ratios['CH4/H2']:.2f}",
                f"{ratios['C2H4/C2H6']:.2f}"
            ])

def main():
    print("Defina a quantidade de casos a serem gerados para cada tipo de falha:")
    cases_count = {
        'PD': int(input("Quantidade de casos PD: ")),  
        'D1': int(input("Quantidade de casos D1: ")),  
        'D2': int(input("Quantidade de casos D2: ")), 
        'T1': int(input("Quantidade de casos T1: ")),  
        'T2': int(input("Quantidade de casos T2: ")), 
        'T3': int(input("Quantidade de casos T3: "))  
    }

    results = []

    for case, count in cases_count.items():
        for _ in range(count):
            gases = generate_gas_values_for_case(case)
            ratios = calculate_ratios(gases)
            results.append((case, gases, ratios))

    write_to_csv(results)
    print("\nResultados foram salvos no arquivo 'gas_faults.csv'.")

if __name__ == "__main__":
    main()
