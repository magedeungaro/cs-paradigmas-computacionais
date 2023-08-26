from oop_vehicle import Vehicle

class Bus(Vehicle):
    pass

def main():
    school_bus = Bus('School Bus', 100, 8)
    print(school_bus)

if __name__ == "__main__":
    main()