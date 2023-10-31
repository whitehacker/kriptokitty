# KriptoKitty Crypto-Asset Exchange API
Welcome to the KriptoKitty Crypto-Asset Exchange API repository. This project serves as a significant contribution to the crypto exchange platform domain by providing a streamlined and efficient mechanism for managing crypto-asset withdrawals.

## Overview
In the rapidly evolving landscape of cryptocurrency exchanges, there's a constant need for reliable and efficient systems to manage asset deposits and withdrawals. Users typically deposit funds (like BTC) into an exchange, engage in trading activities (like swapping BTC for ETH), and, once they achieve their desired gains, they transfer their assets to an external wallet or another exchange.

KriptoKitty API offers a solution to this by introducing a simplified functionality for crypto-asset withdrawals. All interactions with the blockchain and crypto-asset transfers are channeled through our robust backend, ensuring the smooth processing of transactions.

## Simplified Withdrawal Flow:
* User Wallets: Every user has a distinct wallet on the exchange for each asset type. This wallet tracks the user's balance for that specific asset.
* Withdrawal Request: Users can initiate withdrawals, specifying the amount of a particular asset (e.g., ETH).
* Pre-condition Checks: The system verifies certain pre-conditions before processing the withdrawal.
* Blockchain Transaction: If all checks pass, the specified amount is deducted from the user's exchange wallet, and a blockchain transaction is set in motion.
* Transaction Status: Our system updates the transaction's status and logs additional data (like the blockchain transaction hash and network fees) once the transaction has been processed.

### Data Model 
![alt text](https://github.com/whitehacker/kriptokitty/blob/main/gx/db.png?raw=true)

## Run the Application
1. Create and activate a Python virtual environment
    - `python3 -m venv env` (depends what python version do you use and how are your local Python setup)
    - `source env/bin/activate`
2. Install requirements.txt file 
    - `pip install -r requirements.txt`
3. Install PostgreSQL or any other preferred RDBMS, in our case we have used Postgres
    1. `brew install postgresql` (macOS)
    2. `sudo apt install postgresql postgresql-contrib` (Linux - Ubuntu)
4. Open `main.py` and add your database credentials
    2. You should add your database credentials (PostgreSQL)
        - `engine = engine = create_engine('postgresql://username:password@localhost/database_name')`
5. Run the application
    - Open a new terminal and execute the below command:
        - `uvicorn main:app --reload`
6. View the Endpoints and utilize the API
    - Open a browser window and navigation to `127.0.0.1:8000/docs` (make sure you are accessing the right IP and port number)
