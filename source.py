class Data:
    def __init__(self, type_data_v: str) -> None:
        self._list_types_data = {
            'Email' : Data.check_Email,
            'website_URL' : Data.check_Website_URL,
            'Date' : Data.check_Date,
            'Number' : Data.check_Number,
            'Credit_Card_Number' : Data.check_Credit_Card_Number,
            'Mobile_Phone_Number' : Data.check_Mobile_Phone_Number
        }
        self.type_data = type_data_v

    def data_ask(self) -> bool:
        data = input('input your data: ')
        return self._list_types_data[self.type_data](data)

    @property
    def type_data(self) -> str:
        return self._type_data

    @type_data.setter
    def type_data(self, type_data_v: str) -> None:
        if type_data_v not in self._list_types_data.keys():
            raise ValueError("Value error")
        self._type_data = type_data_v

    @staticmethod
    def check_Email(str_Email: str) -> bool:
        if (
            str_Email.count('@') == 1 and
            str_Email.index('@') != 0 and
            str_Email.index('@') != len(str_Email) - 1
        ):
            return True

    @staticmethod
    def check_Website_URL(str_Website_URL: str) -> bool:
        str_url_key_sim = "= + & ? % # ~";
        str_url_nonv_sim = "! @ # $ % ^ & * ( ) [ ] { } | \ : ; \" ' < > , ? "
        i = 0
        while i < len(str_url_nonv_sim):
            if str_url_nonv_sim[i] in str_url_key_sim:
                str_url_nonv_sim = str_url_nonv_sim.replace(str_url_nonv_sim[i],'')
            i += 1
        if str_Website_URL[:12] != 'https://www.':
            return False
        else:
            str_Website_URL = str_Website_URL.replace('https://www.', '')
        site_name = ""
        i = 0
        while i < len(str_Website_URL):
            site_name += str_Website_URL[i];
            i += 1
        if site_name.count('.') != 1:
            return False
        else:
            str_Website_URL.replace(site_name, '')
        for i in range(len(str_Website_URL)):
            if str_Website_URL[i] in str_url_nonv_sim and str_Website_URL[i - 1] != '\\':
                return False
        return True

    @staticmethod
    def check_Date(str_Date: str) -> bool:
        spl_list = str_Date.split('.')
        for i in spl_list:
            if not i.isnumeric():
                return False
        return True

    @staticmethod
    def check_Number(str_Number: str) -> bool:
        if not str_Number.isnumeric():
            return False
        return True

    @staticmethod
    def check_Credit_Card_Number(str_Credit_Card_Number) -> bool:
        for item in str_Credit_Card_Number:
            if not item.isnumeric():
                return False
        if len(str_Credit_Card_Number) == 16:
            return True
        return False

    @staticmethod
    def check_Mobile_Phone_Number(str_Mobile_Phone_Number: str) -> bool:
        if str_Mobile_Phone_Number[:4] != "+374":
            return False
        else:
            str_Mobile_Phone_Number = str_Mobile_Phone_Number.replace('+374', '')
        for item in str_Mobile_Phone_Number:
            if not str_Mobile_Phone_Number.isnumeric():
                return False
        if len(str_Mobile_Phone_Number) == 8:
            return True
        return False

_curr_inputs = ['e', 'ws', 'd', 'n', 'c', 'm']

def main() -> None:
    user_input = input("Email(e), website URL(ws), Date(d), Number(n), Credit_Card_Number(c), Mobile_Phone_Number(m): ")
    while user_input not in _curr_inputs:
        print("Erroooooor!")
        user_input = input("Email(e), website URL(ws), Date(d), Number(n), Credit_Card_Number(c), Mobile_Phone_Number(m): ")
    if user_input == 'e':
        d = Data("Email")
    elif user_input == 'ws':
        d = Data("Website_URL")
    elif user_input == 'c':
        d = Data("Credit_Card_Number")
    elif user_input == 'd':
        d = Data("Date")
    elif user_input == 'n':
        d = Data("Number")
    else:
        d = Data("Mobile_Phone_Number")
    print(d.data_ask())

if __name__ == "__main__":
    main()

