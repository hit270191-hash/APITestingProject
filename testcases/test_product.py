import requests
import pytest
from routes.Routes import Routes
from payloads.Payload import Payload
import json

new_product_id= None

class TestProduct:
    @pytest.fixture(autouse=True)
    def init_class_var(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.category= "fitness"
        self.payload = Payload().product_payload()

    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_get_all_products(self):
        # print(self.base_url)
        res= requests.get(self.base_url+Routes.Get_All_Products)
        data= res.json()
        # print(json.dumps(data, indent=4))
        assert res.status_code ==200

    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_get_product_by_id(self):
        # product_id= self.config.get_property("productId")
        # print(new_product_id)
        res= requests.get(self.base_url+Routes.Get_Product_By_Id.format(id=new_product_id))
        data= res.json()
        print(json.dumps(data, indent=4))
        assert res.status_code ==200

    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_get_product_by_limit(self):
        limit= self.config.get_property("limit")
        res= requests.get(self.base_url+Routes.Get_Product_By_Limit.format(limit=limit))
        data = res.json()
        print(json.dumps(data, indent=4))
        assert res.status_code ==200

    @pytest.mark.smoke
    @pytest.mark.order(3)
    def test_get_product_by_category(self):
        res= requests.get(self.base_url+Routes.Get_Product_By_Category.format(category=self.category))
        data = res.json()
        print(json.dumps(data, indent=4))
        assert res.status_code ==200

    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_create_product(self):
        global new_product_id
        res= requests.post(self.base_url+Routes.Create_Product, json=self.payload.__dict__)
        assert res.status_code ==201
        data=res.json()
        # print(json.dumps(data, indent=4))
        assert data["title"]== self.payload.__dict__["title"]
        new_product_id = data["id"]
        print("New Product Created")

    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_update_product(self):
        print(new_product_id)
        res= requests.put(self.base_url+Routes.Update_Product.format(id=new_product_id), json=self.payload.__dict__)
        assert res.status_code ==200
        data=res.json()
        # print(json.dumps(data, indent=4))
        assert data["title"]== self.payload.__dict__["title"]
        print("Product Updated")

    @pytest.mark.regression
    @pytest.mark.order(7)
    def test_delete_product(self):
        res= requests.delete(self.base_url+Routes.Delete_Product.format(id=new_product_id))
        assert res.status_code ==200
        print("Product Deleted")
