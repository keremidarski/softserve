def format_date(str_date):
    chopped = str_date.split("/")

    return f"{chopped[2]}-{chopped[1]}-{chopped[0]}"


print(format_date("11/12/2019") == "2019-12-11")
print(format_date("12/31/2019") == "2019-31-12")
print(format_date("01/15/2019") == "2019-15-01")
