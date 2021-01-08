import redis


class RediDB(object):

    def __init__(self):
        self.rdb = redis.Redis(host='localhost',
                               port=6379, db=1,
                               decode_responses=True)

    def get_totems_in_radius(self, region, longitude, latitude, radius):
        return self.rdb.georadius(region, longitude, latitude, radius,
                                  'mi')

    def set_totem_location(self, region, longitude, latitude, totem_id):
        self.rdb.geoadd(region, longitude, latitude, totem_id)

    def set_user_totem_id(self, user_id, totem_id):
        self.rdb.set('TOTEM_FOR_{}'.format(user_id), totem_id)

    def get_user_totem_id(self, user_id):
        return self.rdb.get('TOTEM_FOR_{}'.format(user_id))

    def user_join_totem(self, user_id, totem_id):
        self.rdb.lpush('USERS_AT_TOTEM_{}'.format(totem_id), user_id)

    def user_leave_totem(self, user_id, totem_id):
        self.rdb.lrem('USERS_AT_TOTEM_{}'.format(totem_id), user_id)

    def get_totem_details(self, totem_id):
        lname = 'USERS_AT_TOTEM_{}'.format(totem_id)
        users = self.rdb.lrange(lname, 0, 9)
        users_count = self.rdb.llen(lname)
        return {
            'users': users,
            'count': users_count
        }

    def set_user_totems(self, region, longitude, latitude, user_id):
        self.rdb.delete('TOTEMS_FOR_USER_{}'.format(user_id))
        totems = self.get_totems_in_radius(region, longitude, latitude, 2,
                                           'mi', 'withdist')
        for totem in totems:
            if totem[-1] <= 1:
                self.rdb.sadd(
                              'TOTEMS_FOR_USER_{}'.format(user_id),
                              totem[0])

    def check_can_chat(self, user_id, totem_id):
        return self.rdb.sismember(user_id, totem_id)


rdb = RediDB()
