from app.crypto.encryption import encrypt_record, decrypt_record

sample = {
    "name": "Rahul Verma",
    "account_number": "ACC123456",
    "account_type": "Savings",
    "branch_code": "BLR01"
}

encrypted = encrypt_record(sample)
print("Encrypted:", encrypted)

decrypted = decrypt_record(encrypted)
print("Decrypted:", decrypted)  