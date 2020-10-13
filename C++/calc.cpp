# include <iostream>
using namespace std;

int main()
{
    char o;
    float num1, num2;
    cout << "Enter two number: ";
    cin >> num1 >> num2;

    cout << "Enter operator";
    cin >> o;


    switch(o)
    {
        case '+':
            cout << "the answer is\n" << num1+num2;
            break;

        case '-':
            cout << "the answer is\n" << num1-num2;
            break;

        case '*':
            cout << "the answer is\n" << num1*num2;
            break;

        case '/':
            cout << "the answer is\n" << num1/num2;
            break;

        default:
            // If the operator is other than +, -, * or /, error message is shown
            cout << "Error! operator is not correct";
            break;
    }

    return 0;
}