#!/usr/bin/python3
"""Contains the Base class"""
import json
import csv


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new instance from the class
        Args:
            id: instance identifier"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string representation
        Args:
            list_dictionaries: list of dictionaries
        Return: json representation of a string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls: class
            list_objs: list of objects"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f_name:
            if not list_objs:
                json.dump(json.loads("[]"), f_name)
            else:
                json.dump(
                     json.loads(
                          cls.to_json_string(
                              [obj.to_dictionary() for obj in list_objs]
                          )
                     ),
                     f_name
                )

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string: json string"""
        if not json_string:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            cls: the class
            dictionary: dictionary containing properties of cls
        Return: an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        Args:
            cls: class
        Return:  returns a list of instances"""
        try:
            file_name = cls.__name__ + ".json"
            with open(file_name, "r") as f_name:
                content = f_name.read()
                ls = [list_o for list_o in cls.from_json_string(content)]
                return [cls.create(**{k: v for k, v in d.items()}) for d in ls]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in SCV
        Args:
            cls: class
            list_objs: list of objects"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline='') as f_name:
            titles = []
            if cls.__name__ == "Rectangle":
                titles = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                titles = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f_name, fieldnames=titles)
            writer.writeheader()
            for obj in list_objs:
                # writer.writerow(vars(obj))
                if cls.__name__ == "Rectangle":
                    data = {"id": obj.id, "width": obj.width,
                            "height": obj.height, "x": obj.x, "y": obj.y}
                elif cls.__name__ == "Square":
                    data = {"id": obj.id, "size": obj.size,
                            "x": obj.x, "y": obj.y}
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV
        Args:
            cls: class"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r") as f_name:
                content = csv.DictReader(f_name)
                titles = content.fieldnames
                data = [obj for obj in content]
                return [
                    cls.create(**{k: int(v) for k, v in d.items()})
                    for d in data
                ]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rectangles and squares
        Args:
            list_rectangles: list of rectangles
            list_squares:list of squares"""
        import turtle
        turtle.hideturtle()
        turtle.setup(400, 400)
        turtle.bgcolor("red")
        turtle.pensize(5)
        turtle.speed(3)
        for rec in list_rectangles:
            turtle.penup()
            turtle.goto(rec.x, rec.y)
            turtle.pendown()
            turtle.color("blue")
            turtle.goto(rec.x + rec.width, rec.y)
            turtle.goto(rec.x + rec.width,
                        rec.y + rec.height)
            turtle.goto(rec.x, rec.y + rec.height)
            turtle.goto(rec.x, rec.y)
        for sr in list_squares:
            turtle.penup()
            turtle.goto(sr.x, sr.y)
            turtle.pendown()
            turtle.color("green")
            turtle.goto(sr.x + sr.size, sr.y)
            turtle.goto(sr.x + sr.size,
                        sr.y + sr.size)
            turtle.goto(sr.x, sr.y + sr.size)
            turtle.goto(sr.x, sr.y)
