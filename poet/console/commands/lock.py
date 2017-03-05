# -*- coding: utf-8 -*-

from ...installer import Installer

from .command import Command


class LockCommand(Command):
    """
    Lock the dependencies set in poetry.toml.

    lock
        {--f|force : Force locking}
    """

    def handle(self):
        if self.has_lock() and not self.option('force'):
            return

        installer = Installer(self, self._repository)

        installer.lock(self.poet)
