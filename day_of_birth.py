from lib import *

def get_index_of_week_day(date_of_birth):
    day , month , year = str(date_of_birth).split("-") 
    date_of_birth = datetime.datetime(int(year), int(month), int(day))    
    return date_of_birth.weekday()

def day_of_birth_english(index_of_day):
    int(index_of_day)
    if index_of_day < 1:
        index_of_day = 1
    elif index_of_day > 7:
        index_of_day = 7
    name_of_day = calendar.day_name[index_of_day]
    return name_of_day

def translate_to_polish(string_to_translate):
    match string_to_translate:
        case "You were born on:":
            return "Urodziłeś się w:"
        case "Monday":
            return "Poniedziałek"
        case "Tuesday":
            return "Wtorek"
        case "Wednesday":
            return "Środa"
        case "Thursday":
            return "Czwartek"
        case "Friday":
            return "Piątek"
        case "Saturday":
            return "Sobota"
        case "Sunday":
            return "Niedziela"

def translate_to_polish_old_way(string_to_translate):
    english_to_polish = {"You were born on:": "Urodziłeś się w:",
        "Monday":"Poniedziałek",
        "Tuesday": "Wtorek",
        "Wednesday":"Środa",
        "Thursday":"Czwartek",
        "Friday":"Piątek",
        "Saturday":"Sobota",
        "Sunday":"Niedziela"}
    return english_to_polish[string_to_translate] 



def main():
    print("You were born on:", day_of_birth_english(get_index_of_week_day(get_value("Enter your date of birth in format DD-MM-YYYY: "))))
    print()

def test1():
    print(get_index_of_week_day("21-06-2001"))

def test2():
    print("You were born on:",day_of_birth_english(get_index_of_week_day("21-06-2001")))

def test3():
    print(translate_to_polish("You were born on:"),translate_to_polish(day_of_birth_english(get_index_of_week_day("21-06-2001"))))

def test4():
    print(translate_to_polish_old_way("You were born on:"),translate_to_polish_old_way(day_of_birth_english(get_index_of_week_day("21-06-2001"))))

if __name__ == "__main__":
    clearConsole()
    main()
    print("TESTS:")
    test1()
    test2()
    test3()
    test4()

