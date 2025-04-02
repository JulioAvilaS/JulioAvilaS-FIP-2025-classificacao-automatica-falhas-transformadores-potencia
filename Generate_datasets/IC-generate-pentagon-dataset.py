import csv
import random
from enum import Enum
import sys
import os

project_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_file)

from Pentagon_stages.s1_calculate_percentage import calculate_relative_gas_percentage
from Pentagon_stages.s2_calculate_verticis import Gas, GasPercentage, calculate_polygon_vertices_coords
from Pentagon_stages.s3_calculate_centroid_area import calcuate_polygon_area, calculate_polygon_centroid_coords
from Pentagon_stages.s4_calculate_region import calculate_all_centroid_positions_per_line, calculate_pentagon_region, Coordinates


class Failure(Enum):
    PD = "PD"
    D1 = "D1"
    D2 = "D2"
    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    NF = "NF"

def inicialize_failures():
    return {failure: 0 for failure in Failure}

gas_quantities = {
    Gas.C2H2: 0.001,
    Gas.H2: 0.001,
    Gas.C2H6: 0.001,
    Gas.CH4: 0.001,
    Gas.C2H4: 0.001,
}
    

samples = []
labels = []

db_size = 13993

i = 0

number_of_failures = db_size//7 + 3

failure_counters = inicialize_failures()

def exponencial(min, max, lambda_valor):
    while True:
        numero = random.expovariate(lambda_valor)
        if(min <= numero <= max):
            return numero

def midle(min, max, lambda_valor):
    case = random.randint(0, 150)
    if case == 0:
        return random.uniform(min, max)    
    else:
        return exponencial(min, max, lambda_valor)


def randomizer(decimal_places=3):
    min = 0.001
    max = 10000
    lambda_valor = 0.1

    return {
        Gas.C2H2: round(midle(min, max, lambda_valor), decimal_places),
        Gas.H2: round(midle(min, max, lambda_valor), decimal_places),
        Gas.C2H6: round(midle(min, max, lambda_valor), decimal_places),
        Gas.CH4: round(midle(min, max, lambda_valor), decimal_places),
        Gas.C2H4: round(midle(min, max, lambda_valor), decimal_places)
    }

def is_notfail():
    return(gas_quantities[Gas.H2] < (100*1.1) and gas_quantities[Gas.CH4] < (120*1.1) and
        gas_quantities[Gas.C2H6] < (65*1.1) and gas_quantities[Gas.C2H4] < (50*1.1) and
        gas_quantities[Gas.C2H2] < (1*1.1))


def calculate_all_gas_percentage():
    gas_percentages = []
    gases_sum = sum(gas_quantities.values())
    for value in gas_quantities.values():
        gas_percentages.append(calculate_relative_gas_percentage(value, gases_sum))
    return gas_percentages

def calculate_all_coordinates(gas_percentages):
    coordinates_list = []
    gases = [Gas.C2H2, Gas.H2, Gas.C2H6, Gas.CH4, Gas.C2H4]
    for gas, percentage in zip(gases, gas_percentages):
        coordinates_list.append(calculate_polygon_vertices_coords(gas, percentage))
    return coordinates_list

def write_labels(filename, result_labels):
    with open(filename, mode='w', newline='') as file:
        csv_labels = csv.writer(file)
        csv_labels.writerow(["act"])
        for label in result_labels:
            csv_labels.writerow([label])


