def rail_fence_encrypt(text, key):
    rail = [''] * key
    row, step = 0, 1

    for char in text:
        rail[row] += char
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return ''.join(rail)


def rail_fence_decrypt(cipher, key):
    pattern = list(range(key)) + list(range(key - 2, 0, -1))
    indexes = [pattern[i % len(pattern)] for i in range(len(cipher))]
    counts = [indexes.count(i) for i in range(key)]

    rails, pos = [], 0
    for count in counts:
        rails.append(cipher[pos:pos + count])
        pos += count

    rail_pos = [0] * key
    result = ''
    for i in indexes:
        result += rails[i][rail_pos[i]]
        rail_pos[i] += 1

    return result


def main():
    while True:
        print("\n--- Rail Fence Cipher ---")
        print("1. Encrypt text from file")
        print("2. Decrypt text from file")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            filename = input("Enter filename to read plaintext: ")
            try:
                with open(filename, 'r') as f:
                    plaintext = f.read().strip()
                key = int(input("Enter number of rails: "))
                encrypted = rail_fence_encrypt(plaintext, key)
                with open("encrypted.txt", 'w') as f:
                    f.write(encrypted)
                print("\n✅ Encrypted text saved in 'encrypted.txt'")
            except FileNotFoundError:
                print("❌ File not found! Please check the filename.")

        elif choice == '2':
            filename = input("Enter filename to read ciphertext: ")
            try:
                with open(filename, 'r') as f:
                    ciphertext = f.read().strip()
                key = int(input("Enter number of rails used during encryption: "))
                decrypted = rail_fence_decrypt(ciphertext, key)
                with open("decrypted.txt", 'w') as f:
                    f.write(decrypted)
                print("\n✅ Decrypted text saved in 'decrypted.txt'")
            except FileNotFoundError:
                print("❌ File not found! Please check the filename.")

        elif choice == '3':
            print("Exiting program. 👋")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
