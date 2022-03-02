#!/usr/bin/python3
"""
Comments
"""
import json
import os


class FileStorage:
    """
    Comments
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}
        if self.__objects is not None:
            for key, value in self.__objects.items():
                dictionary[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, mode="r", encoding="utf-8") as file:
                    temp_objects = json.load(file)
                    for key, value in temp_objects.items():
                        instance = eval(value["__class__"])(**value)
                        self.__objects[key] = instance
            except Exception as e:
                print("{}".format(e))
        else:
            return
