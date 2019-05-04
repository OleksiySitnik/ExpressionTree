class BinaryTree:

    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None
        self.parent = None
        self.temp_value = None
        # temp_value Saves the result of the operation or the
        # value of variable for use in the following operation

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        """
        Automatically identifies the parent node for left node
        """
        node.parent = self
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        """
        Automatically identifies the parent node for right node
        """
        node.parent = self
        self._right = node

    def __repr__(self):
        str_tree = ""

        def inner_str(node=self, level=0):
            nonlocal str_tree

            if node.right:
                inner_str(node.right, level + 1)

            space_str = "    " * level
            str_tree += (space_str + str(node.value) + "\n")

            if node.left:
                inner_str(node.left, level + 1)

            return str_tree[:-1]

        return inner_str()

    # def show(self, level=0):
    #
    #     if self.right:
    #         self.right.show(level + 1)
    #
    #     space_str = "    " * level
    #     print(strn + str(self.value))
    #
    #     if self.left:
    #         self.left.show(level + 1)

    def fill_temp_value(self, variables_dict):
        """ Fill temp_values in tree

        Params:
            variables_dict - used to store the values ​​of variables
            and to use these values ​​in subsequent operations
        """

        if self.right:
            self.right.fill_temp_value(variables_dict)

        if self.left:
            self.left.fill_temp_value(variables_dict)

        # if self.value.isalnum():
        #     if not self.temp_value:
        #         self.temp_value = variables_dict.get(self.value)

        if self.value == "=":
            variables_dict[self.left.value.strip()] = round(self.right.temp_value, 3)
            self.left.temp_value = float(self.right.temp_value)

        elif self.value == "^":
            self.temp_value = self.right.temp_value ** self.left.temp_value

        elif self.value == ">>":
            self.temp_value = self.left.temp_value

        elif self.value == "+":
            self.temp_value = self.right.temp_value + self.left.temp_value

        elif self.value == "-":
            self.temp_value = self.right.temp_value - self.left.temp_value

        elif self.value == "*":
            self.temp_value = self.right.temp_value * self.left.temp_value

        elif self.value == "/":
            self.temp_value = self.right.temp_value / self.left.temp_value

        else:
            try:
                self.temp_value = float(self.value)

            except ValueError:
                if self.value.isalnum():
                    self.temp_value = variables_dict.get(self.value)
        # elif is_operator(self.value):
        #     self.temp_value = eval((self.right.temp_value + str(self.value) + str(self.left.temp_value))


class Root:

    def __init__(self):
        self.kids = []

    def __iter__(self):
        for kid in self.kids:
            yield kid

    def __getitem__(self, item):
        return self.kids[item]

    def __str__(self):
        str_root = ""
        for btree in self:
            str_root += str(btree) + "\n" * 3

        return str_root

    # def show(self):
    #     for btree in self:
    #         print(btree)
    #         print("\n"*2)
