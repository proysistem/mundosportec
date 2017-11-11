# coding=utf-8

# from datetime import datetime
# from os.path import isfile

from fabric.api import sudo, run, env, cd, local, settings, prefix, task


env.directory = '~/webapps/mundosportec/'
env.activate = 'source ~/.virtualenvs/mundosportec/bin/activate'
env.hosts = ['45.55.223.175', ]
env.project = 'mundosportec'
env.user = 'pro'


@task
def upgrade():
    """
        Update server content
    """

    with settings(warn_only=True):
        local("git push")

    with cd(env.directory):
        run('git pull')
        with prefix(env.activate):
            run('pip install -r requirement/production.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic -l --noinput')
        sudo("supervisorctl restart %s" % env.project)


# @task
# def backup():
#     now = datetime.now()
#     file_name = 'cacperu_%s.out' % now.strftime("%Y-%m-%d_%Hh")  # :%M:%S

#     if not isfile('/home/guido/%s' % file_name):
#         # Genera el respaldo
#         with cd('~'):
#             run('sudo -u postgres pg_dumpall > %s' % file_name)
#         # Descarga el archivo
#         local('scp pytel@server.cacperu.com:%s /home/guido/' % file_name)
#     # Ejecuta el respaldo
#     local('sudo -u postgres psql -f /home/guido/%s' % file_name)


# @task
# def call_command(command):
#     """
#         Ejecuta un comando de manage.py:
#         $ fab call_command:"migrate"
#     """

#     with settings(warn_only=True):
#         local("hg push")

#     with cd(env.directory):
#         run('hg pull -u')
#         with prefix(env.activate):
#             run('python manage.py %s' % command)


# @task
# def call(command):
#     """
#         Ejecuta un comando de manage.py ejm:
#         $ fab call:"migrate"
#     """

#     with cd(env.directory):
#         with prefix(env.activate):
#             run('python manage.py %s' % command)
