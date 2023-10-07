#include <iostream>
#include <cmath>

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int factorial(int n) {
    if (n <= 0) {
        return 1;
    }
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

double power(double base, int exponent) {
    double result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

double logarithm(double base, double x) {
    return log(x) / log(base);
}

bool isEven(int n) {
    return n % 2 == 0;
}

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int digitSum(int n) {
    int sum = 0;
    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

bool isPalindrome(int n) {
    int original = n;
    int reverse = 0;
    while (n != 0) {
        reverse = reverse * 10 + n % 10;
        n /= 10;
    }
    return original == reverse;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    char choice;

    do {
        std::cout << "Выберите действие: " << std::endl;
        std::cout << "1 - Найти факториал числа" << std::endl;
        std::cout << "2 - Возвести число в степень" << std::endl;
        std::cout << "3 - Вычислить логарифм" << std::endl;
        std::cout << "4 - Проверить число на четность" << std::endl;
        std::cout << "5 - Найти наибольший общий делитель двух чисел" << std::endl;
        std::cout << "6 - Вычислить сумму всех цифр числа" << std::endl;
        std::cout << "7 - Найти наименьшее общее кратное двух чисел" << std::endl;

        int selectedAction;
        std::cout << "Ваш выбор (1-7): ";
        std::cin >> selectedAction;

        switch (selectedAction) {
            case 1: {
                int n;
                std::cout << "Введите число: ";
                std::cin >> n;
                std::cout << "Факториал числа " << n << " = " << factorial(n) << std::endl;
                break;
            }
            case 2: {
                double base;
                int exponent;
                std::cout << "Введите основание: ";
                std::cin >> base;
                std::cout << "Введите показатель степени: ";
                std::cin >> exponent;
                std::cout << base << "^" << exponent << " = " << power(base, exponent) << std::endl;
                break;
            }
            case 3: {
                double base, x;
                std::cout << "Введите основание: ";
                std::cin >> base;
                std::cout << "Введите число: ";
                std::cin >> x;
                std::cout << "Логарифм числа " << x << " по основанию " << base << " = " << logarithm(base, x) << std::endl;
                break;
            }
            case 4: {
                int num;
                std::cout << "Введите число: ";
                std::cin >> num;
                std::cout << (isEven(num) ? "Число четное" : "Число нечетное") << std::endl;
                break;
            }
            case 5: {
                int a, b;
                std::cout << "Введите первое число: ";
                std::cin >> a;
                std::cout << "Введите второе число: ";
                std::cin >> b;
                std::cout << "НОД(" << a << ", " << b << ") = " << gcd(a, b) << std::endl;
                break;
            }
            case 6: {
                int num;
                std::cout << "Введите число: ";
                std::cin >> num;
                std::cout << "Сумма всех цифр числа " << num << " = " << digitSum(num) << std::endl;
                break;
            }
            case 7: {
                int a, b;
                std::cout << "Введите первое число: ";
                std::cin >> a;
                std::cout << "Введите второе число: ";
                std::cin >> b;
                std::cout << "НОК(" << a << ", " << b << ") = " << lcm(a, b) << std::endl;
                break;
            }
            default:
                std::cout << "Некорректный выбор." << std::endl;
        }

        std::cout << "Вы хотите продолжить? (y/n): ";
        std::cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    return 0;
}
