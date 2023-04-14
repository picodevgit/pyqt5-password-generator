import mysql.connector
from messagebox import Messages
class Database:
    def __init__(self, username: str = None, password: int = None, solution: str = None) -> None:
        self.username = username
        self.password = password
        self.solution = solution

    def validate(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )

            cursor = connection.cursor()

            self.database_names = ""
            if cursor:
                cursor.execute("SHOW DATABASES")

                for database in cursor:
                    self.database_names += database[0] + "\n"
                if self.database_names.find("password_generator_database") != -1:
                    # print("yes")
                    connection_validator = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="password_generator_database"
                    )

                    cursor_validator = connection_validator.cursor()

                    if cursor_validator:
                        cursor_validator.execute("SELECT username FROM user")

                        name = ""
                        for data in cursor_validator:
                            # print("name is: ", name)

                            # print(data)
                            name += data[0]
                            # print("name is: ", name)

                        cursor_validator.execute("SELECT password FROM user")

                        password = 0
                        for data in cursor_validator:
                            # print(data)
                            password += data[0]
                            # print("pass is: ", password)

                        if name == self.username and password == self.password:
                            self.solution =  "correct"
                            # print("solution is: ", self.solution)
                            return self.solution
                        elif name != self.username and password != self.password:
                            return "both"
                        elif name != self.username:
                            return "name"
                        elif password != self.password:
                            return "password"

                elif self.database_names.find("app_database") == -1:
                    # print("no")
                    if cursor:
                        cursor.execute("CREATE DATABASE password_generator_database")
                        connection_saver = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="password_generator_database"
                        )

                        cursor_saver = connection_saver.cursor()

                        if cursor_saver:
                            cursor_saver.execute("CREATE TABLE user("
                                                 "username VARCHAR(20),"
                                                  "password INT(4)"
                                                  ")")
                            cursor_saver.execute("CREATE TABLE generated_password_table("
                                                 "generated_password VARCHAR(100),"
                                                 "nothing VARCHAR(10)"
                                                 ")")
                            val = (self.username, int(self.password))
                            sql = "INSERT INTO user(username, password) VALUES(%s, %s)"
                            cursor_saver.execute(sql, val)

                            # solution = ""
                            cursor_saver.execute("SELECT username, password FROM user")
                            # for data in cursor_saver:
                            #     print(data)
                            return "new"
        except:
            text = "نام کاربری و رمز ورودی نادرست است." \
                   "لطفا دوباره انتحان کنید.\nتوجه شود که رمز عبور و نام کاربری باید حداقل دارای چهار حرف بدون فاصله باشد."
            self.ui.username_line.setText("")
            self.ui.password_line.setText("")
            return Messages(text).critical()

    def database_checker(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = connection.cursor()

        self.database_names = ""
        if cursor:
            cursor.execute("SHOW DATABASES")

            for database in cursor:
                self.database_names += database[0] + "\n"
            if self.database_names.find("password_generator_database") != -1:
                return "yes"


    def get_account(self):
        # print("in def")
        if self.database_checker() == "yes":
            connection_get_user = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="password_generator_database"
            )
            # print("connected")
            cursor_get_account = connection_get_user.cursor()

            if cursor_get_account:
                cursor_get_account.execute("SELECT username FROM user")

                username = ""
                for l in cursor_get_account:
                    username += l[0]

                cursor_get_account.execute("SELECT password FROM user")

                password = 0
                for i in cursor_get_account:
                    password += i[0]

                accountList = [username, password]

                return accountList
        else:
            return print("There is no account")


    def add_password_data(self, generated_passwords):
        # print("come")
        if self.database_checker() == "yes":
            adding_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="password_generator_database"
            )

            adding_cursor = adding_connection.cursor()

            if adding_cursor:
                sql = "INSERT INTO generated_password_table(generated_password, nothing) VALUES(%s, %s)"
                val = (generated_passwords, "nothing")

                # sql = "INSERT INTO generated_password_table(generated_password) VALUE(%s)"
                adding_cursor.execute(sql, val)
                alter = ""
                # for d in adding_cursor:
                #     alter += d[0]

                # print(alter)

                # print("added")
                # print("its ready")
        else:
            print("There is no account.")

    def show_data(self):
        if self.database_checker() == "yes":
            showConnection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="password_generator_database"
            )

            showCursor = showConnection.cursor()

            if showCursor:
                # print("cursor check")
                showCursor.execute("SELECT * FROM generated_password_table")
                # showCursor.fetchall()
                lastPasswords = ""
                # print("before for")
                for l in showCursor:
                    lastPasswords += l[0] + "\n"
                    # print(l)
                # print(lastPasswords)
                return lastPasswords
                #     lastPasswords += l[0]
                # if type(lastPasswords) == str:
                #     print(lastPasswords)

    def trash(self):
        if self.database_checker() == "yes":
            trashConnection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="password_generator_database"
            )

            trashCursor = trashConnection.cursor()

            if trashCursor:
                trashCursor.execute("DROP DATABASE IF EXISTS password_generator_database")



# sol = ""
# print(Database("amirl", 3422).checkData())
# print((Database().get_account()))
# print(Database().add_password_data("amir"))
# print(Database().show_data())
# Database().add_password_data("amirhosein1")