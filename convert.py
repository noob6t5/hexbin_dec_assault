import random
import time
import sys

# Roasts, shuffled for no repeats until exhaustion
roast_pool = []
roasts = [
    "Bro... did you just forget BASIC math? Go touch grass.",
    "You're about as useful as a screen door on a submarine.",
    "Congrats. You just disappointed every register in the CPU.",
    "This is why GDB breaks on YOU.",
    "Lol MG",
    "Garis Jhakne",
    "Makadosk even bot do better then u MF",
    "Assembly xoddye mug",
    "K exploit Dev banxas mug yesari"
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

conversion_types = [
    "dec_to_hex",
    "dec_to_bin",
    "hex_to_dec",
    "hex_to_bin",
    "bin_to_dec",
    "bin_to_hex"
]

wrong_answers = {}
start_time = time.time()
streak = 0
total = 0

def get_roast():
    global roast_pool
    if not roast_pool:
        roast_pool = random.sample(roasts, len(roasts))
    return roast_pool.pop()

# Conversion functions
def dec_to_hex(n):
    return hex(n)

def dec_to_bin(n):
    return bin(n)

def hex_to_dec(h):
    return int(h, 16)

def hex_to_bin(h):
    return bin(int(h, 16))

def bin_to_dec(b):
    return int(b, 2)

def bin_to_hex(b):
    return hex(int(b, 2))

# Endian flip helpers
def flip_endian(hexstr, chunk_size_bytes):
    """
    Flip endianness of hex string.
    hexstr: string like '0x1234abcd'
    chunk_size_bytes: 2 (16bit), 3 (24bit), 4 (32bit)
    """
    # Clean hex (strip 0x)
    h = hexstr[2:] if hexstr.startswith('0x') else hexstr
    # Pad if necessary (must be even length)
    if len(h) % 2 != 0:
        h = '0' + h

    # Split into bytes
    bytes_list = [h[i:i+2] for i in range(0, len(h), 2)]

    # Ensure total bytes is divisible by chunk size
    if len(bytes_list) % chunk_size_bytes != 0:
        # pad at start with 00 bytes (big endian style)
        pad_len = chunk_size_bytes - (len(bytes_list) % chunk_size_bytes)
        bytes_list = ['00'] * pad_len + bytes_list

    # Flip bytes in each chunk
    flipped_chunks = []
    for i in range(0, len(bytes_list), chunk_size_bytes):
        chunk = bytes_list[i:i+chunk_size_bytes]
        flipped_chunks += chunk[::-1]

    flipped_hex = ''.join(flipped_chunks).lstrip('0')
    if flipped_hex == '':
        flipped_hex = '0'

    return '0x' + flipped_hex

def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\nCowardice detected. Exiting.")
        sys.exit()
    except KeyboardInterrupt:
        print("\nQuit like a bitch. See ya.")
        sys.exit()

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

def ask_conversion_question():
    global streak, total
    ctype = random.choice(conversion_types)
    number = random.randint(0, 255)

    prompt = ""
    correct = ""
    user = ""

    if ctype == "dec_to_hex":
        prompt = f"DECIMAL → HEX :: [{number}]"
        correct = dec_to_hex(number)
        print(f"\n🔥 Convert {prompt}")
        user = safe_input("→ HEX (with 0x): ").strip().lower()
        if not is_valid_hex(user):
            print("❌ Invalid HEX input.")
            return False

    elif ctype == "dec_to_bin":
        prompt = f"DECIMAL → BINARY :: [{number}]"
        correct = dec_to_bin(number)
        print(f"\n🔥 Convert {prompt}")
        user = safe_input("→ BINARY (with 0b): ").strip().lower()
        if not (user.startswith('0b') and is_valid_bin(user[2:])):
            print("❌ Invalid BINARY input.")
            return False

    elif ctype == "hex_to_dec":
        h = hex(number)
        prompt = f"HEX → DECIMAL :: [{h}]"
        correct = str(hex_to_dec(h))
        print(f"\n🔥 Convert {prompt}")
        user = safe_input("→ DECIMAL: ").strip()
        if not is_valid_dec(user):
            print("❌ Invalid DECIMAL input.")
            return False

    elif ctype == "hex_to_bin":
        h = hex(number)
        prompt = f"HEX → BINARY :: [{h}]"
        correct = hex_to_bin(h)
        print(f"\n🔥 Convert {prompt}")
        user = safe_input("→ BINARY (with 0b): ").strip().lower()
        if not (user.startswith('0b') and is_valid_bin(user[2:])):
            print("❌ Invalid BINARY input.")
            return False

    elif ctype == "bin_to_dec":
        b = bin(number)
        prompt = f"BINARY → DECIMAL :: [{b}]"
        correct = str(bin_to_dec(b))
        print(f"\n🔥 Convert {prompt}")
        user = safe_input("→ DECIMAL: ").strip()
        if not is_valid_dec(user):
            print("❌ Invalid DECIMAL input.")
            return False

    elif ctype == "bin_to_hex":
        b = bin(number)
        prompt = f"BINARY → HEX :: [{b}]"
        correct = bin_to_hex(b)
        print(f"\n🔥 Convert {prompt}")
        user = safe_input("→ HEX (with 0x): ").strip().lower()
        if not is_valid_hex(user):
            print("❌ Invalid HEX input.")
            return False

    else:
        print("WTF... Unknown conversion type.")
        return False

    if user == correct:
        streak += 1
        total += 1
        print(f"✔️ Correct, beast. Streak: {streak} | Total: {total}")
        return True
    else:
        streak = 0
        total += 1
        print(f"❌ WRONG. Correct answer → {correct}")
        print(f"💀 {get_roast()}")
        wrong_answers[ctype] = wrong_answers.get(ctype, 0) + 1
        return False


def ask_endian_question():
    global streak, total
    # Choose a random hex number of 1 to 4 bytes (8-32 bits)
    length_bytes = random.choice([2,3,4])
    max_val = (1 << (length_bytes * 8)) -1
    number = random.randint(0, max_val)

    hexnum = hex(number)
    # User must flip endian of this hex num
    prompt = f"FLIP ENDIANESS ({length_bytes*8} bits) :: [{hexnum}]"
    print(f"\n🔥 Convert {prompt}")

    correct = flip_endian(hexnum, length_bytes)
    user = safe_input("→ Your flipped HEX (with 0x): ").strip().lower()
    if not is_valid_hex(user):
        print("❌ Invalid HEX input.")
        return False

    if user == correct:
        streak += 1
        total += 1
        print(f"✔️ Correct, endian warrior. Streak: {streak} | Total: {total}")
        return True
    else:
        streak = 0
        total += 1
        print(f"❌ WRONG. Correct answer → {correct}")
        print(f"💀 {get_roast()}")
        wrong_answers["endian_flip"] = wrong_answers.get("endian_flip", 0) + 1
        return False


def main_game_loop():
    print("""
🩸 ========================= 🩸
    BINARY ↔ HEX ↔ DEC WAR
    + ENDIAN HELL MODE ACTIVATED
🩸 ========================= 🩸

💣 Rules:
- No mercy.
- Get it right, keep the streak.
- Fail, and I'll roast you harder than your CPU under prime95.

CTRL+C to bail like a coward.
""")

    try:
        while True:
            # 75% normal conversions, 25% endian flips for spice
            if random.random() < 0.75:
                ask_conversion_question()
            else:
                ask_endian_question()

    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        print("\nCowardly quit detected. Here's your stats:")
        print(f"Total questions: {total}")
        print(f"Wrong answers breakdown: {wrong_answers}")
        print(f"Time elapsed: {elapsed:.2f}s")
        print("Come back harder next time, or stay a weak-ass script kiddie.")

if __name__ == "__main__":
    main_game_loop()

