from faker import Faker
from datetime import timedelta

def create_trip():
    PickupDateTime = faker.date_time_this_year()
    tripdurration = timedelta(
        days=0, 
        seconds=faker.random_int(0,60),
        microseconds = faker.random_int(0,1000000),
        milliseconds = faker.random_int(0,1000),
        minutes = faker.random_int(0,90),
        hours = 0,
        weeks = 0
    )
    DropOffDateTime = PickupDateTime+tripdurration
    passengerCount = faker.random_int(0,3)
    tripDistance = faker.random_int(0,15) + faker.random_int(0,100)/100
    puLocationId = faker.random_int(0,1000)
    doLocationId = faker.random_int(0,1000)
    fareAmount = round(tripDistance * (faker.random_int(0,2)+faker.random_int(0,100)/100),2)
    puYear = PickupDateTime.year
    puMonth = PickupDateTime.month

    trip = {
        'PickupDateTime':str(PickupDateTime),
        'DropOffDateTime':str(DropOffDateTime),
        'passengerCount':passengerCount,
        'tripDistance':tripDistance,
        'puLocationId':puLocationId,
        'doLocationId':doLocationId,
        'fareAmount':fareAmount,
        'puYear':puYear,
        'puMonth':puMonth
    }
    return trip
