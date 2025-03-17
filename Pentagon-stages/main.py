import csv
from s1_calculate_percentage import calculate_relative_gas_percentage
from s2_calculate_verticis import Gas, GasPercentage, calculate_polygon_vertices_coords
from s3_calculate_centroid_area import calcuate_polygon_area, calculate_polygon_centroid_coords
from s4_calculate_region import calculate_all_centroid_positions_per_line, calculate_pentagon_region, Coordinates

gas_quantities = {
    Gas.C2H2: 0.001,
    Gas.H2: 0.001,
    Gas.C2H6: 0.001,
    Gas.CH4: 0.001,
    Gas.C2H4: 0.001,
}

def read_samples(filename):
    samples_list = []
    with open(filename, mode='r') as file:
        gas_samples_csv = csv.reader(file)
        next(gas_samples_csv)
        for row in gas_samples_csv:
            samples_list.append(row)
    return samples_list

def get_gases_list(index, list):
    gases_list = []
    for gas in list[index]:
        gases_list.append(float(gas))
    return gases_list

def set_gas_quantities(gases_list): # A ordem dos gases no arquivo está diferente da do programa. Por isso a mudança no índices.
   gas_quantities[Gas.C2H2] = gases_list[2]
   gas_quantities[Gas.H2] = gases_list[0]
   gas_quantities[Gas.C2H6] = gases_list[4]
   gas_quantities[Gas.CH4] = gases_list[1]
   gas_quantities[Gas.C2H4] = gases_list[3]

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


samples_list = read_samples("840-test-dataset/test_samples.csv")
i = 1
result_labels = []

for i in range(len(samples_list) - 1):
    gases_list = get_gases_list(i, samples_list)

    set_gas_quantities(gases_list)

    gas_percentages = calculate_all_gas_percentage()

    coordinates_list = calculate_all_coordinates(gas_percentages)

    polygon_area = calcuate_polygon_area(coordinates_list)

    centroid_coords = calculate_polygon_centroid_coords(coordinates_list, polygon_area)

    centroid_positions_per_line = calculate_all_centroid_positions_per_line(centroid_coords)

    pentagon_region = calculate_pentagon_region(centroid_coords, centroid_positions_per_line)    

    result_labels.append(pentagon_region.value)

    i+=1
    
write_labels("Duval-pentagon-labels/840-database-labels.csv", result_labels)









