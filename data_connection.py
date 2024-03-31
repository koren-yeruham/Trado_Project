
import pymongo
from bson import ObjectId


username = "qa_agency"
password = "!5szveK7$TE$93u"
database_name = "trado_qa"


def main():
    client = create_mongo_connection(username, password, database_name)
    db = create_mongo_db(client, 'trado_qa')
    connection_c(db)
    display_collections(db)

    # Main menu
    while True:
        print("\n--- Main Menu ---")
        print("1. Display sample documents")
        print("2. Display all documents in a collection")
        print("3. Get specific key-value")
        print("4. Count key-value pairs")
        print("5. Get distinct key values")
        print("6. Get loginCode")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            collection = input("Please enter collection name: ")
            display_samples(db, collection)
        elif choice == "2":
            collection_name = input("Enter collection name: ")
            display_all_documents_in_a_collection(db, collection_name)
        elif choice == "3":
            collection_name = input("Enter collection name: ")
            document_id = input("Enter document ID: ")
            key = input("Enter key: ")
            value = get_specific_key_value(db, collection_name, document_id, key)
            print(f"The {key} for document with ID '{document_id}' is: {value}")
        elif choice == "4":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            value = input("Enter value: ")
            count = count_key_value(db, collection_name, key, value)
            print(f"There are {count} documents with '{key}': '{value}'.")
        elif choice == "5":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            distinct_values = get_distinct_key_values(db, collection_name, key)
            print(f"The distinct {key} values in {collection_name} are:")
            for i in distinct_values:
                print(i)
        elif choice == "6":
            phone1 = input("Please enter the user's phone number: ")
            loginCode = get_loginCode(db, phone1)
            print(f"The code is {loginCode}")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


# Function to create MongoDB connection
def create_mongo_connection(user_name, encoded_password, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        "mongodb+srv://qa_agency:!5szveK7$TE$93u@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority"
    )

    return client


def close_connection(client):
    client.close()


# first we access create_mongo_connection(user_name, encoded_password, db_name) and return client object
# then we send the client object to create_mongo_db(client, db_name) and return db object to be used in the code
def create_mongo_db(client, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    db = client[db_name]
    return db


# Function to test the MongoDB connection
def connection_c(db):
    try:
        db.command("ping")
        print("Connected to MongoDB.")
    except Exception as e:
        print("Error connecting to MongoDB:", e)


# Function to get a list of collection names in the given database
def get_collections(db):
    collections = db.list_collection_names()
    return collections


# Function to display collection names in the given database
def display_collections(db):
    collections = db.list_collection_names()
    for collection in collections:
        print(f"Collection name: {collection}")


# Function to display document count and an example document for each collection in the given database
def display_samples(db, collection):
    collections = get_collections(db)
    for i in collections:
        if i == "adminusers":
            sample_collection = db[collection]
            document_count = sample_collection.count_documents({})
            print(f"There are {document_count} documents in the {i} collection.")
            print(f"Example data set: {sample_collection.find_one()}")


# Function to display all documents in a given collection
def display_all_documents_in_a_collection(db, collection_name):
    collection = db[collection_name]
    documents = collection.find()
    for document in documents:
        print(document)


# Function to get the value of a specific key in a document identified by its ID in a given collection
def get_specific_key_value(db, collection_name, document_id, key):
    collection = db[collection_name]
    document = collection.find_one({"_id": ObjectId(document_id)})
    if document:
        value = document.get(key)
        return value
    else:
        return None


def get_loginCode(db, phone):
    collection = db["adminusers"]
    document = collection.find_one({"phone": phone})
    if document:
        value = document.get("loginCode", "NoValue")
        print(value)
        return value
    else:
        return None


# Function to count the documents with a specific key-value pair in a given collection
def count_key_value(db, collection_name, key, value):
    collection = db[collection_name]
    count = collection.count_documents({key: value})
    return count


# Function to get the distinct values of a specific key in a given collection
def get_distinct_key_values(db, collection_name, key):
    collection = db[collection_name]
    distinct_values = collection.distinct(key)
    return distinct_values


# Function to test the stock status of products in the 'products' collection
# def test_product_stock(db):
#     products = db["products"]
#     out_of_stock_products = products.count_documents({"productStock": 0})
#     print(f"There are {out_of_stock_products} out-of-stock products.")
#
#
# # Function to test the order status in the 'orders' collection
# def test_orders(db):
#     orders = db["orders"]
#     pending_orders = orders.count_documents({"status": "ready"})
    # print(f"There are {pending_orders} ready orders.")


if __name__ == "__main__":
    main()

