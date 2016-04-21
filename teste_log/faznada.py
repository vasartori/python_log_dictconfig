import logging


class FazNada(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        print(__name__)

    def metodo1(self):
        print('faz nada!')
        self.log.error('ERRO no FAZ NADA!!!')
        self.log.info('INFO FAZ NADA!!!')
        self.log.debug('DEBUG FAZ NADA!!!')
        print('fim faz nada')
