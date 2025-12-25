def calculator():
    print("ماشین  حساب ساده پایتون")
    print("عملیات موجود: +  -  *  /")

    while True:
        try:
            num1 = float(input("عدد اول رو وارد کن: "))
            op = input("عملگر رو وارد کن (+ - * /): ")
            num2 = float(input("عدد دوم رو وارد کن: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("خطا: تقسیم بر صفر مجاز نیست!")
                    continue
            else:
                print("عملگر نامعتبره!")
                continue

            print(f"نتیجه: {result}\n")

        except ValueError:
            print("لطفاً فقط عدد وارد کن!\n")

        again = input("می‌خوای ادامه بدی؟ (y/n): ")
        if again.lower() != "y":
            print("خروج از ماشین حساب...")
            break

calculator()
