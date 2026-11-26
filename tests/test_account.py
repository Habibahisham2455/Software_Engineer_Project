import unittest

from account import is_valid_email, register_func, login, get_profile, update_profile


class TestAccount(unittest.TestCase):

    #testing emails

    def test_valid_email_domain(self):
        self.assertTrue(is_valid_email("name@domain"))

    def test_invalid_email_domain(self):
        self.assertFalse(is_valid_email("name@gmail.com"))

    def test_no_name_before_domain(self):
        self.assertFalse(is_valid_email("@domain"))

    #testing the register function

    def test_register_valid_user(self):
        self.assertEqual(register_func("name1@domain", "2222", "Name", "USD", 3000), "Registered successfully.")

    def test_register_decimal_income(self):
        self.assertEqual(register_func("name2@domain", "9999", "Name", "EGP", 2500.5),  "Registered successfully.")

    def test_register_duplicate_email(self):
        register_func("name3@domain", "9999", "Name Last", "USD", 6000)
        with self.assertRaises(ValueError):
            register_func("name3@domain", "9999", "Name Last", "USD", 6000)

    def test_register_invalid_email_domain(self):
        with self.assertRaises(ValueError):
            register_func("name4@gmail.com", "5678", "Name", "EGP", 5000)

    #testing login function

    def test_login_valid_credentials(self):
        register_func("name5@domain", "9999", "Name", "GBP", 5600)
        self.assertEqual(login("name5@domain", "1234"),  "Welcome, Name!")

    def test_login_invalid_password(self):
        register_func("name6@domain", "9999", "Name", "GBP", 5600)
        with self.assertRaises(ValueError):
            login("name@domain", "abcd")

    def test_login_unregistered_email(self):
        with self.assertRaises(ValueError):
            login("unknown@domain", "1234")

    #testing profile functions
    
    def test_get_existing_profile(self):
        register_func("existing@domain", "9999", "Name", "EGP", 9000)
        self.assertEqual(get_profile("existing@domain")["display_name"], "Name")

    def test_update_existing_profile(self):
        register_func("updating@domain", "9999", "Hello", "EGP", 9000)
        self.assertEqual(update_profile("updating@domain", "Hello world", "GBP", 6500), "Profile updated.")



if __name__ == "__main__":
    unittest.main()
