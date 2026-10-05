# Sistema de Cadastramento de Alunos de Artes Marciais
Um script interativo em Python via terminal desenvolvido para gerenciar o processo de matrícula, seleção de modalidades/faixas, compra de vestuário e checkout de pagamentos para uma academia de artes marciais.

📌 Funcionalidades
Cadastro Inteligente: Captura dados cadastrais do aluno e calcula a idade exata com base na data de nascimento.

Validação de Menores: Solicita dados do responsável legal caso o aluno seja menor de 18 anos (com opção de incluir até 2 responsáveis).

Validação de Dados: Loop de validação para Telefone (11 dígitos), CEP (8 dígitos), Cartão de Crédito (16 dígitos) e CVV (3 dígitos).

Gestão de Modalidades: Suporte a Jiu-Jitsu, Luta Livre Esportiva e Muay-Thai, ajustando dinamicamente o menu de faixas/tarjas conforme a idade do aluno.

Venda de Equipamentos: Opção de compra de trajes para iniciantes (Kimono, Faixa, Resguarde, Short, Tarja) com cálculo de valor final em tempo real.

Módulo de Pagamento: Suporte a PIX e Cartão (Débito e Crédito parcelado em até 3x).

🛠️ Tecnologias e Bibliotecas
Python 3.x

datetime (Nativa) - Manipulação e cálculo de datas.

time (Nativa) - Controle de pausas (sleep) na interface do terminal.

emoji (Externa) - Exibição de emojis no final do atendimento.