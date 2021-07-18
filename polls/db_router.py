class DBRouter:

    MyApp = ['polls', 'auth', 'sessions', 'admin', 'contenttypes', ]

    MyDbId = 'polls'

    _DEBUG = False

    def _getMyDbId(self, name):
        if name in self.MyApp:
            return self.MyDbId
        return None

    def db_for_read(self, model, **hints):
        if self._DEBUG:
            print('[db_for_read] app_label : %s' % (model._meta.app_label, ))
        return self._getMyDbId(model._meta.app_label)

    def db_for_write(self, model, **hints):
        if self._DEBUG:
            print('[db_for_write] app_label : %s' % (model._meta.app_label, ))
        return self._getMyDbId(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        if self._DEBUG:
            print('[allow_relation] obj1.app_label : %s' % (obj1._meta.app_label, ))
            print('[allow_relation] obj2.app_label : %s' % (obj2._meta.app_label, ))
        r = self._getMyDbId(obj1._meta.app_label)
        if r:
            return r
        return self._getMyDbId(obj2._meta.app_label)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if self._DEBUG:
            print('[allow_migrate] app_label : %s' % (app_label, ))
        return self._getMyDbId(app_label)
