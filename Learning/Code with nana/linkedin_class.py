class User():
    def __init__(self, user_name, email, password, job_title):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_title(self, new_title):
        self.job_title = new_title

    def get_user_info(self):
        print(f"User_Name:{self.user_name}, Email:{self.email}, Password:{self.password}, Job title:{self.job_title}")


user1 = User("Huzaifa","mdhuzaifachauhan@gmail.com","Th82647452","student")
user1.get_user_info()
user1.change_password(12345)
user1.get_user_info()