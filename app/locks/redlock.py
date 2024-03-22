
import uuid
from redis import StrictRedis
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
        self._resource = resource_name
        if type(connect_info) == dict:
            self._redis = StrictRedis(**connect_info)
        else:
            self._redis = StrictRedis.from_url(connect_info)
        
        
    def _do_release(self,token:str):        
        self._redis.eval(self._unlock_script, 1, self._resource, token)
        
        
    def _do_acquire(self,token:str):
        if self._redis.set(self._resource,token,nx = True,px = self._ttl):
            return True
        return False        
        
    
    
    def acquire(self):
        
        token = uuid.uuid1().hex.encode()  
        if not self._do_acquire(token):            
            raise LockException("It is not possible to take the lock")
        self._token = token
        
        
        
            
    def release(self):
        expected_token = self._token
        if expected_token is None:
            raise LockException("Cannot release an unlocked lock")
        self._token = None
        self._do_release(expected_token)

