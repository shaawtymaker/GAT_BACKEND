from app.crypto.search_index import build_search_index, build_query_mask

customer_name = "Rahul Verma"
query = "Akarsh" #the original input "Rahul"

index = build_search_index(customer_name)
query_mask = build_query_mask(query)

print("Customer index:", index)
print("Query mask:", query_mask)

# Basic overlap check
if index & query_mask == query_mask:
    print("MATCH")
else:
    print("NO MATCH")