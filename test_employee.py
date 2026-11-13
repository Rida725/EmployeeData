from employee import employee_details

def test_employee_details_Rida():
    result = employee_details("Rida", 101, "IT", 45000)

    expected_emp = (
        "Employee Name: Rida\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 45000"
    )

    assert result == expected_emp