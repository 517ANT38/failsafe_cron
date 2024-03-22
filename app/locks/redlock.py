
import uuid
from redis import RedisError, StrictRedis
from app.exceptions.lock_exception import LockException
from app.locks.lock import Lock



class Redlock(Lock):
    
    _unlock_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end"""
   
    
    
    def __init__(self,connect_info:str|dict,resource_name:str,ttl:float):
        self._ttl = int(ttl*1000)
        self._resource_name = resource_name
        if type(connect_info) == dict:
            self._server_redis = StrictRedis(**connect_info)
        else:
            self._server_redis = StrictRedis.from_url(connect_info)
        
        
    def _do_release(self, resource:str,token:str):        
        self._server_redis.eval(self._unlock_script, 1, resource, token)
        
        
    def _do_acquire(self,resorce: str,token:str, ttl: int):
        return self._server_redis.set(resorce,token,nx = True,px = ttl)        
        
    
    
    def acquire(self):
        
        token = uuid.uuid1().hex    
        try:
            flag = self._do_acquire(self._resource_name,token,self._ttl)
            if not flag:            
                raise LockException("It is not possible to take the lock")
            self._token = token
        except RedisError as e:
            raise LockException("Redis error",e)
        
        
            
    def release(self):
        expected_token = self._token
        if expected_token is None:
            raise LockException("Cannot release an unlocked lock")
        self._token = None
        self._do_release(self._resource_name,expected_token)

