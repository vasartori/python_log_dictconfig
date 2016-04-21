import logging


class OutraClasse(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        print(__name__)

    def metodo2(self):
        print('faz nada!')
        self.log.error('ERRO OUTRA CLASSE!!!')
        self.log.info('INFO OUTRA CLASSE!!!')
        self.log.debug('DEBUG OUTRA CLASSE!!!')
        print('fim faz nada')
