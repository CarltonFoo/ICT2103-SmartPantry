from flask import Blueprint

mysqlbp = Blueprint(
    'authentication_mysql_blueprint',
    __name__,
    url_prefix=''
)

nosqlbp = Blueprint(
    'authentication_nosql_blueprint',
    __name__,
    url_prefix=''
)
