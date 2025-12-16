from fastapi import Request, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Tenant

def extract_subdomain(host: str) -> str:
    """Extract subdomain from host header."""
    # Remove port if present (e.g., "storename.localhost:8000" -> "storename.localhost")
    host_without_port = host.split(":")[0]
    parts = host_without_port.split(".")
    if len(parts) >= 2:
        return parts[0]
    return ""

async def resolve_tenant(request: Request, call_next):
    """Middleware to resolve tenant from subdomain."""
    # Bypass tenant resolution for /health endpoint
    if request.url.path == "/health":
        response = await call_next(request)
        return response
    
    host = request.headers.get("host", "")
    subdomain = extract_subdomain(host)
    
    # Return 404 for bare domains, localhost without subdomain, or www subdomain
    if not subdomain or subdomain.lower() == "www":
        raise HTTPException(status_code=404, detail="Tenant not found")
    
    db: Session = SessionLocal()
    try:
        tenant = db.query(Tenant).filter(Tenant.slug == subdomain).first()
        if not tenant:
            raise HTTPException(status_code=404, detail="Tenant not found")
        
        request.state.tenant = tenant
    finally:
        db.close()
    
    response = await call_next(request)
    return response

