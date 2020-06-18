# Sequential Social Dilemma Environments for OpenAI GYM
Reproduction of https://github.com/eugenevinitsky/sequential_social_dilemma_games in fully OpenAI GYM


Basic environment description:
- Agentes recebem 1 de recompensa a cada maça coletada
	- Agentes podem atacar os outros com um raio que custa -1 de recompensa e causa a todos os agentes que receberem o tiro -50 de recompensa. O tiro vai em uma direção específica até o fim do mapa.
	- Maçãs aparecem a um ritmo proporcional ao número atual de maçãs. Ela é 0 para nenhuma maçã ao redor, 0.005 pra uma maçã ao redor, 0.02 pra duas maçãs ao redor e 0.05 para três maçãs ao redor. Mais maçãs não aumentam a probabilidade.
	- Campo é 38x16
	- O agente pode mover para qualquer direção
	- O agente pode ficar parado
	- O agente pode girar horário ou anti-horário. As direções possíveis são cima, baixo, esquerda, direita.
	- Agentes não podem ocupar o mesmo espaço
Agentes não podem ocupar paredes