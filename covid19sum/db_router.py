class DBRouter:

    MyApp = 'covid19sum'

    MyDbId = 'covid19sum'

    def _getMyDbId(self, name):
        if name == self.MyApp:
            return self.MyDbId
        return None

    def db_for_read(self, model, **hints):
        print('[%s.db_for_read] app_label : %s' % (self.MyApp, model._meta.app_label, ))
        return self._getMyDbId(model._meta.app_label)

    def db_for_write(self, model, **hints):
        print('[%s.db_for_write] app_label : %s' % (self.MyApp, model._meta.app_label, ))
        return self._getMyDbId(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        print('[%s.allow_relation] obj1.app_label : %s' % (self.MyApp, obj1._meta.app_label, ))
        print('[%s.allow_relation] obj2.app_label : %s' % (self.MyApp, obj2._meta.app_label, ))
        r = self._getMyDbId(obj1._meta.app_label)
        if r:
            return r
        return self._getMyDbId(obj2._meta.app_label)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print('[%s.allow_migrate] app_label : %s' % (self.MyApp, app_label, ))
        return self._getMyDbId(app_label)
