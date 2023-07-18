class CategoricalHandlingError(Exception):
    def __init__(self, error):
        self.message = error.args[0]
        self.tip = "You probably did not select a way of handling Categorical values."
        super().__init__(self.message)