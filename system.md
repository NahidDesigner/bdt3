# System Constraints (Non-Negotiable)

## Backend
- FastAPI
- Python 3.11
- SQLAlchemy 2.0
- PostgreSQL

## Frontend
- React + Vite
- Tailwind CSS
- Axios
- react-i18next

## Auth
- JWT access + refresh tokens
- OTP (mock for now)

## Multitenancy
- Row-level isolation using tenant_id
- Tenant resolved from subdomain (Host header)
- One shared database

## Background Jobs
- NONE for now (explicitly deferred)

## Deployment
- Docker Compose
- Coolify
- Nginx handled by Coolify
- One backend container
- One frontend container
