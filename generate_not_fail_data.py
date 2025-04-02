import csv
import random

MIN_ALL_GASES_LIMIT = 0.00001

H2_MAX_LIMIT = 100
CH4_MAX_LIMIT = 120
C2H6_MAX_LIMIT = 65
C2H4_MAX_LIMIT = 50
C2H2_MAX_LIMIT = 1

MIN_ERROR_MARGIN_PERCENTAGE = 5
MAX_EROR_MARGIN_PERCENTAGE = 10

ROUND_VALUE = 2

def generate_concentrations():
    margin_error = random.uniform(MIN_ERROR_MARGIN_PERCENTAGE, MAX_EROR_MARGIN_PERCENTAGE)

    gases = {
        "H2": round(random.uniform(MIN_ALL_GASES_LIMIT, H2_MAX_LIMIT * (1 + margin_error / 100)), ROUND_VALUE),
        "CH4" : round(random.uniform(MIN_ALL_GASES_LIMIT, CH4_MAX_LIMIT * (1 +margin_error / 100)), ROUND_VALUE),
        "C2H6" : round(random.uniform(MIN_ALL_GASES_LIMIT, C2H6_MAX_LIMIT * (1 + margin_error / 100)), ROUND_VALUE),
        "C2H4" : round(random.uniform(MIN_ALL_GASES_LIMIT, C2H4_MAX_LIMIT * (1 + margin_error / 100)), ROUND_VALUE),
        "C2H2" : round(random.uniform(MIN_ALL_GASES_LIMIT, C2H2_MAX_LIMIT * (1 + margin_error / 100)), ROUND_VALUE)
    }

    return gases


def generate_not_fail_csv_data(lines: int):
    header = ["h2", "ch4", "c2h2", "c2h4", "c2h6"]

    with open("Datasets/Ibrahim-444-dataset/not_fail.csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(header)
        
        for _ in range(lines):
            gases_data = generate_concentrations()

            writer.writerow([
                gases_data["H2"],
                gases_data["CH4"],
                gases_data["C2H2"],
                gases_data["C2H4"],
                gases_data["C2H6"]
            ])

if __name__ == "__main__":
    generate_not_fail_csv_data(74)
