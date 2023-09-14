from generic.base_setup import Base_SetUp
from generic.excel import Excel

class Test1(Base_SetUp):

    def test1(self):
        p = Excel.get_cell_data("../test_data/input.xlsx", "Sheet1", 1, 1)
        print("Data from excel",p)
        print("executing test")
        print(self.driver.title)
