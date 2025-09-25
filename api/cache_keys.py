from rest_framework_extensions.key_constructor.constructors import DefaultKeyConstructor
from rest_framework_extensions.key_constructor.bits import (
    ListSqlQueryKeyBit,
    PaginationKeyBit,
    QueryParamsKeyBit,
    RetrieveSqlQueryKeyBit,
    UserKeyBit,
)


# Cache key for list endpoints with filters, search, pagination
class ApplicationsListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    query_params = QueryParamsKeyBit()


class UserApplicationsListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    query_params = QueryParamsKeyBit()
    user = UserKeyBit()


class ApplicationsDetailKeyConstructor(DefaultKeyConstructor):
    """
    Key for retrieve endpoints — uses the SQL fingerprint for the single-object query.
    """

    retrieve_sql = RetrieveSqlQueryKeyBit()


class ListCacheKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    query_params = QueryParamsKeyBit()


class DetailCacheKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
    query_params = QueryParamsKeyBit()


class JobsListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    query_params = QueryParamsKeyBit()


class JobsDetailKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
