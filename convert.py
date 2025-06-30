import random
import time
import sys

roasts = [
    "Bro... did you just forget BASIC math? Go touch grass.",
    "You're about as useful as a screen door on a submarine.",
    "Congrats. You just disappointed every register in the CPU.",
    "This is why GDB breaks on YOU.",
    "Lol MG",
    "Garis Jhakne",
    "Makadosk even bot do better then u MF",
    "Assembly xoddye mug",
    "K exploit Dev banxas mug yesari",
    "I've seen malware do better conversions, lmao.",
    "Was that a fat-finger, or are you just built broken?",
    "MG. Even NULL pointers aren't this empty.",
    "Did the carry bit fall out of your brain?",
    "You just got stack smashed by your own stupidity.",
    "Bruh. Even shellcode cries watching this.",
    "Your ALU just committed suicide.",
    "The CPU scheduler downgraded you to background noise.",
    "Even segfaults make more sense than that answer.",
    "Assembler just rage quit your existence.",
    "Endian shift left your brain out the window.",
    "That endian flip was harder than your answer.",
]

def get_roast():
    return random.choice(roasts)

def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nQuit like a bitch. See ya.")
        sys.exit()

def dec_to_hex(n):
    return hex(n)

def dec_to_bin(n):
    return bin(n)

def hex_to_dec(h):
    return str(int(h, 16))

def hex_to_bin(h):
    return bin(int(h, 16))

def bin_to_dec(b):
    return str(int(b, 2))

def bin_to_hex(b):
    return hex(int(b, 2))

def ascii_to_alpha(code_str):
    # code_str = space separated decimal ASCII codes
    try:
        chars = [chr(int(c)) for c in code_str.strip().split()]
        return ''.join(chars)
    except:
        return None

def alpha_to_ascii(s):
    return ' '.join(str(ord(c)) for c in s)

def is_valid_bin(s):
    return all(c in '01' for c in s)

def is_valid_hex(s):
    if s.startswith('0x'):
        s = s[2:]
    try:
        int(s, 16)
        return True
    except:
        return False

def is_valid_dec(s):
    try:
        int(s)
        return True
    except:
        return False

def generate_question(conv_type):
    number = random.randint(0, 255)
    if conv_type == "dec_to_hex":
        return f"DECIMAL → HEX :: [{number}]", dec_to_hex(number)
    elif conv_type == "dec_to_bin":
        return f"DECIMAL → BINARY :: [{number}]", dec_to_bin(number)
    elif conv_type == "hex_to_dec":
        h = hex(number)
        return f"HEX → DECIMAL :: [{h}]", hex_to_dec(h)
    elif conv_type == "hex_to_bin":
        h = hex(number)
        return f"HEX → BINARY :: [{h}]", hex_to_bin(h)
    elif conv_type == "bin_to_dec":
        b = bin(number)
        return f"BINARY → DECIMAL :: [{b}]", bin_to_dec(b)
    elif conv_type == "bin_to_hex":
        b = bin(number)
        return f"BINARY → HEX :: [{b}]", bin_to_hex(b)
    elif conv_type == "ascii_to_alpha":
        # random ASCII decimal codes, space separated
        length = random.randint(3, 7)
        codes = [str(random.randint(32, 126)) for _ in range(length)]
        code_str = ' '.join(codes)
        alpha = ascii_to_alpha(code_str)
        return f"ASCII DECIMAL CODES → ALPHABET :: [{code_str}]", alpha
    elif conv_type == "alpha_to_ascii":
        # random string from printable ascii chars
        length = random.randint(3, 7)
        s = ''.join(chr(random.randint(32,126)) for _ in range(length))
        ascii_codes = alpha_to_ascii(s)
        return f"ALPHABET → ASCII DECIMAL CODES :: [{s}]", ascii_codes
    else:
        return None, None

def validate_answer(conv_type, user, correct):
    user = user.strip()
    correct = correct.strip()
    if conv_type in ["dec_to_hex", "bin_to_hex", "hex_to_bin"]:
        # normalize hex to lowercase with 0x
        user = user.lower()
        if not user.startswith("0x"):
            return False
        # validate hex string content
        if not is_valid_hex(user):
            return False
        return user == correct.lower()
    elif conv_type in ["dec_to_bin", "hex_to_bin"]:
        # normalize bin to lowercase with 0b
        user = user.lower()
        if not user.startswith("0b"):
            return False
        if not is_valid_bin(user[2:]):
            return False
        return user == correct.lower()
    elif conv_type in ["hex_to_dec", "bin_to_dec"]:
        if not is_valid_dec(user):
            return False
        return user == correct
    elif conv_type == "ascii_to_alpha":
        # user input is string, compare directly
        return user == correct
    elif conv_type == "alpha_to_ascii":
        # user input is space separated decimals
        try:
            user_codes = user.split()
            correct_codes = correct.split()
            if len(user_codes) != len(correct_codes):
                return False
            for uc, cc in zip(user_codes, correct_codes):
                if int(uc) != int(cc):
                    return False
            return True
        except:
            return False
    else:
        return False

def print_menu():
    print("""
🩸 ========================= 🩸
    ASCII ↔ ALPHABET & BASE WAR
🩸 ========================= 🩸

💣 Rules:
- No mercy.
- Choose your poison.
- Get it right, keep the streak.
- Fail, and I'll roast you harder than your CPU under prime95.

CTRL+C to bail like a coward.

Pick conversion type:
 1. dec_to_hex
 2. dec_to_bin
 3. hex_to_dec
 4. hex_to_bin
 5. bin_to_dec
 6. bin_to_hex
 7. ascii_to_alpha
 8. alpha_to_ascii
 9. Switch mode / Quit
""")

def main():
    streak = 0
    total = 0
    wrong_answers = {}
    while True:
        print_menu()
        choice = safe_input("→ Your choice (number): ").strip()
        if choice == '9':
            print("Peace out, warrior.")
            break
        choices_map = {
            '1': "dec_to_hex",
            '2': "dec_to_bin",
            '3': "hex_to_dec",
            '4': "hex_to_bin",
            '5': "bin_to_dec",
            '6': "bin_to_hex",
            '7': "ascii_to_alpha",
            '8': "alpha_to_ascii",
        }
        conv_type = choices_map.get(choice)
        if not conv_type:
            print("Invalid choice, dipshit. Try again.")
            continue

        print(f"\nLocking into mode: {conv_type}. Crush it. CTRL+C to bail.\n")
        try:
            while True:
                prompt, correct = generate_question(conv_type)
                if prompt is None:
                    print("Broken conversion type, aborting.")
                    break
                print(f"🔥 Convert {prompt}")
                user = safe_input("→ Your answer: ").strip()
                if not validate_answer(conv_type, user, correct):
                    streak = 0
                    total += 1
                    wrong_answers[conv_type] = wrong_answers.get(conv_type, 0) + 1
                    print(f"❌ WRONG. Correct answer → {correct}")
                    print(f"💀 {get_roast()}")
                else:
                    streak += 1
                    total += 1
                    print(f"✔️ Correct, beast. Streak: {streak} | Total: {total}\n")
        except KeyboardInterrupt:
            print("\nMode exited. Back to menu.\n")
            continue

if __name__ == "__main__":
    main()
