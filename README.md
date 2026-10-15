# Banking & Digital Wallet System

A menu-driven banking program written in Python using object-oriented programming. It uses only the standard library.

## Features
- Create basic, savings and checking accounts
- Deposit, withdraw and transfer money
- View a statement of all transactions
- Custom errors for invalid amounts, insufficient funds, missing or duplicate accounts and invalid transfers

## Project structure
- exceptions.py: custom error classes
- transaction.py: the Transaction class
- accounts.py: Account, SavingsAccount and CheckingAccount
- bank.py: the Bank class that manages all accounts
- main.py: the menu-driven program

## OOP concepts used
Classes and objects, inheritance, method overriding, encapsulation, properties, composition and custom exceptions.

## How to run
Install Python 3, then run this in the project folder:

    python main.py