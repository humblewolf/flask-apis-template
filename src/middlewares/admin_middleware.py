from flask import request, g

from src.consts import config, sym
# from src.utils import FmfException


class FsAdminMiddleware:
    def process_req(self):
        pass
        # if request.path.startswith("/admin/"):
        #     # this is an admin route hit
        #     # this user shall have admin creds
        #     if 'username' in request.values and 'password' in request.values:
        #         if request.values['username'] == config.admin_username \
        #                 and request.values['password'] == config.admin_password:
        #             # this will be valid for a request lifecycle only
        #             # https://flask.palletsprojects.com/en/1.1.x/api/#application-globals
        #             g.setdefault(sym.MiscSymbols.is_admin_request.name, True)
        #         else:
        #             raise FmfException("auth failed, admin creds incorrect")
        #     else:
        #         raise FmfException("auth failed, creds not supplied")
