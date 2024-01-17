from typing import Literal

from Person.PersonalInfo import Info


class Node:
    def __init__(self,
                 personal_info: Info,
                 children: list | None = None,
                 parents: list | None = None,
                 spouse=None) -> None:
        """
        :param personal_info:
        :type personal_info: Info
        :param children:
        :type children: list[Node] | None
        :param parents:
        :type parents: list[Node] | None
        :param spouse:
        :type spouse: Node | None
        """
        self.personal_info: Info = personal_info
        self.children: list[Node] | None = children
        self.parents: list[Node] | None = parents
        self.spouse: Node | None = spouse

    def __str__(self) -> str:
        return self.personal_info.first_name + " " + self.personal_info.last_name

    def add_relation(self, relative, relation: Literal["child", "parent", "spouse"]) -> None:
        """
        :param relation:
        :type relative: Node
        :param relation:
        :type relation: Literal["child", "parent", "spouse"]
        """
        def __add_child():
            if self.children is not None:
                self.children.append(relative)
            else:
                self.children = [relative]

        def __add_parent():
            if len(self.parents) >= 2:
                raise AttributeError("Cannot have more than two parents")
            if self.parents is not None:
                self.parents.append(relative)
            else:
                self.parents = [relative]

        def __add_spouse():
            self.spouse = relative

        match relation:
            case "child": __add_child()
            case "parent": __add_parent()
            case "spouse": __add_spouse()
            case _: raise ValueError("Invalid relation")


class Tree:
    def __init__(self, root: Node):
        self.root: Node = root

    @staticmethod
    def add_relation(target: Node, relative: Node, relation: Literal["child", "parent", "spouse"]):
        target.add_relation(relative, relation)
