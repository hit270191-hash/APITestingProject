class Routes:
    Base_Url= "http://localhost:3000"

    #Product Module
    Get_All_Products= "/products"
    Get_Product_By_Id= "/products/{id}"
    Get_Product_By_Limit= "/products?_limit={limit}"
    Get_Product_By_Category= "/products?category={category}"
    Create_Product= "/products"
    Update_Product= "/products/{id}"
    Delete_Product= "/products/{id}"