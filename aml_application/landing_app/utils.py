from base_app.models import AvailableApps

def get_available_apps() -> list[str]:
    available_apps_obj = AvailableApps.objects.all()
    available_apps = [app.name for app in available_apps_obj]
    return available_apps