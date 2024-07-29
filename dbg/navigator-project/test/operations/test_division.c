#include <criterion/criterion.h>
#include "operations/division.h"

Test(operations_division, one){
    int actual = operations_divide(2, 3);
    int expected = 0;
    cr_assert(actual == expected);
}

Test(operations_division, two){
    int actual = operations_divide(2, -3);
    int expected = 0;
    cr_assert(actual == expected);
}
