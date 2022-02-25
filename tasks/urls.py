from rest_framework.routers import SimpleRouter

from tasks.views import TaskChangeViewSet, TaskViewSet

router = SimpleRouter()
router.register('api/task', TaskViewSet)
router.register('api/task-change', TaskChangeViewSet)

urlpatterns = router.get_urls()
