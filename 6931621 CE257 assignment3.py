#6931621
#Badu David
#List of cars and their prices
cars={"Toyota Yaris":28000,"Lexus NX":56000,"Land Cruiser":75000,"Mercedes Benz C300":48500, "Elantra":61000,
      "Subaru Impreza":19500,"Buick Encore":59000,"Kia Rio":17450,"Tesla Model S":72000,"Honda HR-V":65600,
      "Audi A5":75550,"Genesis G90":68700,"Volvo S90":45000,"Cadillac CT5":855600,"Porsche Cayman":76000,
      "Chevrolet Corvette":87500,"Cadillac CT4":69900," Infiniti Q50":69800,"Acura TLX":50900,"BMW X5":52400,
      "Range Rover Sport":75000,"Ford F-150":55900,"Toyota Tundra":36000,"Ram 1500":82000, "Rivian R1T":675250,
      "Chevrolet Colorado":45000," GMC Hummer EV Pickup":108000,"Nissan Titan":64000,"Honda Civic":24600, 
      "Jeep Gladiator":85100, "Hyundai Santa Cruz":35000,"Jaguar E-Pace":65000,"Mini Cooper":23200,"Camry":23000,
      "Kia Forte":19220,"Volkswagen Jetta":20632,"Honda Ridgeline":85500,"Lincoln Corsair":52500}
car_type=input("Enter a car_type:")
if car_type in cars:
    print("Yes")
    car_price=cars[car_type]
    print(f"Tthe price of {car_type}is${car_price}")
else:
    print(f"{car_type} is not available")

    