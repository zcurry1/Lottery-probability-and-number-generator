import random
import math  #used for probability calculation
import logging #track user choices and helps debug log errors

class LotteryFactory:
    @staticmethod
    def generate_numbers(start, end, count):
        try: #generate list of random numbers within specific range
            numbers = random.sample(range(start, end + 1), count)
            numbers.sort()
            return numbers
        except ValueError as e:
            logging.error("Error generating numbers: e")
            return [] 
            #logs error of numbers requested outside of size range
    

    @staticmethod
    def generate_multiple_sets(times, start, end, count):
        return [LotteryFactory.generate_numbers(start, end, count) for _ in range(times)]
#adding prob generator- i still am working on whether i can bring in past numbers or not
@staticmethod
    def mega_millions_probability():
        main_numbers_combinations = math.comb(70, 5)
        mega_ball_combinations = math.comb(25, 1)
        total_combinations = main_numbers_combinations * mega_ball_combinations
        probability = 1 / total_combinations
        return probability





def display_menu():
    print('\n\nSelect an option:\n')
    print('1. Georgia Cash 3')
    print('2. Georgia Cash 4')
    print('3. Georgia Fantasy 5')
    print('4. Georgia Powerball')
    print('5. Georgia Mega Millions')
    print('Q. Quit')

def process_choice(choice):
    if choice == '1':
        print('\nGeorgia Cash 3:', LotteryFactory.generate_multiple_sets(3, 0, 9, 3))
    elif choice == '2':
        print('\nGeorgia Cash 4:', LotteryFactory.generate_multiple_sets(3, 0, 9, 4))
    elif choice == '3':
        print('\nGeorgia Fantasy 5:', LotteryFactory.generate_multiple_sets(1, 1, 42, 5))
    elif choice == '4':
        print('\nGeorgia Powerball:', LotteryFactory.generate_numbers(1, 69, 5), LotteryFactory.generate_numbers(1, 26, 1))
    elif choice == '5':
        print('\nGeorgia Mega Millions:', LotteryFactory.generate_numbers(1, 70, 5), LotteryFactory.generate_numbers(1, 25, 1))
        print('Probability of winning the Mega Millions jackpot:', LotteryFactory.mega_millions_probability()) #enhance output when they choose number 5
    else:
        print('Invalid choice. Please select a valid option.') # added an else clause for invalid inputs
def worker_function():
    while True:
        display_menu()
        choice = input('\nEnter your choice: ').lower()

        if choice.startswith('q'):
            print("Done! Thanks for playing.")
            break
        else:
            process_choice(choice)

if __name__ == '__main__':
    worker_function()
