map_options = {"yes": "[Y|n]", "no": "[y|N]", "": "[y|n]"}
invalid_message = "Invalid option!"
map_values = {"y": "yes", "n": "no"}
def input_yes_no(question, default="no"):
    default = default if default is not None else ""
    map_values_2 = {**map_values, "": default}
    map_fn = lambda x: map_values_2.get(x, x)
    options = map_options[map_fn(default)]
    while True:
        ans = map_fn(input(f"{question} {options} ").strip().lower())
        if ans in ["yes", "no"]: return ans == "yes"
        print(invalid_message)

if __name__ == "__main__":
    print(input_yes_no("Cake?", default="yes"))
    print(input_yes_no("Coke?", default="no"))
    print(input_yes_no("Pie?", default=None))
