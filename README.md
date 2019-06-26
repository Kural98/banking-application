Banking-System
A look and feel of banking system. In which a person can open account,deposit,withdrawal,transfer and many more banking tasks.

Indroduction:
In this project our aim is give a look and feel of a banking system. In this user can open account either of saving, current,fixed deposit account. User can deposit,widthdraw or transer money and user can see also see their bank statement.
Loan option is also available and many more.For details see the (banking_diagram.png) in the directory.

Compilation:
This project is maded using python 3.5 and Oracle database. In python we are using cx_Oracle library for database connection.

Working:

This project first connect a user form Oracle database.Then user will signup some customers and according to need we can perform various banking related tasks see (banking_diagram.png).

Detailed Banking System:

The Bank provides following services:

A customer can have either of the following type of accounts:

Savings Account – Generally used for temporary savings. Offers interest at the rate of 7.5% per annum on your savings. 

Maximum 10 withdrawals are allowed per month. No minimum balance is needed to open or maintain this account.

Current Account – Generally used by corporates and business men. No interest is offered on this account. No limit of on no. of withdrawals. A customer needs to have minimum 5K to open or maintain this account.

A customer can do following transactions:

Deposit and withdraw money in his account/s

Transfer money to other accounts

Print his account statement for given range of dates

Customers can open a Fixed Deposit (FD) account with the bank

FD Account number is auto-generated by the bank on opening of a new FD.

Customer can deposit money to FD account and can specify the term or duration of the FD.

A Customer can have more than one FD accounts as well. FD account no.s will be linked to the customer-id.

Minimum FD balance is Rs.1000 and min deposit term is 12 months.

Customers can avail Loan from the bank:

Loan Account Number is auto generated on disbursal of a new loan.

Customer can specify the loan amount and the repayment term

A Customer can avail more than one loan from the bank. Loan account no. will be linked to the customer-id via savings account of that customer. Maximum Loan Amount eligible = 2 * balance in Savings account at the time of availing the loan.

Bank wants to maintain history of closed accounts i.e. which accounts have been closed on which dates. Bank admin can see this history.

Every customer has a customer-id and password to access his account.

When a new customer registers himself with the bank, a customer-id is auto generated by the bank and given to him.
Password needs to be set by the customer. It should be minimum 8 characters and can be any combination of numeric and alphabets.

Allow maximum 3 consecutive re-trials for unsuccessful login attempts.

Bank keeps following information of all customers to send regular updates

First and Last Name of customer

Address has following fields - Address Line 1, Line 2, City, State, Pincode. Pincode should be a 6 digit numeric and rest of the fields are strings.

Account no./s – Account no. is auto-generated by the bank on opening of a new account and is same as customer id.

Transactions (withdrawals & deposits) done by the customers on respective accounts

The admin should be able to extract reports on FD accounts in the bank

The admin should be able to extract reports on loans disbursed from the bank
