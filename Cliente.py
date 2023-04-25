class Cliente:
    
    def __init__ (self, idCliente, nomeCliente, senhaCliente, enderecoCliente, emailCliente):
        self._idCliente = idCliente
        self._nomeCliente = nomeCliente
        self._senhaCliente = senhaCliente
        self.enderecoCliente = enderecoCliente
        self._emailCliente = emailCliente
