class Character:
    def __init__(self, initial_points=10):
        # 初始化角色的属性和初始点数
        self.attributes = {
            "Strength": 0,
            "Agility": 0,
            "Intelligence": 0,
            "Stamina": 0
        }
        self.available_points = initial_points

    def display_status(self):
        # 显示当前的属性和剩余点数
        print("\nCurrent Status:")
        for attr, value in self.attributes.items():
            print(f"{attr}: {value}")
        print(f"Available Points: {self.available_points}\n")

    def add_points(self, attribute, points):
        # 分配点数到指定属性
        if attribute not in self.attributes:
            print("Invalid attribute. Please choose a valid attribute.")
            return
        if points <= 0:
            print("Points must be positive.")
            return
        if points > self.available_points:
            print("Not enough available points.")
            return

        self.attributes[attribute] += points
        self.available_points -= points
        print(f"Added {points} points to {attribute}.")

    def run(self):
        # 主循环，允许用户进行加点操作
        print("Welcome to the Attribute Point Allocation System!")
        self.display_status()

        while self.available_points > 0:
            print("Choose an attribute to add points to (Strength, Agility, Intelligence, Stamina)")
            attribute = input("Enter attribute name: ").capitalize()
            try:
                points = int(input("Enter points to add: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            self.add_points(attribute, points)
            self.display_status()

        print("All points allocated. Final status:")
        self.display_status()

# 示例运行
character = Character(initial_points=10)
character.run()
