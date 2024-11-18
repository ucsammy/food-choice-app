#things to do on a date
#can also be for if you are not in a relationship    
import random
choices = [
    'burgers', 
    'mexican', 
    'chinese', 
    'pizza'
 ] 
boba_spots_vacaville = [
    "Peace Love & Boba",
    "RareTea Vacaville",
    "Tea Dojo Cafe",
    "B&B Boba & Banh Mi",
    "Milk Tea Lab"
]
burger_spots_vacaville = [
    "Falafel & Gyro",
    "Burger City",
    "In-N-Out Burger",
    "Habit Burger & Grill",
    "Shula’s Kitchen 707",
    "University of Beer - Vacaville",
    "Nation's Giant Hamburgers & Great Pies",
    "Buckhorn BBQ + Grill",
    "Fosters Freeze",
    "Five Guys"
]
mexican_spots_vacaville = [
    "Los Reyes Restaurante Y Cantina",
    "Murillo's Mexican Food",
    "Vasquez Delicatessen",
    "Pelayo's Mexican Food",
    "Tacos Jalisco",
    "Villa Corona",
    "Taqueria El Tejaban",
    "El Azteca Mexican Food",
    "Burrito Palace Restaurant",
    "Favela's Taqueria"
]
chinese_spots_vacaville = [
    "Tasty Every Hour Chinese Restaurant",
    "AA Chinese Fast Food",
    "Wah Shine",
    "88 BaoBao Dumpling House",
    "Stir Fry Chinese Food",
    "Stir Fry Express",
    "China House",
    "Chef Chen's Chinese Restaurant",
    "Dragon Palace",
    "Kings Buffet"
]
pizza_spots_vacaville = [
    "Napoli Pizzeria Vacaville",
    "Amici's East Coast Pizzeria",
    "Pietro's No. 2",
    "Pieology Pizzeria Vacaville",
    "Round Table Pizza",
    "Mountain Mike's Pizza",
    "Mary's Pizza Shack",
    "Cenario's Pizza",
    "BJ's Restaurant & Brewhouse",
    "Pizza Twist"
]
italian_spots_vacaville = [
     "Fuso Italian Restaurant",
    "Pietro's No. 1",
    "Pietro's No. 2",
    "La Borgata Italian Deli",
    "Napoli Pizzeria",
    "Amici's East Coast Pizzeria",
    "Olive Garden Italian Restaurant",
    "Mary's Pizza Shack",
    "Cenario's Pizza",
    "Round Table Pizza"
]


print("Categories of food we have is: Boba, Burgers, Mexican, Chinese, Pizza, Italian")
user_input = input("What category of food do you want? ").lower()

# Use match-case to print the places based on the category
match user_input:
    case "boba":
        print("Here is your first boba spot!: ", random.choice(boba_spots_vacaville))
    case "burgers":
        print("Here is your first burger spot!: ", random.choice(burger_spots_vacaville))
    case "mexican":
        print("Here is your first mexican spot!: ", random.choice(mexican_spots_vacaville))
    case "chinese":
        print("Here is your first chinese spot!: ", random.choice(chinese_spots_vacaville))
    case "pizza":
        print("Here is your first pizza spot!: ", random.choice(pizza_spots_vacaville))
    case "italian":
        print("Here is your first italian spot!: ", random.choice(italian_spots_vacaville))
    case _ :
        print("try again")


   
