
from data_transform.transform import TransformData


class TransformStr(TransformData[str,str]):
    
    def transfrom(self, data: str) -> str:
        s = data.rstrip()
        if len(s) == 0:
            return "Note 0\n"
        num = int(s.split(" ")[1])        
        return f"Note {num+1}\n"