out_range_gases_count = 0
while(i < db_size):
    gas_values = randomizer()
    gas_quantities.update(gas_values)  

    if is_notfail() and failure_counters[Failure.NF] < number_of_failures:
      i += 1 
      failure_counters[Failure.NF] +=1
      
      samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4],
      gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4],
      gas_quantities[Gas.C2H6]))
      
      labels.append(1) # NF

    else:
      gas_percentages = calculate_all_gas_percentage()

      if any(value > 40 for value in gas_percentages):
         out_range_gases_count += 1

    #   while any(value > 40 for value in gas_percentages) or is_notfail():
    #     gas_values = randomizer()
    #     gas_quantities.update(gas_values) 
    #     gas_percentages = calculate_all_gas_percentage()

      coordinates_list = calculate_all_coordinates(gas_percentages)

      polygon_area = calcuate_polygon_area(coordinates_list)

      centroid_coords = calculate_polygon_centroid_coords(coordinates_list, polygon_area)

      centroid_positions_per_line = calculate_all_centroid_positions_per_line(centroid_coords)

      pentagon_region = calculate_pentagon_region(centroid_coords, centroid_positions_per_line)    

      if(pentagon_region.name == Failure.PD.name and failure_counters[Failure.PD] < number_of_failures):
        print(f"Falha PD {gas_percentages} em {i}")
        i += 1
        failure_counters[Failure.PD] +=1
        samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4], gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4], gas_quantities[Gas.C2H6]))
        labels.append(2)  # PD
            
      elif(pentagon_region.name == Failure.D1.name and failure_counters[Failure.D1] < number_of_failures):
        i += 1
        failure_counters[Failure.D1] +=1
        samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4], gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4], gas_quantities[Gas.C2H6]))
        labels.append(3)  # D1

      elif(pentagon_region.name == Failure.D2.name and failure_counters[Failure.D2] < number_of_failures):
        i += 1
        failure_counters[Failure.D2] +=1
        samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4], gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4], gas_quantities[Gas.C2H6]))
        labels.append(4)  # D2

      elif(pentagon_region.name == Failure.T1.name and failure_counters[Failure.T1] < number_of_failures):
        i += 1
        failure_counters[Failure.T1] +=1
        samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4], gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4], gas_quantities[Gas.C2H6]))
        labels.append(5)  # T1

      elif(pentagon_region.name == Failure.T2.name and failure_counters[Failure.T2] < number_of_failures):
        i += 1
        failure_counters[Failure.T2] +=1
        samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4], gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4], gas_quantities[Gas.C2H6]))
        labels.append(6)  # T2

      elif(pentagon_region.name == Failure.T3.name and failure_counters[Failure.T3] < number_of_failures):
        i += 1
        failure_counters[Failure.T3] +=1
        samples.append((gas_quantities[Gas.H2], gas_quantities[Gas.CH4], gas_quantities[Gas.C2H2], gas_quantities[Gas.C2H4], gas_quantities[Gas.C2H6]))
        labels.append(7)  # T3

filename = "C:/ProjetosIC/JulioAvilaS-FIP-2025-classificacao-automatica-falhas-transformadores-potencia/Datasets/2.0-dataset/train_samples.csv"

db_840_min_max_samples = [
   [92600.0,10200.0,0.001,2.0,1.0],
   [0.0,18900.0,330.0,540.0,410.0],
   [8800.0,64064.0,0.001,95650.0,72128.0],
   [5.26,0.001,66.4,28.2,0.001],
   [10092.0,5399.0,37565.0,6500.0,530.0],
   [3417.62,131.42,0.0,1.22,14.36],
   [134.0,13.0,0.001,0.001,267.0],
   [7020.0,1850.0,4410.0,2960.0,0.0]
]
db_840_min_max_labels = [2,5,7,3,3,2,2,4]

db_ibrahim_min_max_samples = [
   [92600.0,10200.0,0.001,0.001,0.001],
   [0.001,0.001,35.0,5.0,10.0],
   [8800.0,64064.0,0.001,95650.0,72128.0],
   [20000.0,13000.0,57000.0,29000.0,1850.0],
   [625.0,130.0,0.0001,2.0,47.0],
   [0.001,116.0,0.001,0.001,70.0],
   [0.001,3.4,0.001,54.0,0.001]
]
db_ibrahim_min_max_labels = [2,4,7,4,5,5,7]


with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["h2","ch4","c2h2","c2h4","c2h6"])
    for row in db_ibrahim_min_max_samples:
       writer.writerow(row)

    for sample in samples:
        writer.writerow(sample)


filename = "C:/ProjetosIC/JulioAvilaS-FIP-2025-classificacao-automatica-falhas-transformadores-potencia/Datasets/2.0-dataset/train_labels.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['act'])
    for row in db_ibrahim_min_max_labels:
       writer.writerow([row])

    for label in labels:
        writer.writerow([label])

print(f"{out_range_gases_count} gases com mais de 40%")
print("Dataset criado com sucesso.")