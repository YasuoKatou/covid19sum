class DBRouter:

    MyApp = 'covid19sum'

    MyDbId = 'covid19sum'

    def db_for_read(self, model, **hints):
        print('[db_for_read] app_label : %s' % model._meta.app_label)
        if model._meta.app_label == self.MyApp:
            return self.MyDbId
        return None

    def db_for_write(self, model, **hints):
        print('[db_for_write] app_label : %s' % model._meta.app_label)
        if model._meta.app_label == self.MyApp:
            return self.MyDbId
        return None

    def allow_relation(self, obj1, obj2, **hints):
        print('[allow_relation] obj1.app_label : %s' % obj1._meta.app_label)
        print('[allow_relation] obj2.app_label : %s' % obj2._meta.app_label)
        if (obj1._meta.app_label == MyApp or
            obj2._meta.app_label == MyApp):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print('[allow_migrate] app_label : %s' % app_label)
        if app_label == self.MyApp:
            return self.MyDbId
        return None
