from .views import*
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'/api/director', DirectorView)
router.register(r'/api/movie', MovieView)
router.register(r'/api/plan', PlanView)
router.register(r'/api/user-plan', UserPlanView)
router.register(r'/api/favorite', FavoriteMovieView)

urlpatterns = router.urls