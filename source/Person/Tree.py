from Person.PersonalInfo import Info
from Person import Tree


class TreeNode:
    def __init__(self,
                 personal_info: Info,
                 children: list[Tree.TreeNode] | None = None,
                 parents: list[Info] | None = None,
                 main: bool = False) -> None:

        self.personal_info: Info = personal_info
        self.children: list[Info] | None = children
        self.parents: list[Info] | None = parents
        self.main: bool = main
