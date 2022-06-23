def get_budgets(lst_budgets):
    budgets_sum = 0

    for person in lst_budgets:
        budgets_sum += person["budget"]

    return budgets_sum


print(
    get_budgets(
        [
            {"name": "John", "age": 21, "budget": 23000},
            {"name": "Steve", "age": 32, "budget": 40000},
            {"name": "Martin", "age": 16, "budget": 2700},
        ]
    )
)
