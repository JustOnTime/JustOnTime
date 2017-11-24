import csv
import mailchimp3
import json
import os

def main():

    with open('.mailchimp.json') as json_data_file:
        data = json.load(json_data_file)

    with open(data['csv_file'], 'rb') as csvfile:
        connections = csv.DictReader(csvfile)
        for connection in connections:

            list_id = data['list_id']
            client = mailchimp3.MailChimp(data['user'],data['secret'])

            try:

                client.lists.members.create(list_id, {
                'email_address': connection['Email Address'],
                'status': 'subscribed',
                'merge_fields': {
                    'FNAME': connection['First Name'],
                    'LNAME': connection['Last Name']
                }})
                print(connection['First Name'], connection['Last Name'], connection['Email Address'])

            except Exception as e:
                pass

    os.remove(data['csv_file'])

    return

if __name__ == "__main__":
    main()
