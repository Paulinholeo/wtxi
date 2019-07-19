<p>sudo systemctl daemon-reload;sudo systemctl enable wtxi.service</p>

<h2>Funcionamento:</h2>

<ul>
	<li>A cada 'TEMPO_MAX_TXI' verifica se tx.txi esta alterando</li>
	<li>A cada '11s' verifica TXI pid. Se não estiver rodando, inicia. Verifica bricapd, se não estiver rodando, inicia.</li>
	<li>A cada 'TEMPO_MAX_BRICAP' verifica ultimo arquivo da pasta brib. Se não estiver alterando reinicia bricapd. Se reiniciar bricapd 10x, reinicia computador.</li>
</ul>

