class Menu:
    """
    This class takes a list of functions to put in a menu

    items
    in the format [{"Quit python", exit}]

    execute
    if true, the menu automatically executes the selected function
    """
    def __init__(self, items, title=None, subtitle=None, execute=True):
        assert type(items) is list
        self.items = []
        self.title = title
        self.subtitle = subtitle
        self.execute = bool(execute)
        for item in items:
            if callable(item):  # Is the menu item a function/callable variable?
                try:
                    self.items.append({item.__name__: item})
                except AttributeError:
                    # I will assume it is quit
                    self.items.append({"Quit": item})
            elif type(item) is dict:
                # Dictionary item must be in format
                # {"String", functionVariable}
                self.items.append(item)

    def show(self):
        print("=" * 100)
        if self.title:
            print("\n" + self.title)
        if self.subtitle:
            print("\n" + self.subtitle)

        for i in range(len(self.items)):
            functionName = list(self.items[i].keys())[0]
            print("{0} : {1}".format(i, functionName))

        # Select option
        option = -1
        try:
            option = int(input("\nChoose an option: "))
        except ValueError:
            print("Not a number :(")
            self.show()
        except NameError:
            print("Not a number :(")
            return self.show()

        # Validate
        if 0 <= option <= len(self.items) - 1:
            chosenFunctionName = list(self.items[option].keys())[0]
            chosenFunction = self.items[option][chosenFunctionName]
        else:
            print("Number out of bounds")
            return self.show()

        if self.execute:
            chosenFunction()
        return chosenFunction
