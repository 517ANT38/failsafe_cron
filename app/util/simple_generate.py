import random
import string
from app.util.generate_unique import GenerateUnique

CHARACTERS = string.ascii_letters + string.digits

class SimpleGenerate(GenerateUnique):
    
    
    def generate(self,size: int) -> str:         
        return ''.join(random.choice(CHARACTERS) for _ in range(22))