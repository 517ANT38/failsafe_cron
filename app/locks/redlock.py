
import uuid
from redis import Redis, StrictRedis
from app.exceptions.lock_exception import LockException
from app.locks.lock import Lock, LockObj



class Redlock(Lock):
    
    
    
    
    def __init__(self,connect_info:str|dict|Redis):
        
        if type(connect_info) == dict:
            self._redis = StrictRedis(**connect_info)
        elif type(connect_info) == str:
            self._redis = StrictRedis.from_url(connect_info)
        else:
            self._redis = connect_info
            
        
    def _do_release(self,resource:str,token:str):    
        
        if self._redis.get(resource) == token:
            self._redis.delete(resource)
        
        
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

