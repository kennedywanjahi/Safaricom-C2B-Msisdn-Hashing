# Safaricom-C2B-Msisdn-Hashing
A python Script to assist in creating records of your existing Customer MSISDN after Safaricom Migration to Data Minimization on the C2B Notifications.
Please note that this is for existing records only.
You will need to add extra logic for Hashed MSIDNs records during customer addition or sign up.

# Why you might need this
In Line with Kenya's Data Protection ACT of 2019, Safaricom Communicated 
    "
    Safaricom will be minimizing the level of detail that our partners receive when a customer makes a payment on M-Pesa. 
    These changes will affect C2B API:
    Accessed via Payment aggregator/Broker
    Accessed via Daraja 
    "

    What this Means:
        Old Standard format 254xxxxxxxxx No Longer applies
        New Format The hashed phone number will be a SHA-256 hash of 64 characters length Alphanumeric
        e.g "
            the MSISDN 254705912645 translates to  
            94c392c311d522da950619227b3361752a42042db7e1e699b26e628305c68a88
        "
    Hence if you have an existing record of all your customers numbers you will need to generate hashes for them.

# Set Up
This Script will work for a SQL based database with the base script configured to work with a MySQL database

For a different data base you will need to set up for the provider.

1. You wil need python installed on your machine(VM, EC2, Personal Machine or your machine of execution)
2. Create and activate a python virtual environment
3. Install Requirements in requirements in requirements.txt file
4. Add your database configuration on the Config Section.
5. This Project assumes you add a column next to your msisdn colum named ===>>> msisdn_hash
6. Based on your database structure modify select and insert queries
7. Execute your python script 
8. Wait for records to update
    

 

