import random
import os

def clear_screen():
    # สำหรับ Linux หรือ macOS
    if os.name == 'posix':
        os.system('clear')
    # สำหรับ Windows
    elif os.name == 'nt':
        os.system('cls')

def select_language():
    clear_screen()  # เคลียร์หน้าจอ
    print("Please select a language / กรุณาเลือกภาษา:")
    print("1 = English")
    print("2 = ไทย")
    
    language_choice = input("Enter the language number / กรอกหมายเลขภาษาที่ต้องการ: ")
    if language_choice not in ["1", "2"]:
        #clear_screen()  # เคลียร์หน้าจออีกครั้ง
        print(f"\nInvalid choice! / เลือกไม่ถูกต้อง!")
        return select_language()
    return language_choice


def game():
    language = select_language()

    if language == "1":
        print(f"\nWelcome to the game")
        username = input("Username: ")
        #password = input("Password: ")
        print(f"\n{username}, let's play the game together!")
    else:
        print(f"\nยินดีต้อนรับเข้าสู่เกม")
        username = input("ชื่อผู้ใช้: ")
        #password = input("รหัสผ่าน: ")
        print(f"\n{username} มาเล่นเกมกันเถอะ!")

    player_score = 0
    bot_score = 0
    
    # Choices dictionary separated by language
    choices_en = {
        "1": "rock", "2": "paper", "3": "scissors",
        "rock": "rock", "paper": "paper", "scissors": "scissors"
    }

    choices_th = {
        "1": "ค้อน", "2": "กระดาษ", "3": "กรรไกร",
        "ค้อน": "rock", "กระดาษ": "paper", "กรรไกร": "scissors"
    }

    # เลือก dictionary ตามภาษาที่ผู้เล่นเลือก
    choices = choices_en if language == "1" else choices_th
    hands = ["rock", "paper", "scissors"] if language == "1" else ["ค้อน", "กระดาษ", "กรรไกร"]

    while True:
        # ถ้าผู้เล่นเลือกภาษาอังกฤษ
        if language == "1":
            player_select = input("Please select your choice (1 = rock🔨 , 2 = paper📄 , 3 = scissors✂️   or 0 = stop): ").lower()
        else:
            player_select = input("กรุณาเลือก (1 = ค้อน🔨 , 2 = กระดาษ📄 , 3 = กรรไกร✂️   หรือ 0 = หยุด): ").lower()

        # ตรวจสอบว่าผู้เล่นเลือก stop หรือ หยุด โดยการใส่ 0
        if player_select in ["0", "stop", "หยุด"]:
            break
        
        # ตรวจสอบว่าผู้เล่นเลือกตัวเลือกที่ถูกต้องหรือไม่
        if player_select in choices:
            player_select = choices[player_select]
            random_hands = random.randint(0, 2)
            bot_select = hands[random_hands]

            if language == "1":
                print(f"You selected: {player_select} | Bot selected: {bot_select}")
            else:
                print(f"คุณเลือก: {player_select} | บอทเลือก: {bot_select}")
            
            # Draw
            if player_select == bot_select:
                result_text = "It's a draw!" if language == "1" else "ผล: เสมอกัน!"
            
            # Rock
            elif (player_select == "rock" and bot_select == "scissors") or \
                 (player_select == "ค้อน" and bot_select == "กรรไกร"):
                player_score += 1
                result_text = "You won!" if language == "1" else "คุณชนะ!"
            
            # Paper
            elif (player_select == "paper" and bot_select == "rock") or \
                 (player_select == "กระดาษ" and bot_select == "ค้อน"):
                player_score += 1
                result_text = "You won!" if language == "1" else "คุณชนะ!"
            
            # Scissors
            elif (player_select == "scissors" and bot_select == "paper") or \
                 (player_select == "กรรไกร" and bot_select == "กระดาษ"):
                player_score += 1
                result_text = "You won!" if language == "1" else "คุณชนะ!"
            
            # Bot wins
            else:
                bot_score += 1
                result_text = "You lost!" if language == "1" else "คุณแพ้!"
            
            if language == "1":
                print(f"Result: {result_text}")
                print(f"Score: Player {player_score} vs Bot {bot_score}")
                print("=============================================================")
            else:
                print(f"ผล: {result_text}")
                print(f"คะแนน: ผู้เล่น {player_score} vs บอท {bot_score}")
                print("=============================================================")
        
        # ถ้าเลือกไม่ถูกต้อง
        else:
            if language == "1":
                print("Invalid input, please try again!")
                print("=============================================================")
            else:
                print("กรอกไม่ถูกต้อง กรุณาลองอีกครั้ง!")
                print("=============================================================")
        
    # Game summary
    print(f"\n************************************************************************")
    if language == "1":
        print(f"Final Score: Player {player_score} : Bot {bot_score}")
        if player_score > bot_score:
            print("You are the winner! 🥳")
        elif player_score < bot_score:
            print("You lost! 😫")
        else:
            print("It's a draw! 🤗")
        print(f"\nGame stopped!")
    else:
        print(f"คะแนนรวม: ผู้เล่น {player_score} : บอท {bot_score}")
        if player_score > bot_score:
            print("คุณเป็นผู้ชนะ! 🥳")
        elif player_score < bot_score:
            print("คุณแพ้! 😫")
        else:
            print("เสมอกัน! 🤗")
        print(f"\nจบเกม!")

# Start the game
game()
