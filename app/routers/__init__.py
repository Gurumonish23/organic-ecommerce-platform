# Import all the routers to ensure they are registered with the FastAPI application
from .admin import router as admin_router
from .auth import router as auth_router
from .nutritionists import router as nutritionists_router
from .orders import router as orders_router
from .packages import router as packages_router
from .payments import router as payments_router
from .products import router as products_router

# This file serves as a central point to import all routers, making it easier to manage and maintain the codebase.