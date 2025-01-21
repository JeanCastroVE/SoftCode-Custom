{
    "name": "Sale Custom",
    "summary": """
        Customizaciones de Sale
        """,
    "author": "Softcode",
    "contributors": [
        "Jean Castro <jeancastro.developerve@gmail.com>"
    ],
    "license": "LGPL-3",
    "website": "",
    "category": "Softcode",
    "version": "17.1",
    "depends": ["sale",
                "sale_management"],
    "data": ["security/sale_security.xml",
             "security/ir.model.access.csv",
             "views/sale_campaign_views.xml"],
    "assets": {},
    "installable": True,
    "application": True,
    "auto_install": False,
}
