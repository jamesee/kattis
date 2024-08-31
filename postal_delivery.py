
from dataclasses import dataclass
import sys
from math import ceil

class Node:
    def __init__(self, data):
        self.location = data[0]
        self.mails_to_deliver = data[1]

    def __repr__(self):
        return f"({self.location}, {self.mails_to_deliver})"

@dataclass
class Truck:
    capacity:   int
    mails:      int = 0
    current_location:   int = 0
    dist_travelled: int = 0

    def return_to_postoffice(self):
        self.dist_travelled += abs(self.current_location)
        self.mails = self.capacity
        self.current_location = 0
        return
    
    def move_to_location(self, dest: Node):
        self.dist_travelled += abs(dest.location - self.current_location)
        self.current_location = dest.location
        if dest.mails_to_deliver > self.mails:
            while dest.mails_to_deliver > self.mails:
                self.dist_travelled += abs(dest.location) * 2
                dest.mails_to_deliver -= self.capacity
        self.mails -= dest.mails_to_deliver  
        dest.mails_to_deliver = 0
        if self.mails == 0:
            return self.return_to_postoffice()
        return

def validate_input(first_line: tuple[str, str]) -> bool:
    x = list(map(int, first_line))
    if x[0] >= 3 and x[0] <= 1_000 and x[1] >= 1 and x[1] <= 10_000:
        return True
    return sys.exit("Range Error: 3 <= N <= 1_000, 1<= K <= 10_000, N and K are integers.")


def validate_data(data: tuple[str, str]) -> bool:
    x = list(map(int, data))
    if x[0] >= -1_500 and x[0] <= 1_500 and x[1] >= 1 and x[1] <= 800:
        return True
    return sys.exit("Range Error: -1500 <= x <= 1500, 1 <= t <= 800, x and t are integers.")

def parse_inputs() -> tuple[int, list[int]]:
    first_line = input().strip().split()
    validate_input(first_line)
    #print(*map(int, first_line))
    num_of_locations, truck_capacity = map(int, first_line)

    locations: list[tuple[int, int]] = []
    for _ in range(num_of_locations):
        read_data = input().strip().split()
        validate_data(read_data)
        locations.append(tuple(map(int, read_data)))
    return truck_capacity, locations

# def test_truck() -> None:

#     postoffice = Node((0,0))
#     node1 = Node((-10, 50))
#     node2 = Node((10, 175))
#     node3 = Node((25, 20))

#     truck_capacity = 100
#     truck = Truck(capacity=truck_capacity, mails=truck_capacity)

#     truck.move_to_location(node3)
#     print(f"node3 : {node3}")
#     print(truck)

#     truck.move_to_location(node2)
#     print(f"node2 : {node2}")
#     print(truck)

#     if truck.current_location != 0:
#         truck.move_to_location(postoffice)
#     print(truck)

def read_inputs() -> tuple[Truck, list[tuple[int,int]], list[tuple[int,int]]]:
    truck_capacity, locations = parse_inputs()
    truck = Truck(capacity=truck_capacity, mails=truck_capacity)
    
    positive_locations = list()
    for x in sorted([x for x in locations if x[0]>0]):
        positive_locations.append(x)
    
    negative_locations = list()
    for x in sorted([x for x in locations if x[0]<0], reverse=True):
        negative_locations.append(x)

    return truck, negative_locations, positive_locations

def simulation(truck: Truck, locations: list[list[int,int]]) -> None:
    postoffice = Node((0,0))
    while len(locations):
        truck.move_to_location(Node(locations.pop()))
    if truck.current_location != 0:
        truck.return_to_postoffice()
    return

def main() -> None:
   
    truck, negative_locations, positive_locations = read_inputs()

    simulation(truck, positive_locations)
    simulation(truck, negative_locations)

    print(truck.dist_travelled)

if __name__ == "__main__":
    main()


