def deploy():

    #run deployment task
    from app import create_app,db
    from flask_migrate import init,migrate,stamp,upgrade
    from models import User

    app=create_app()
    app.app_context().push()
    db.create_all()

    #migrate database
    init()
    stamp()
    migrate()
    upgrade()

deploy()
