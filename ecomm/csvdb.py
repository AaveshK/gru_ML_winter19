with open(data.csv) as f:
        reader = csv.reader(f)
        for row in reader:
            	created = Product.objects.get_or_create(
                name=row[0],
                price=row[1],
                )
