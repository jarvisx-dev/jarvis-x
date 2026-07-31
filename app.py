from core.engine import JarvisEngine
from config.settings import OWNER

jarvis = JarvisEngine()

jarvis.start()

print()

print(f"Welcome back, {OWNER}.")