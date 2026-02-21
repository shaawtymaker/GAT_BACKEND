from app.services.crypto_service import encrypt_and_index, decrypt_customer, build_search_query

customer = {
    "name": "Rahul Verma",
    "account_number": "ACC123456",
    "account_type": "Savings",
    "branch_code": "BLR01"
}

encrypted, index = encrypt_and_index(customer)
print("Encrypted:", encrypted)
print("Index:", index)

query_mask = build_search_query("Rahul")

print("Match:", index & query_mask == query_mask)

decrypted = decrypt_customer(encrypted)
print("Decrypted:", decrypted)