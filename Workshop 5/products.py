products=[
    ["Mac book", 40000, "Apple",10],
    ["Zenbook", 20000, "Asus",20],
    ["Swift", 150000, "Acer",60],
]

while products:
    try:
        product = products.pop(0)
        print("Name:", product[0])
        print("Price:", product[1])
        print("Brand:", product[2])
        print("Stock:", product[3])
        print("-" * 20)
    except IndexError:
        print("Error: Missing data for product.")
    except Exception as e:
        print("Unexpected error:",e)
