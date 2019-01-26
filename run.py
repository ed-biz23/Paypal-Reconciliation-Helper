import csv
import time

def main(reconciliationCSV, annualStatmentCSV):
    try:
        ## Get all the transaction ids from Reconciliation ##
        with open(reconciliationCSV, 'r', encoding="utf8") as csv_file:
            csv_reader = csv.DictReader(x.replace('\0', '') for x in csv_file)
            reconciliation_transactionsID = set(line['Transaction ID'] for line in csv_reader)

        ## Retrieve the data from the yearly statment ##
        with open(annualStatmentCSV, 'r', encoding="utf8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

        ## Creates new csv with updated Paypal Reconciliation data ##
            with open(f'new_1099K_Reconciliation_{int(time.time())}.csv', 'w') as new_file:
                fieldnames = ['Date', 'Transaction ID', 'Payer Email ID', 'Received Amount',
                              'Received Currency', 'Fee and Cost', 'Status']

                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
                csv_writer.writeheader()
                statement_transactionsID = set()
                for line in csv_reader:
                    # print(line['\ufeff"Date"'])
                    if line['Transaction ID'] in reconciliation_transactionsID and line['Status'] == 'Completed':
                        statement_transactionsID.add(line['Transaction ID'])
                        csv_writer.writerow({'Date': line['\ufeff"Date"'],
                                             'Transaction ID': line['Transaction ID'],
                                             'Payer Email ID': line['From Email Address'],
                                             'Received Amount': line['Gross'],
                                             'Received Currency': line['Currency'],
                                             'Fee and Cost': line['Fee'],
                                             'Status': line['Status']})
                    elif line['Type'] == 'Payment Refund' and float(line['Gross']) < 0:
                        csv_writer.writerow({'Date': line['\ufeff"Date"'],
                                             'Transaction ID': line['Transaction ID'],
                                             'Payer Email ID': line['To Email Address'],
                                             'Received Amount': line['Gross'],
                                             'Received Currency': line['Currency'],
                                             'Fee and Cost': line['Fee'],
                                             'Status': 'Refunded'})

                print('Transaction(s) that needs to be entered manually.')
                for transaction in reconciliation_transactionsID ^ statement_transactionsID:
                    print('Transaction Id:', transaction)
    except Exception as E:
        exit(E)

if __name__ == '__main__':
    print('Before you begin, please make sure both Reconciliation and Annual Paypal Statement in same directory '
          'or folder as this script\n')

    reconciliationCSV = str(input('Please enter the name of the reconciliation file including the extension ".csv": ')).strip()
    print()
    annualStatmentCSV = str(input('Please enter the name of the Annual Statment file including the extension ".csv": ')).strip()
    print()
    main(reconciliationCSV, annualStatmentCSV)
    time.sleep(3600)