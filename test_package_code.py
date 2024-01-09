import pytest
from package_code import package_code

# Function to test calc_average
def test_calc_average():
  first_operands = [1, 5, 7]
  second_operands = [3, 8, 9]
  expected_results = [2, 6.5, 8]

  for f,s,e in zip(first_operands, second_operands, expected_results):
    calculated_average = package_code.calc_average(f,s)
    assert calculated_average == pytest.approx(e, rel=1e-6, abs=1e-6)

# Function to test min values
def test_calc_min():
  first_values = [ 7, 9, 11, 14]
  second_values = [5, 9, 15, 0]
  expected_results = [5, 9, 11, 0]

  for fv, sv, er in zip (first_values, second_values, expected_results):
    calculated_minimum = package_code.calc_min(fv, sv)
    assert calculated_minimum == er
