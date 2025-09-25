# views.py
from django.http import HttpResponse
from django.core.cache import caches

# Access each cache
redis_cache = caches['default']
memcached_cache = caches['memcached']
file_cache = caches['file_cache']
local_cache = caches['local_memory']

# -------------------
# Redis Views
# -------------------
def set_redis_cache(request):
    redis_cache.set("redis_key", "Hello Redis!", timeout=60)
    return HttpResponse("Redis cache set successfully!")

def display_redis_cache(request):
    value = redis_cache.get("redis_key")
    return HttpResponse(f"Redis cached value: {value}")

# -------------------
# Memcached Views
# -------------------
def set_memcached_cache(request):
    memcached_cache.set("mem_key", "Hello Memcached!", timeout=120)
    return HttpResponse("Memcached cache set successfully!")

def display_memcached_cache(request):
    value = memcached_cache.get("mem_key")
    return HttpResponse(f"Memcached cached value: {value}")

# -------------------
# File-based Views
# -------------------
def set_file_cache(request):
    file_cache.set("file_key", "Hello File Cache!", timeout=300)
    return HttpResponse("File cache set successfully!")

def display_file_cache(request):
    value = file_cache.get("file_key")
    return HttpResponse(f"File cached value: {value}")

# -------------------
# Local Memory Views
# -------------------
def set_local_cache(request):
    local_cache.set("local_key", "Hello Local Memory!", timeout=60)
    return HttpResponse("Local memory cache set successfully!")

def display_local_cache(request):
    value = local_cache.get("local_key")
    return HttpResponse(f"Local memory cached value: {value}")
