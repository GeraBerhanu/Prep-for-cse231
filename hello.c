#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("Hello, %s.", answer);
    string x = get_string(" How are you doing today? Good or Bad?");

    if  (strcmp(x,"Good") == 0)
{
    printf("I'm happy to hear that");
}
    else if (strcmp(x,"Bad") == 0)
{
    printf("I'm sorry to hear that");
}
}