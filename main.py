from automation.tests.shopping_cart import ShoppingCart
from dotenv import load_dotenv
from automation.data.user_data import UserData

load_dotenv()


if __name__ == "__main__":
    user = UserData()
    from automation.tests.login import Login

    login = Login(user, "https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A"
                        "%2F%2Fwww.amazon.com.br%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome"
                        "%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_"
                        "%3Dnav_AccountFlyout_signout&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.ns"
                        "=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    login.test_case_01()

    sc = ShoppingCart("https://www.amazon.com.br/gp/product/B0BSYM83KD/ref=ox_sc_rp_title_rp_1?psc=1&pf_rd_p=8bf9544f"
                      "-9359-4cba-a3cf-681926554abc&pd_rd_wg=Ejbsv&pd_rd_i=B0BSYM83KD&pd_rd_w=zV4LR&content-id=amzn1"
                      ".sym.8bf9544f-9359-4cba-a3cf-681926554abc&pd_rd_r=KPKW2S3575MX7HYDZ5DR&irclickid"
                      "=Qrl1qr3DkxyPTHQR-3QSTT8eUkC2jcze6TY21Q0&ref=dmm_asc_ir_4061861_Qrl1qr3DkxyPTHQR"
                      "-3QSTT8eUkC2jcze6TY21Q0&irgwc=1")

    sc.test_case_06()
    sc.wait(2)
