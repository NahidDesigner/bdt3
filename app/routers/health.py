from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/health")
async def health(request: Request):
    tenant = getattr(request.state, "tenant", None)
    tenant_slug = tenant.slug if tenant else None
    
    return {
        "status": "ok",
        "tenant": tenant_slug
    }

