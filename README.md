# Paypal-Reconciliation-Helper
Simple script to help you with fees and refund of the sales transaction.

# Requirement
Requires Python 3.6 and +

# What it does?
This script will help you to get the transaction fees and also sales refund that correlates with your transaction ids in Paypal Reconciliation Data and output new csv file including those fees and refund, which is useful for tax deduction.

# How to
Please make sure you include your Paypal Reconciliation Data and Paypal annual statement in same folder as this script.
Follow the on screen instructions to execute this script successfully.

# PS
Please make sure your Paypal Reconciliation has `Transaction ID` header in the csv file and your Paypal annual statement has the following headers: 
`Date, Transaction ID, From Email Address, Gross, Currency, Fee, Status, To Email Address`.
Also, it will print out the transaction id number if it was unable to retrieve data.

*It has only been tested with 2018 Tax year.*
