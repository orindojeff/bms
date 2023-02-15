from django.contrib.admin import AdminSite


class ProjectManagementAdminSite(AdminSite):
    site_header = "WALLPAPER KENYA"
    site_title = "Wallpaper Kenya Admin Portal"
    index_title = "Welcome to Wallpaper Kenya Admin Portal"

spm_admin_site = ProjectManagementAdminSite(name='spm_admin')

