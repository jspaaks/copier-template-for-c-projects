#include <criterion/criterion.h>
#include "operations/multiplication.h"

Test(operations_multiplication, one){
    int actual = operations_multiply(2, 3);
    int expected = 6;
    cr_assert(actual == expected);
}

Test(operations_multiplication, two){
    int actual = operations_multiply(2, -3);
    int expected = -6;
    cr_assert(actual == expected);
}
