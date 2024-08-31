
from typing import Optional, tuple, List
from dataclasses import dataclass
import sys

class Node:
    def __init__(self, data):
        self.location = data[0]
        self.mails_to_deliver = data[1]
        self.next = None

    def __repr__(self):
        return f"({self.location}, {self.mails_to_deliver})"

class LocationsLinkedList:
    def __init__(self, data: tuple[int, int]):
        self.head: Node = Node(data)
    
    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_furthest_node_with_mails(self) -> Node:
        current = self.head
        while current.next and current.next.mails_to_deliver:
            current = current.next
        return  current 

    def display(self) -> None:
        current = self.head
        while current:
            if current.next is None:
                print((current.location, current.mails_to_deliver))
            else:
                print((current.location, current.mails_to_deliver), end=" -> ")
            current = current.next


@dataclass
class Truck:
    capacity:   int
    mails:      int = 0
    current_location:   int = 0
    dist_travelled: int = 0

    def return_to_postoffice(self):
        self.move_to_location(Node((0,0)))
        self.mails = self.capacity
        return

    def unload_mails(self, dest: Node):
        if dest.mails_to_deliver > self.mails:
            dest.mails_to_deliver -= self.mails
            return self.return_to_postoffice()
        else:
            self.mails -= dest.mails_to_deliver
            dest.mails_to_deliver = 0
        return

    def move_to_location(self, dest: Node):
        if dest.location == 0:
            self.mails = self.capacity
        self.dist_travelled += abs(dest.location - self.current_location)
        self.current_location = dest.location
        return self.unload_mails(dest)

def validate_input(first_line: tuple[str, str]) -> bool:
    x = list(map(int, first_line))
    if x[0] >= 3 and x[0] <= 1_000 and x[1] >= 1 and x[1] <= 10_000:
        return True
    else:
        return False

def validate_data(data: tuple[str, str]) -> bool:
    x = list(map(int, data))
    if x[0] >= -1_500 and x[0] <= 1_500 and x[1] >= 1 and x[1] <= 800:
        return True
    else:
        return False

def parse_inputs() -> tuple[int, list[int]]:
    first_line = input().strip().split()
    if not validate_input(first_line):
        sys.exit(1)
    #print(*map(int, first_line))
    num_of_locations, truck_capacity = map(int, first_line)

    locations: list[tuple[int, int]] = []
    for _ in range(num_of_locations):
        read_data = input().strip().split()
        if validate_data(read_data):
            locations.append(tuple(map(int, read_data)))
    return truck_capacity, locations

def test_truck() -> None:

    postoffice = Node((0,0))
    node1 = Node((-10, 50))
    node2 = Node((10, 175))
    node3 = Node((25, 20))

    truck_capacity = 100
    truck = Truck(capacity=truck_capacity, mails=truck_capacity)

    truck.move_to_location(node2)
    print(f"node2 : {node2}")
    print(truck)

    truck.move_to_location(node2)
    print(f"node2 : {node2}")
    print(truck)

def test_linkedlist() -> None:

    ll = LocationsLinkedList()
    
    ll.append((-100, 20))
    ll.append((100, 50))
    ll.append((10, 30))
    
    ll.display()

def generate_linked_lists() -> tuple[Truck, LocationsLinkedList, LocationsLinkedList]:
    truck_capacity, locations = parse_inputs()
    truck = Truck(capacity=truck_capacity, mails=truck_capacity)
    
    positive_locations_ll = LocationsLinkedList((0,0))
    for x in sorted([x for x in locations if x[0]>0]):
        positive_locations_ll.append(x)
    
    negative_locations_ll = LocationsLinkedList((0,0))
    for x in sorted([x for x in locations if x[0]<0], reverse=True):
        negative_locations_ll.append(x)

    return truck, negative_locations_ll, positive_locations_ll

def simulation(truck, ll: LocationsLinkedList) -> Truck:
    while True:
        furthest_node = ll.find_furthest_node_with_mails()
        truck.move_to_location(furthest_node)
        if furthest_node.location == 0:
            break
    return truck

def main() -> None:
   
    truck, negative_locations_ll, positive_locations_ll = generate_linked_lists()

#    print("-"*30, "[output]")
#    negative_locations_ll.display()
#    positive_locations_ll.display()
#    print(truck)
#   

    truck = simulation(truck, negative_locations_ll)
    truck = simulation(truck, positive_locations_ll)
    
#    print("-"*30, "[result]")
#    negative_locations_ll.display()
#    print(truck)
#    positive_locations_ll.display()
#    print(truck)

    print(truck.dist_travelled)

if __name__ == "__main__":
    main()

    # debug
    #test_linkedlist()
    #test_truck()

