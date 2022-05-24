SECRET_KEY = '-2#se2w2t^20h%7g6_6+(zztxlmz#99f*r(dgsri7@ip_8zov@'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        'USER': 'root',
        'PASSWORD': 'example',
        'HOST': 'db',
        'OPTIONS': {
                'autocommit': True
        }
    }
}

