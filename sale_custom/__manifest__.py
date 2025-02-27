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
             "data/sale_data.xml",
             "views/sale_campaign_views.xml",
             "views/sale_order_views.xml",
             "report/sale_order_report.xml"],
    "assets": {},
    "installable": True,
    "application": True,
    "auto_install": False,
}
