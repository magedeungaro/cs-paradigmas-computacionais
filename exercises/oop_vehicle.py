class Vehicle:
    def __init__(self, model, max_velocity, km_per_liter):
        self.model = model
        self.max_velocity = max_velocity
        self.km_per_liter = km_per_liter
    
    def __str__(self):
        return f"Model: {self.model} - Max vel.: {self.max_velocity} km/h - Eficiency: {self.km_per_liter} km/l"
    

def main():
    fusca = Vehicle('Fusca', 120, 12)
    print(fusca)

if __name__ == "__main__":
    main()