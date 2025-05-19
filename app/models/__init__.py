# Import all the models to ensure they are registered with SQLAlchemy's Base
from .user import User
from .product import Product
from .package import Package
from .order import Order
from .health_profile import HealthProfile
from .appointment import Appointment
from .payment import Payment
from .analytics import AnalyticsData, SalesAnalytics, UserActivity

# This file serves as a central point to import all models, making it easier to manage and maintain the codebase.