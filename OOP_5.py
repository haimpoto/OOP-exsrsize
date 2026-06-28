class DictUtils:

    @staticmethod
    def from_lists(keys: list, values: list) -> dict:
        new_dict = {}
        for i, key in enumerate(keys):
            new_dict[key] = values[i]
        return new_dict

    @staticmethod
    def from_tuples(tuples_list: list[tuple]) -> dict:
        new_dict = {}
        for tup in tuples_list:
            new_dict[tup[0]] = tup[1]
        return new_dict

    @staticmethod
    def count_dict(items: list) -> dict:
        new_dict = {}
        for i, item in enumerate(items):
            if item not in new_dict:
                new_dict[item] = 1
            else:
                new_dict[item] += 1
        return new_dict

    @staticmethod
    def nested_dict(keys: list, default_value=None) -> dict:
        new_dict = {}
        for key in keys:
            if not default_value:
                new_dict[key] = {}
            else:
                new_dict[key] = {default_value: default_value}
        return new_dict

    @staticmethod
    def count_inf(dictionary: dict) -> dict:
        new_dict = {"keys": 0, "unique_values": 0}
        values = []
        for key, value in dictionary.items():
            new_dict["keys"] += 1
            if value not in values:
                new_dict["unique_values"] += 1
                values.append(value)
        return new_dict

    @staticmethod
    def find_key_by_value(dictionary: dict, value):
        for key in dictionary:
            if dictionary[key] == value:
                return key
        return None

    @staticmethod
    def dict_status(dictionary: dict) -> str:
        if not dictionary:
            return "empty"
        keys = False
        for key in dictionary.keys():
            if key:
                keys = True
                break
        if not keys:
            return "has_empty_keys"
        values = False
        for value in dictionary.values():
            if value:
                values = True
                break
        if not values:
            return "has_empty_values"
        else:
            return "full"

    @staticmethod
    def numeric_status(dictionary: dict) -> dict:
        new_dict = {}
        temp_list = []
        for value in dictionary.values():
            if isinstance(value,(int, float)):
                temp_list.append(value)
        if not temp_list:
            return {}
        new_dict["sum"] = sum(temp_list)
        new_dict["average"] = new_dict["sum"] / len(temp_list)
        new_dict["min"] = min(temp_list)
        new_dict["max"] = max(temp_list)
        return new_dict

    @staticmethod
    def common_keys(dict1: dict, dict2: dict) -> list:
        list_of_keys = []
        for key in dict1.keys():
            if key in dict2:
                list_of_keys.append(key)
        return list_of_keys

    @staticmethod
    def print_dict(dictionary: dict, title: str = "Dictionary") -> None:
        print(f" === {title} === ")
        for key, value in dictionary.items():
            print(f"\t{key}: {value}")
        print("", "=" * (len(title) + 8))

    @staticmethod
    def safe_update(dictionary: dict, key, value) -> None | str:
        if key in dictionary:
            dictionary[key] = value
            return None
        else:
            return "Error. this key does not exist in dictionary"

    @staticmethod
    def merge_dicts(dict1: dict, dict2: dict, conflict_strategy: str = "keep_first") -> dict:
        new_dict = {}
        for key in dict1:
            new_dict[key] = dict1[key]
        if conflict_strategy == "keep_first":
            for key in dict2:
                if key not in new_dict:
                    new_dict[key] = dict2[key]
        elif conflict_strategy == "keep_second":
            for key in dict2:
                new_dict[key] = dict2[key]
        elif conflict_strategy == "sum_values":
            for key in dict2:
                if key not in new_dict:
                    new_dict[key] = dict2[key]
                else:
                    new_dict[key] += dict2[key]
        return new_dict



dic1 = {1: 1, "desw": 2, "qwertyu": 1, 8: "haim", "poto": 8}
dic2 = {"1": 1, "": 2}
print(DictUtils.find_key_by_value(dic1, 1))
print(DictUtils.numeric_status(dic1))
DictUtils.print_dict(dic1, "qwerty")
