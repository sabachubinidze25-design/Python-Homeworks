import math


def calculator():
    """
    კალკულატორი ძლიერი შეცდომების დამუშავებით
    """
    print("=" * 60)
    print("კალკულატორი".center(60))
    print("=" * 60)

    while True:
        print("\n📋 ხელმისაწვდომი ოპერაციები:")
        print("1. + (შეკრება)")
        print("2. - (გამოკლება)")
        print("3. * (გამრავლება)")
        print("4. / (გაყოფა)")
        print("5. ** (ხარისხში აყვანა)")
        print("6. √ (ფესვის ამოღება)")
        print("7.  გასვლა")
        print("-" * 60)

        choice = input("\n➤ არჩიე ოპერაცია (1-7): ").strip()

        if not choice:
            print("შეცდომა: არაფერი არ შეგიყვანია!  სცადე ხელახლა.")
            continue

        if choice == '7' or choice. lower() in ['exit', 'გასვლა', 'quit', 'q']:
            print("\n მადლობა გამოყენებისთვის!  ")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print(f"შეცდომა: '{choice}' არასწორი არჩევანია!")
            print("გთხოვთ აირჩიოთ რიცხვი 1-დან 7-მდე.")
            continue

        try:
            if choice == '6':
                num_input = input("➤ შეიყვანეთ რიცხვი: ").strip()

                if not num_input:
                    print("შეცდომა: არაფერი არ შეგიყვანია!")
                    continue

                try:
                    num = float(num_input)
                except ValueError:
                    print(f"შეცდომა: '{num_input}' არ არის რიცხვი!")
                    print(" მაგალითად შეიყვანეთ: 16, 25, 100")
                    continue

                if num < 0:
                    print(
                        f"შეცდომა: უარყოფითი რიცხვის ({num}) ფესვი არ არსებობს!")
                    print("გთხოვთ შეიყვანოთ დადებითი რიცხვი.")
                    continue

                result = math.sqrt(num)
                print(f"\n √{num} = {result}")

            elif choice in ['1', '2', '3', '4', '5']:
                num1_input = input("➤ შეიყვანეთ პირველი რიცხვი: ").strip()

                if not num1_input:
                    print("შეცდომა: პირველი რიცხვი არ არის შეყვანილი!")
                    continue

                try:
                    num1 = float(num1_input)
                except ValueError:
                    print(f"შეცდომა: '{num1_input}' არ არის რიცხვი!")
                    print(" მაგალითად შეიყვანეთ: 5, 10. 5, -3")
                    continue

                num2_input = input("➤ შეიყვანეთ მეორე რიცხვი: ").strip()

                if not num2_input:
                    print("შეცდომა: მეორე რიცხვი არ არის შეყვანილი!")
                    continue

                try:
                    num2 = float(num2_input)
                except ValueError:
                    print(f"შეცდომა: '{num2_input}' არ არის რიცხვი!")
                    print("მაგალითად შეიყვანეთ: 5, 10.5, -3")
                    continue

                if choice == '1':
                    result = num1 + num2
                    print(f"\n{num1} + {num2} = {result}")

                elif choice == '2':
                    result = num1 - num2
                    print(f"\n{num1} - {num2} = {result}")

                elif choice == '3':
                    result = num1 * num2
                    print(f"\n{num1} × {num2} = {result}")

                elif choice == '4':
                    if num2 == 0:
                        print(
                            f"შეცდომა: {num1} / 0 - ნულზე გაყოფა შეუძლებელია!")
                        print(" მეორე რიცხვი არ უნდა იყოს ნული.")
                        continue
                    result = num1 / num2
                    print(f"\n {num1} ÷ {num2} = {result}")

                elif choice == '5':
                    if abs(num2) > 1000:
                        print(f"შეცდომა: ხარისხი ({num2}) ძალიან დიდია!")
                        print(" გთხოვთ შეიყვანოთ უფრო პატარა რიცხვი.")
                        continue
                    if num1 == 0 and num2 == 0:
                        print("შეცდომა: 0^0 მათემატიკურად განუსაზღვრელია!")
                        continue

                    if num1 == 0 and num2 < 0:
                        print("შეცდომა: 0-ს უარყოფით ხარისხში აყვანა შეუძლებელია!")
                        continue

                    try:
                        result = num1 ** num2
                        if abs(result) > 1e100:
                            print(
                                f"შეცდომა: შედეგი ({result:. 2e}) ძალიან დიდია!")
                            continue
                        print(f"\n {num1}^{num2} = {result}")
                    except OverflowError:
                        print("შეცდომა: შედეგი ძალიან დიდია გამოსათვლელად!")
                        continue

        except KeyboardInterrupt:
            print("\n\n პროგრამა შეწყვეტილია მომხმარებლის მიერ.")
            break
        except MemoryError:
            print("შეცდომა: არასაკმარისი მეხსიერება!")
        except Exception as e:
            print(f"მოულოდნელი შეცდომა: {e}")
            print("გთხოვთ სცადოთ ხელახლა.")

        print("\n" + "=" * 60)


if __name__ == "__main__":
    try:
        calculator()
    except KeyboardInterrupt:
        print("\n\nპროგრამა დახურულია.")
    except Exception as e:
        print(f"\nკრიტიკული შეცდომა: {e}")
