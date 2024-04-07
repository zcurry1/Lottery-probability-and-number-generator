import random

class LotteryFactory:
    @staticmethod
    def generate_numbers(start, end, count):
        numbers = random.sample(range(start, end + 1), count)
        numbers.sort()
        return numbers

    @staticmethod
    def generate_multiple_sets(times, start, end, count):
        return [LotteryFactory.generate_numbers(start, end, count) for _ in range(times)]

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
