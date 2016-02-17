import tempfile
import subprocess
import os

import idaapi

from ida_settings import IDASettings

EDITOR = r'C:\Windows\System32\notepad.exe'


class Autoruns(idaapi.plugin_t):
    flags = idaapi.PLUGIN_PROC
    comment = 'Autoruns'
    help = 'Autoruns'
    wanted_name = 'Autoruns'
    wanted_hotkey = ''

    def _edit(self):
        path = tempfile.mktemp()
        with open(path, 'wb') as f:
            f.write(self._code)

        subprocess.Popen([EDITOR, path]).wait()

        with open(path, 'rb') as f:
            self._code = f.read()

        os.unlink(path)

    @property
    def _code(self):
        try:
            return self.settings['code']
        except:
            return ''

    @_code.setter
    def _code(self, value):
        self.settings.idb['code'] = value

    def init(self):
        self.settings = IDASettings('Autoruns')

        exec(self._code)

        self.menu_items = []
        idaapi.add_menu_item('View/', 'Edit Autoruns', '', idaapi.SETMENU_INS, self._edit, tuple())
        return idaapi.PLUGIN_KEEP

    def term(self):
        for menu_items in self.menu_items:
            idaapi.del_menu_item(menu_items)

    def run(self, arg):
        pass


def PLUGIN_ENTRY():
    return Autoruns()
