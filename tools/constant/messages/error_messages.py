
class EmailErrors:

    EMAIL_REQUIRED:str = "Please Enter Email"
    EMAIL_MAX_LENGTH:str = "Entred Email is too long ..."
    EMAIL_MIN_LENGTH:str = "Entred Email is too low ..."

class PasswordErrors:

    PASSWORD_REQUIRED:str = "Please Enter Password"
    PASSWORD_MAX_LENGTH:str = "Entred Password is too long ..."
    PASSWORD_MIN_LENGTH:str = "Entred Password is too low ..."

class RePasswordErrors:

    NOT_SAME:str = "Password and RePassword are not same !"

class AuthenticationErrors:

    INCORRECT_INFORMATION:str = "Entred Information Not Matched with Users of Website"

class AdsTitle:

    MAX_LENGTH_ERROR:str = "Entred Title is too long"
    REQUIRED_ERROR:str = "Please Enter Title"

class CategoryTitle:
    MAX_LENGTH_ERROR:str = "Entred Category is too long"
    REQUIRED_ERROR:str = "Please Enter Category"

class Describtion:
    MAX_LENGTH_ERROR:str = "Entred Describtion is too long"
    REQUIRED_ERROR:str = "Please Enter Describtion"

class Price:
    REQUIRED_ERROR:str = "Please Enter Price"