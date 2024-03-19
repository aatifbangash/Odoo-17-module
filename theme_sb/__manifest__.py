{
    'name': 'SB Theme 2',
    'description': 'SB website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/snippets/block_1.xml',
        'views/snippets/block_2.xml',
        'views/snippets/block_3.xml',
        'views/homepage.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'theme_sb/static/css/style.scss',
            'theme_sb/static/src/js/script.js',
        ],
    },
    'license': 'LGPL-3',
}
