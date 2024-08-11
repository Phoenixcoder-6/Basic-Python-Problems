class Account:
    def __init__(self, acc_no, acc_pwd):
        self.acc_no = acc_no
        self.__acc_pwd = acc_pwd

    def reset_pwd(self, old_pwd, new_pwd):
        if self.__acc_pwd == old_pwd:
            self.__acc_pwd = new_pwd
            print("Password change successful")
        else:
            print("Incorrect old password")

# Create an account instance
A1 = Account(12345, "abhg")

# Print the account number
print(A1.acc_no)

# Attempt to reset the password
A1.reset_pwd("abgh", "abgh")
