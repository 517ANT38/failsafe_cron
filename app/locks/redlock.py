
from redis import Redis, RedisError, StrictRedis
from app.exceptions.lock_exception import LockException
from app.locks.lock import Lock
from app.util.generate_unique import GenerateUnique
from app.util.simple_generate import SimpleGenerate
from app.util.util import ObjLock


class Redlock(Lock):
    
    _unlock_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end"""
    _generate_val:GenerateUnique
    _server_redis:Redis
    
    def __init__(self,connect_info:str|dict,generate_val = SimpleGenerate()):
        
        self._generate_val = generate_val
        if type(connect_info) == dict:
            self._server_redis = StrictRedis(**connect_info)
        else:
            self._server_redis = StrictRedis.from_url(connect_info)
        
        
    def _release_instance(self, resource:str,key:str):        
        self._server_redis.eval(self._unlock_script, 1, resource, key)
        
        
    def _acquire_instance(self,resorce: str,val:str, ttl: int):
        return self._server_redis.set(resorce,val,nx = True,px = ttl)        
        
    
    
    def acquire(self, resorce: str, ttl: int):
        
        val = self._generate_val.generate(22)    
        try:
            flag = self._acquire_instance(resorce,val,ttl)
            if not flag:            
                raise LockException("It is not possible to take the lock")
            return ObjLock(resorce,val)
        except RedisError as e:
            raise LockException(e)
        
        
            
    def release(self, lock: ObjLock):
        self._release_instance(lock.resource,lock.key)

