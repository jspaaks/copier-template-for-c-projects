#include <criterion/criterion.h>
#include "addition.h"

Test(addition, one){
    int actual = add(2, 3);
    int expected = 5;
    cr_assert(actual == expected);
}

Test(addition, two){
    int actual = add(2, -3);
    int expected = -1;
    cr_assert(actual == expected);
}
