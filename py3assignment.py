import pickle
import csv


def create_hospitals_list():
    hospitals = []

    while True:
        hospital_name = input("Enter hospital name (or 'q' to quit): ")
        if hospital_name == 'q':
            break

        address = input("Enter hospital address: ")

        hospital = {'hospital_name': hospital_name, 'address': address}
        hospitals.append(hospital)

    return hospitals


def write_to_pickle(hospitals, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(hospitals, file)
    print("Data written to pickle file successfully!")


def read_from_pickle(file_name):
    with open(file_name, 'rb') as file:
        hospitals = pickle.load(file)
    return hospitals


def write_to_csv(hospitals, file_name):
    keys = hospitals[0].keys()

    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(hospitals)

    print("Data written to CSV file successfully!")


# Read hospital details from console and create a list of dictionaries
hospitals_list = create_hospitals_list()

# Write the list to a pickle file
pickle_file = 'hospitals.pickle'
write_to_pickle(hospitals_list, pickle_file)

# Read the list from the pickle file
read_hospitals = read_from_pickle(pickle_file)

# Write the list to a CSV file
csv_file = 'hospitals.csv'
write_to_csv(read_hospitals, csv_file)
