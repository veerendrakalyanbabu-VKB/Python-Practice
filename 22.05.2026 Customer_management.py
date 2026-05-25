customers = [
    {
        "name": "Veerendra Kalyan Babu",
        "city": "Hyderabad",
        "email": "Veerendra.kalyanbabu@gmail.com",
        "addresses": [
            {
                "door_no": "110",
                "street": "MG Road",
                "pincode": "521201"
            },
            {
                "door_no": "112",
                "street": "Temple Street",
                "pincode": "521202"
            }
        ]
    },

    {
        "name": "Ganesh",
        "city": "Vijayawada",
        "email": "ganesh@gmail.com",
        "addresses": [
            {
                "door_no": "5-12",
                "street": "Benz Circle",
                "pincode": "520010"
            }
        ]
    },

    {
        "name": "Harish",
        "city": "Hyderabad",
        "email": "harish@gmail.com", 
        "addresses": [
            {
                "door_no": "7-55",
                "street": "Ameerpet",
                "pincode": "500016"
            },
            {
                "door_no": "8-66",
                "street": "KPHB",
                "pincode": "500072"
            }
        ]
    }
]

# Printing customer details

for customer in customers:

    print("Customer Details")
    print("Name:", customer["name"])
    print("City:", customer["city"])
    print("Email:", customer["email"])

    print("Addresses:")

    for address in customer["addresses"]:
        print(
            address["door_no"],
            address["street"],
            address["pincode"]
        )

    print("----------------------------")