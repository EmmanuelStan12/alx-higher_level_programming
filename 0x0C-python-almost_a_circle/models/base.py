#!/usr/bin/python3
"""This module contains base class"""
import json
import os
import csv


class Base:
    """This is a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries into json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json to a file"""
        if list_objs is None or len(list_objs) == 0:
            return
        result = []
        for inst in list_objs:
            inst_name = "{}.json".format(cls.__name__)
            dict = inst.to_dictionary()
            result.append(dict)
        json_str = Base.to_json_string(result)
        with open(inst_name, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """transforms a json to list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a class with dictionary attributes"""
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a json file"""
        file_name = "{}.json".format(cls.__name__)
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r', encoding='utf-8') as file:
            json_string = ''.join(file.readlines())
            inst_list = Base.from_json_string(json_string)
            instances = []
            for item in inst_list:
                instances.append(cls.create(**item))
        return instances 

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves json to a csv"""
        if list_objs is None or len(list_objs) == 0:
            return
        result = []
        for inst in list_objs:
            inst_name = "{}.csv".format(cls.__name__)
            dict = inst.to_dictionary()
            result.append(dict)
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            keys = ['id', 'width', 'height', 'x', 'y']
        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=result[0].keys())
            writer.writeheader()
            writer.writerows(result)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances from a csv file"""
        file_name = "{}.csv".format(cls.__name__)
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            instances = []
            for row in reader:
                print(row)
                instances.append(cls.create(**row))
        return instances 
