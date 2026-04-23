class Passenger:
    def __init__(self, name: str , destination: str):
        self._name = name
        self._destination = destination

class Transport:
    def __init__(self, speed: int):
        self._speed = speed

    def move(self, destination: str, distance: int):
        print(f" the road to {destination} took {distance / self._speed} hours")

class Bus(Transport):
    def __init__(self, passengers: list[Passenger], capacity: int, speed: int):
        super().__init__(speed)
        self._passengers = passengers
        self._capacity = capacity

    def board_passengers(self, passenger: Passenger):
        if len(self._passengers) + 1 <= self._capacity:
            self._passengers.append(passenger)
            return
        print("Can't board a passenger bus is full")

    def move(self, destination: str, distance: int):
        count = 0
        new = []

        for passenger in self._passengers:
            if passenger._destination == destination:
                print(f"Passenger {passenger._name} was taken to a desired destination")
                count += 1

            else:
                new.append(passenger)

        self._passengers = new

        print(f"In total {count} passengers left on this station")
        super().move(destination, distance)



