
from app.util.generate_unique import GenerateUnique
import os

class UGenerate(GenerateUnique):
    def generate(self, size: int) -> str:
        return os.urandom(size).decode(encoding="utf-16")