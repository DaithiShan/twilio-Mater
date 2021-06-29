import csv

phones = []

with open('sms_client/participants.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # We don't want first line of bad data
    next(csv_data)

    for line in csv_data:
        phones.append(f"{line['Phone']}")
