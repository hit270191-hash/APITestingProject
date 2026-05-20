import os
from dataclasses import asdict

import pytest
import requests
from utils.DataProvider import read_json_data
from utils.DataProvider import read_excel_data
from datamodels.Product import Product
from routes.Routes import Routes

path= os.path.abspath(os.path.join(os.path.dirname(__file__),"../testData/productdata.json"))
xlpath= os.path.abspath(os.path.join(os.path.dirname(__file__),"../testData/products_data.xlsx"))

class TestProductAPI:

    @pytest.fixture(autouse=True)
    def init_class_var(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]

    @pytest.mark.parametrize("product_test_data",read_json_data(path))  #[({},), ({},), ({},)]
    # @pytest.mark.parametrize("product_test_data", read_excel_data(xlpath, "products_data"))
    def test_add_new_delete_product(self, product_test_data):
        product_data= product_test_data[0]     ##to run for json file add [0]

        title= product_data["title"]
        description= product_data["description"]
        price= product_data["price"]
        category= product_data["category"]
        stock= product_data["stock"]
        payload= Product(title,price,description,category,stock)

        # response = requests.post(self.base_url+Routes.Create_Product,json=payload.__dict__)
        response = requests.post(self.base_url + Routes.Create_Product, json= asdict(payload))
        assert response.status_code==201
        data=response.json()

        assert data["title"] == title
        product_id= data["id"]

        #Delete Product
        res = requests.delete(self.base_url+Routes.Delete_Product.format(id= product_id))
        assert res.status_code==200




