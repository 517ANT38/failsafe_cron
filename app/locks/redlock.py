
import logging
import time
from redis import RedisError, StrictRedis
from app.exceptions.lock_exception import LockException
from app.locks.lock import Lock
from app.util.simple_generate import SimpleGenerate
from app.util.util import ObjLock


class Redlock(Lock):
    
    unlock_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end"""
    
    def __init__(self,connect_info:str|dict):
        
        self.gerate_val = SimpleGenerate()
        if type(connect_info) == dict:
            self.server_redis = StrictRedis(**connect_info)
        else:
            self.server_redis = StrictRedis.from_url(connect_info)
        
        
    def _unlock_instance(self, resource:str,key:str):        
        self.server_redis.eval(self.unlock_script, 1, resource, key)
        
        
    def _lock_instance(self,resorce: str,val:str, ttl: int):
        return self.server_redis.set(resorce,val,nx = True,px = ttl)        
        
    
    
    def lock(self, resorce: str, ttl: int):
        
        val = self.gerate_val.generate(22)    
        try:
            flag = self._lock_instance(resorce,val,ttl)
            if not flag:            
                raise LockException("It is not possible to take the lock")
            return ObjLock(resorce,val)
        except RedisError as e:
            raise LockException(e)
        
        
            
    def unlock(self, lock: ObjLock):
        self._unlock_instance(lock.resource,lock.key)

