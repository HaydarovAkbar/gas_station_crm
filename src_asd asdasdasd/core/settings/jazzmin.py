JAZZMIN_SETTINGS = {
    "site_title": "CRM Admin",
    "site_header": "CRM Admin",
    "welcome_sign": "Welcome to CRM Admin",
    "search_model": "auth.User",
    "user_menu": [
        {"name": "Profile", "url": "admin:auth_user_change", "icon": "user", "permissions": ["auth.change_user"]},
        {"name": "API Docs", "url": "schema-swagger-ui", "icon": "book", "permissions": ["auth.change_user"]},
        {"name": "Support", "url": " ", "icon": "question-circle", "permissions": ["auth.change_user"]},

        {"name": "Settings", "url": "admin:core_setting_changelist", "icon": "cog",
         "permissions": ["auth.change_user"]},
        {"name": "Log Out", "url": "admin:logout", "icon": "sign-out-alt"},
    ],
    "user_menu_links": [
        {"name": "dev", "url": "https://kamezukashi.uz", "icon": "link"},

    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core": "fas fa-cogs",
        "app": "fas fa-home",
        "sites": "fas fa-satellite",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "custom_css": None,
    "custom_js": None,

    "fieldsets": [
        ("General Information", {"fields": ["name", "logo", "favicon"]}),
        ("SEO Information", {"fields": ["site_title", "site_header", "welcome_sign"]}),
        ("Menu Options", {"fields": ["related_modal_active", "show_ui_builder", "changeform_format"]}),
        ("User Options", {"fields": ["user_avatar", "user_avatar_diameter", "user_menu"]}),
        ("Links", {"fields": ["links"]}),
        ("Icons", {"fields": ["icons", "default_icon_parents", "default_icon_children"]}),
        ("Customization", {"fields": ["custom_css", "custom_js"]}),
    ],

    "related_modal_active": False,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "sketchy",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}