def validate_credentials(user_input, passuser_input):
    """ฟังก์ชันตรวจสอบชื่อผู้ใช้และรหัสผ่าน"""
    if user_input == "admin" and passuser_input == "Ad13n@23t":
        return True
    return False

def main():
    user_input = input("Enter username: ")
    passuser_input = input("Enter password: ")

    try:
        if validate_credentials(user_input, passuser_input):
            print("Welcome, admin")
        else:
            print("Invalid username or password!")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
