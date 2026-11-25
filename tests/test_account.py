import unittest

from account import is_valid_email, register, login, get_profile, update_profile


class TestAccount(unittest.TestCase):

    def test_valid_email_domain(self):
        self.assertTrue(is_valid_email("name@domain"))

    def test_invalid_email_domain(self):
        self.assertFalse(is_valid_email("name@gmail.com"))

    def test_no_name_before_domain(self):
        self.assertFalse(is_valid_email("@domain"))

    def test_register_valid_user(self):
        self.assertEqual(register("name@domain", "2222", "Name", "USD", 3000), (True, "Registered successfully."))

    def test_register_decimal_income(self):
        self.assertEqual(register("name@domain", "9999", "Name", "EGP", 2500.5), (True, "Registered successfully."))

    def test_register_duplicate_email(self):
        self.assertEqual(register("name@domain", "9999", "NAme Last", "USD", 6000), (False, "Account already exists."))

    def test_register_invalid_email_domain(self):
        self.assertEqual(register("name@gmail.com", "5678", "Name", "EGP", 5000), (False, "Email must end with @domain."))

    def test_login_valid_credentials(self):
        self.assertEqual(login("name@domain", "1234"), (True, "Welcome, Name!"))

    def test_login_invalid_password(self):
        self.assertEqual(login("name@domain", "abcd"), (False, "Invalid password."))

    def test_login_unregistered_email(self):
        self.assertEqual(login("unknown@domain", "1234"), (False, "Wrong Email, Try Again."))

    def test_get_existing_profile(self):
        self.assertEqual(get_profile("name@domain")["display_name"], "NAme")

    def test_update_existing_profile(self):
        self.assertEqual(update_profile("hello@domain", "hello world", "USD", 6500), (True, "Profile updated."))



if __name__ == "__main__":
    unittest.main()
