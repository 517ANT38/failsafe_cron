
import time
from redis import RedisError, StrictRedis
from locks.lock import Lock
from util.util import ObjLock, get_unique_id


class Redlock(Lock):
    
    
    def __init__(self,connect_info:str|dict,retry_count=3, retry_delay=0.2):
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        if type(connect_info) == dict:
            self.server_redis = StrictRedis(**connect_info)
        else:
            self.server_redis = StrictRedis.from_url(connect_info)
        
        
    def _unlock_instance(self, resource:str,key:bytes):
        if self.server_redis.get(resource) == key:
            self.server_redis.delete(resource)
        
    def _lock_instance(self,resorce: str,val:bytes, ttl: int):
        self.server_redis.set(resorce,val,nx = True,px = ttl)
    
    def lock(self, resorce: str, ttl: int):
        retry = 0
        val = get_unique_id()
        err = None
        while retry < self.retry_count:
            start_time = int(time.time() * 1000)
            try:
                self._lock_instance(resorce,val,ttl)
            except RedisError as e:
                err = e
            elapsed_time = int(time.time() * 1000) - start_time
            validity = int(ttl - elapsed_time)
            if validity > 0:
                if err:
                    raise err
                return ObjLock(validity,resorce,val)
            else:
                retry += 1
                time.sleep(self.retry_delay)
        return False
            
    def unlock(self, lock: ObjLock):
        self._unlock_instance(lock.resource,lock.key)
