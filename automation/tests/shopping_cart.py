from automation.driver.web_driver import WebDriver


class ShoppingCart(WebDriver):
    def __init__(self, url):
        super().__init__(url)

    def test_case_05(self):
        self.find_by("id", "add-to-cart-button").click()

    def test_case_06(self):
        self.go_to("https://www.amazon.com.br/gp/cart/view.html?ref_=nav_cart&irclickid=Qrl1qr3DkxyPTHQR"
                   "-3QSTT8eUkC2jcVX6TY21Q0&ref=dmm_asc_ir_4061861_Qrl1qr3DkxyPTHQR-3QSTT8eUkC2jcVX6TY21Q0&irgwc=1")
        self.find_by("name", "submit.delete.67c4ba28-8716-4cb7-90f4-79de79e669c4").click()
