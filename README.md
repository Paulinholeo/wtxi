<h1>sudo systemctl daemon-reload;sudo systemctl enable wtxi.service</h1>

<h2>Funcionamento:</h2>

A cada 'TEMPO_MAX_TXI' verifica se tx.txi esta alterando;
A cada '11s' verifica TXI pid. Se não estiver rodando, inicia. Verifica bricapd, se não estiver rodando, inicia.
A cada 'TEMPO_MAX_BRICAP' verifica ultimo arquivo da pasta brib. Se não estiver alterando reinicia bricapd. Se reiniciar bricapd 10x, reinicia computador.

