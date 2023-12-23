mixed_data_list = [42, "Hello", 3.14, True, [1, 2, 3], {"key": "value"}, None]

string_list = list(map(lambda x: str(x), mixed_data_list))

print(string_list)

mixed_data_list_2 = [42, "Hello", 3.14, {"key": "value"}, None, "World", 7, 8, 9, "Another String"]

filtered_list = list(filter(lambda s: isinstance(s, int), mixed_data_list_2))

print(filtered_list)
