
import uuid
from redis import StrictRedis
from app.exceptions.lock_exception import LockException
from app.locks.lock import Lock, LockObj



class Redlock(Lock):
    
    _unlock_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end"""
   
    
    
    def __init__(self,connect_info:str|dict):
        
        if type(connect_info) == dict:
            self._redis = StrictRedis(**connect_info)
        else:
            self._redis = StrictRedis.from_url(connect_info)
        
        
    def _do_release(self,resource:str,token:str):        
        self._redis.eval(self._unlock_script, 1, resource, token)
        
        
    def _do_acquire(self,token:str,resource:str,ttl:int):
        if self._redis.set(resource,token,nx = True,px = ttl):
            return True
        return False        
        
    
    
    def acquire(self,resource_name:str,ttl:float):        
        token = uuid.uuid1().hex.encode()  
        ttl_ml = int(ttl * 1000)
        if not self._do_acquire(token,resource_name,ttl_ml):            
            raise LockException("It is not possible to take the lock")
        return LockObj(resource_name,token)
        
        
        
            
    def release(self,lock_obj:LockObj):        
        self._do_release(lock_obj.resource,lock_obj.token)

