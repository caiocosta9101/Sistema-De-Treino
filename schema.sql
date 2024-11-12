-- Criar o banco de dados
CREATE DATABASE 
USE # usar database criada dentro do mysql

-- Tabela de usuários
CREATE TABLE Usuarios (
    idusuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    idade INT NOT NULL
);

-- Tabela de exercícios
CREATE TABLE Exercicios (
    idexercicio INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    grupo_muscular VARCHAR(50) NOT NULL,
    descricao TEXT
);

-- Tabela de periodização
CREATE TABLE Periodizacao (
    idperiodizacao INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

-- Tabela de treinos
CREATE TABLE Treinos (
    idtreino INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_periodizacao INT,
    nome VARCHAR(100) NOT NULL,
    data_criacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(idusuario) ON DELETE CASCADE,
    FOREIGN KEY (id_periodizacao) REFERENCES Periodizacao(idperiodizacao) ON DELETE SET NULL
);

-- Tabela de detalhes do treino
CREATE TABLE TreinoDetalhes (
    idtreinodetalhe INT PRIMARY KEY AUTO_INCREMENT,
    id_treino INT NOT NULL,
    id_exercicio INT NOT NULL,
    series INT NOT NULL,
    repeticoes INT NOT NULL,
    carga FLOAT NOT NULL,
    FOREIGN KEY (id_treino) REFERENCES Treinos(idtreino) ON DELETE CASCADE,
    FOREIGN KEY (id_exercicio) REFERENCES Exercicios(idexercicio)
);

-- Tabela de progresso
CREATE TABLE Progresso (
    idprogresso INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_treino INT NOT NULL,
    id_exercicio INT NOT NULL,
    data DATE NOT NULL,
    serie_progresso INT NOT NULL,
    repeticoes_progresso INT NOT NULL,
    carga_progresso FLOAT NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(idusuario) ON DELETE CASCADE,
    FOREIGN KEY (id_treino) REFERENCES Treinos(idtreino) ON DELETE CASCADE,
    FOREIGN KEY (id_exercicio) REFERENCES Exercicios(idexercicio)
);


-- Inserindo exercícios na tabela Exercicios
INSERT INTO Exercicios (nome, grupo_muscular, descricao)
VALUES
    -- Peitoral
    ('Supino Reto', 'Peitoral', 'Exercício de empurrar com foco no peitoral e tríceps.'),
    ('Supino Inclinado', 'Peitoral', 'Variante do supino que trabalha mais a parte superior do peitoral.'),
    ('Supino Declinado', 'Peitoral', 'Exercício focado na parte inferior do peitoral.'),
    ('Crucifixo', 'Peitoral', 'Exercício de isolamento para o peitoral, realizado com halteres.'),
    ('Crossover', 'Peitoral', 'Exercício para definir o peitoral com cabos.'),
    ('Pullover', 'Peitoral', 'Exercício que trabalha a expansão torácica e o peitoral.'),
    ('Flexão de Braços', 'Peitoral', 'Exercício básico para fortalecer o peitoral e tríceps.'),
    ('Peck Deck', 'Peitoral', 'Máquina para realizar crucifixo de forma guiada.'),
    ('Paralelas', 'Peitoral', 'Exercício de peso corporal para o peitoral e tríceps.'),
    ('Fly Inclinado', 'Peitoral', 'Variante do crucifixo, realizado em banco inclinado.'),
    ('Fly Declinado', 'Peitoral', 'Variante do crucifixo, realizado em banco declinado.'),
    ('Supino com Halteres', 'Peitoral', 'Supino realizado com halteres, aumentando a amplitude de movimento.'),
    ('Supino com Pegada Fechada', 'Peitoral', 'Variante do supino que foca mais nos tríceps e peitoral interno.'),
    ('Flexão com Inclinação', 'Peitoral', 'Flexão de braços com os pés elevados, focando na parte superior do peitoral.'),
    ('Flexão com Declinação', 'Peitoral', 'Flexão de braços com as mãos elevadas, focando na parte inferior do peitoral.'),
    ('Press com Cabo', 'Peitoral', 'Exercício realizado com cabo, simulando o movimento de supino.'),
    ('Press com Máquina', 'Peitoral', 'Exercício realizado em máquina, para maior estabilidade no movimento.'),
    ('Crossover Inclinado', 'Peitoral', 'Crossover realizado com a polia ajustada para pegar mais o peitoral superior.'),
    ('Crossover Declinado', 'Peitoral', 'Crossover realizado com a polia ajustada para pegar mais o peitoral inferior.'),
    ('Peck Deck Unilateral', 'Peitoral', 'Variante do Peck Deck, realizada com um braço de cada vez.'),

    -- Costas
    ('Remada Curvada', 'Costas', 'Exercício para fortalecer a musculatura das costas e bíceps.'),
    ('Remada Unilateral', 'Costas', 'Exercício com halteres, trabalhando uma parte das costas de cada vez.'),
    ('Puxada Frontal', 'Costas', 'Exercício de puxada com foco no latíssimo do dorso.'),
    ('Puxada Triângulo', 'Costas', 'Variante da puxada com pegada neutra para as costas.'),
    ('Levantamento Terra', 'Costas', 'Exercício composto que envolve costas, glúteos e pernas.'),
    ('Remada Alta', 'Costas', 'Exercício que trabalha a parte superior das costas e trapézio.'),
    ('Remada Cavalinho', 'Costas', 'Exercício que foca na parte medial das costas.'),
    ('Pull Over com Barra', 'Costas', 'Exercício que trabalha a expansão torácica e os dorsais.'),
    ('Remada Sentada', 'Costas', 'Exercício realizado com cabo para focar nas costas.'),
    ('Barra Fixa', 'Costas', 'Exercício de peso corporal para as costas e bíceps.'),
    ('Pulldown com Pegada Inversa', 'Costas', 'Variante do pulldown com as palmas viradas para o rosto.'),
    ('Remada Unilateral com Cabo', 'Costas', 'Exercício realizado em máquina, trabalhando um lado de cada vez.'),
    ('Encolhimento com Barra', 'Costas', 'Exercício focado no trapézio.'),
    ('Encolhimento com Halteres', 'Costas', 'Exercício para o trapézio, realizado com halteres.'),
    ('Pullover com Halteres', 'Costas', 'Exercício para trabalhar a musculatura das costas e peito.'),
    ('Remada com Pegada Supinada', 'Costas', 'Variante da remada, com as palmas das mãos voltadas para cima.'),
    ('Remada Cavalinho com Pegada Neutra', 'Costas', 'Variante da remada para trabalhar diferentes ângulos.'),
    ('Levantamento Terra com Barra Hexagonal', 'Costas', 'Variante do levantamento terra para maior segurança na execução.'),
    ('Rack Pull', 'Costas', 'Levantamento parcial para trabalhar a parte superior das costas.'),
    ('Face Pull', 'Costas', 'Exercício para fortalecer os músculos do manguito rotador e trapézio.'),

    -- Pernas
    ('Agachamento Livre', 'Pernas', 'Exercício para desenvolver quadríceps, glúteos e posterior de coxa.'),
    ('Leg Press', 'Pernas', 'Exercício que trabalha principalmente os quadríceps e glúteos.'),
    ('Extensão de Pernas', 'Pernas', 'Exercício isolado para os quadríceps.'),
    ('Flexão de Pernas', 'Pernas', 'Exercício isolado para os isquiotibiais.'),
    ('Panturrilha em Pé', 'Pernas', 'Exercício focado nos músculos da panturrilha.'),
    ('Stiff', 'Pernas', 'Exercício focado nos posteriores de coxa e glúteos.'),
    ('Agachamento Frontal', 'Pernas', 'Variante do agachamento que enfatiza os quadríceps.'),
    ('Hack Machine', 'Pernas', 'Exercício realizado em máquina, focando nos quadríceps e glúteos.'),
    ('Afundo', 'Pernas', 'Exercício unilateral para trabalhar as pernas e glúteos.'),
    ('Cadeira Adutora', 'Pernas', 'Exercício para os músculos adutores.'),
    ('Cadeira Abdutora', 'Pernas', 'Exercício para os músculos abdutores.'),
    ('Avanço', 'Pernas', 'Exercício para trabalhar os músculos das pernas e glúteos.'),
    ('Elevação de Quadril', 'Pernas', 'Exercício para os glúteos e parte inferior das costas.'),
    ('Passada', 'Pernas', 'Exercício que trabalha os músculos das pernas e glúteos em movimento dinâmico.'),
    ('Step Up', 'Pernas', 'Exercício que trabalha os quadríceps e glúteos subindo em uma plataforma.'),
    ('Agachamento Búlgaro', 'Pernas', 'Exercício unilateral para pernas e glúteos.'),
    ('Leg Press Unilateral', 'Pernas', 'Variante do Leg Press para trabalhar uma perna de cada vez.'),
    ('Agachamento Sissy', 'Pernas', 'Exercício avançado para isolar os quadríceps.'),
    ('Panturrilha Sentado', 'Pernas', 'Exercício de panturrilha realizado sentado.'),
    ('Levantamento Terra Romeno', 'Pernas', 'Variante do levantamento terra focado nos isquiotibiais.'),

    -- Ombros
    ('Desenvolvimento com Barra', 'Ombros', 'Exercício para fortalecer os músculos dos ombros.'),
    ('Elevação Lateral', 'Ombros', 'Exercício de isolamento para a porção lateral dos ombros.'),
    ('Elevação Frontal', 'Ombros', 'Exercício para a porção anterior dos ombros.'),
    ('Desenvolvimento Arnold', 'Ombros', 'Variante do desenvolvimento para os ombros inventada por Arnold Schwarzenegger.'),
    ('Crucifixo Invertido', 'Ombros', 'Exercício focado na parte posterior dos ombros.'),
    ('Remada Alta', 'Ombros', 'Exercício para o trapézio e deltoide anterior.'),
    ('Press Militar', 'Ombros', 'Exercício composto para os ombros e tríceps.'),
    ('Desenvolvimento com Halteres', 'Ombros', 'Desenvolvimento de ombro realizado com halteres.'),
    ('Elevação Lateral Inclinada', 'Ombros', 'Variante da elevação lateral para trabalhar diferentes ângulos.'),
    ('Press com Máquina', 'Ombros', 'Exercício para os ombros realizado em máquina para maior estabilidade.'),
    ('Face Pull', 'Ombros', 'Exercício para a parte posterior dos ombros e trapézio.'),
    ('Shrug com Barra', 'Ombros', 'Exercício para trapézio realizado com barra.'),
    ('Shrug com Halteres', 'Ombros', 'Exercício para o trapézio, realizado com halteres.'),
    ('Levantamento Y', 'Ombros', 'Exercício para fortalecer os músculos do manguito rotador.'),
    ('Levantamento Lateral com Cabo', 'Ombros', 'Variante da elevação lateral para isolar melhor os ombros.'),
    ('Desenvolvimento com Pegada Neutra', 'Ombros', 'Exercício para ombros com uma pegada neutra para maior conforto.'),
    ('Press com Pegada Inclinada', 'Ombros', 'Variante do desenvolvimento para trabalhar os ombros com um ângulo diferente.'),
    ('Elevação Frontal com Cabo', 'Ombros', 'Variante da elevação frontal para mais tensão contínua.'),
    ('Levantamento Lateral com Inclinação para Frente', 'Ombros', 'Variante para trabalhar a porção posterior do deltoide.'),
    ('Levantamento Inverso no Pec Deck', 'Ombros', 'Exercício para a parte posterior dos ombros realizado na máquina Pec Deck.');



-- Bíceps
INSERT INTO Exercicios (nome, grupo_muscular, descricao)
VALUES
    ('Rosca Direta', 'Bíceps', 'Exercício básico para o fortalecimento dos bíceps.'),
    ('Rosca Martelo', 'Bíceps', 'Exercício que trabalha a parte lateral do bíceps e o antebraço.'),
    ('Rosca Concentrada', 'Bíceps', 'Exercício de isolamento para o bíceps realizado sentado.'),
    ('Rosca Scott', 'Bíceps', 'Variante da rosca para trabalhar o bíceps de forma concentrada.'),
    ('Rosca Inversa', 'Bíceps', 'Exercício que foca no braquial e nos antebraços.'),
    ('Rosca Alternada com Halteres', 'Bíceps', 'Exercício que alterna os braços para trabalhar os bíceps.'),
    ('Rosca 21', 'Bíceps', 'Exercício composto de 21 repetições divididas em três partes.'),
    ('Rosca no Cabo', 'Bíceps', 'Exercício realizado no cabo para uma tensão contínua nos bíceps.'),
    ('Rosca Concentrada Unilateral', 'Bíceps', 'Variante da rosca concentrada, feita com um braço de cada vez.'),
    ('Rosca Spider', 'Bíceps', 'Exercício de isolamento para os bíceps realizado em banco inclinado.'),
    ('Rosca com Pegada Pronada', 'Bíceps', 'Exercício que trabalha mais o braquial e o antebraço.'),
    ('Rosca com Barra W', 'Bíceps', 'Rosca realizada com barra em formato W para maior conforto nos pulsos.'),
    ('Rosca com Barra Reta', 'Bíceps', 'Rosca realizada com barra reta, trabalhando o bíceps de forma direta.'),
    ('Rosca no Banco Inclinado', 'Bíceps', 'Exercício que isola os bíceps com os braços estendidos.'),
    ('Rosca Concentração com Cabo', 'Bíceps', 'Variante da rosca concentrada usando o cabo.'),
    ('Rosca Martelo Cruzada', 'Bíceps', 'Variante da rosca martelo, onde o halter cruza a linha média do corpo.'),
    ('Rosca Alternada com Rotação', 'Bíceps', 'Rosca realizada com rotação dos punhos para ativar mais o bíceps.'),
    ('Rosca Isométrica', 'Bíceps', 'Exercício onde o bíceps é mantido em contração por um tempo específico.'),
    ('Rosca 45 Graus', 'Bíceps', 'Rosca realizada com o banco inclinado em 45 graus.'),
    ('Rosca com Faixa Elástica', 'Bíceps', 'Variante da rosca utilizando uma faixa elástica para resistência.');

-- Tríceps
INSERT INTO Exercicios (nome, grupo_muscular, descricao)
VALUES
    ('Tríceps Corda', 'Tríceps', 'Exercício realizado no cabo com uma corda, focado na parte lateral do tríceps.'),
    ('Tríceps Francês', 'Tríceps', 'Exercício para alongamento e fortalecimento do tríceps.'),
    ('Tríceps Testa', 'Tríceps', 'Exercício realizado com barra para os tríceps.'),
    ('Mergulho no Banco', 'Tríceps', 'Exercício para trabalhar os tríceps usando o peso do corpo.'),
    ('Tríceps Pulley', 'Tríceps', 'Exercício de empurrar no cabo focado nos tríceps.'),
    ('Tríceps Unilateral', 'Tríceps', 'Exercício realizado com um braço de cada vez.'),
    ('Tríceps na Paralela', 'Tríceps', 'Exercício que usa o peso corporal para trabalhar os tríceps.'),
    ('Tríceps no Banco com Pegada Invertida', 'Tríceps', 'Variante do tríceps no banco, com as palmas das mãos voltadas para cima.'),
    ('Tríceps na Máquina', 'Tríceps', 'Exercício guiado em máquina para os tríceps.'),
    ('Kickback', 'Tríceps', 'Exercício de isolamento para os tríceps realizado com halteres.'),
    ('Tríceps com Pegada Supinada', 'Tríceps', 'Exercício no cabo com a palma da mão voltada para cima.'),
    ('Tríceps com Pegada Pronada', 'Tríceps', 'Exercício no cabo com a palma da mão voltada para baixo.'),
    ('Tríceps com Halteres', 'Tríceps', 'Exercício realizado com halteres, focando nos tríceps.'),
    ('Tríceps Overhead com Corda', 'Tríceps', 'Exercício realizado acima da cabeça com uma corda.'),
    ('Tríceps Overhead com Barra', 'Tríceps', 'Exercício realizado acima da cabeça com uma barra.'),
    ('Tríceps Skull Crusher', 'Tríceps', 'Variante do tríceps testa, realizada em banco inclinado.'),
    ('Tríceps na Barra Fixa', 'Tríceps', 'Exercício que usa a barra fixa para trabalhar os tríceps.'),
    ('Tríceps em Dip Station', 'Tríceps', 'Exercício realizado em uma estação de mergulho.'),
    ('Tríceps no Smith', 'Tríceps', 'Exercício realizado no Smith Machine para maior estabilidade.'),
    ('Tríceps com Faixa Elástica', 'Tríceps', 'Variante do tríceps realizado com uma faixa elástica para resistência.');

-- Abdômen
INSERT INTO Exercicios (nome, grupo_muscular, descricao)
VALUES
    ('Abdominal Supra', 'Abdômen', 'Exercício básico de flexão de tronco para o abdômen.'),
    ('Abdominal Infra', 'Abdômen', 'Exercício focado na parte inferior do abdômen.'),
    ('Abdominal Oblíquo', 'Abdômen', 'Exercício para trabalhar os músculos oblíquos.'),
    ('Prancha', 'Abdômen', 'Exercício isométrico para fortalecimento do core.'),
    ('Elevação de Pernas', 'Abdômen', 'Exercício focado na parte inferior do abdômen, realizado pendurado.'),
    ('Abdominal na Roda', 'Abdômen', 'Exercício para o abdômen realizado com uma roda de abdominais.'),
    ('Abdominal na Cadeira Romana', 'Abdômen', 'Exercício realizado em uma cadeira romana para trabalhar o core.'),
    ('Abdominal com Torção', 'Abdômen', 'Exercício para o abdômen com rotação para envolver os oblíquos.'),
    ('Abdominal V-Up', 'Abdômen', 'Exercício avançado para o abdômen, com levantamento simultâneo de pernas e tronco.'),
    ('Crunch Invertido', 'Abdômen', 'Exercício focado na parte inferior do abdômen.'),
    ('Bicicleta no Solo', 'Abdômen', 'Exercício para o abdômen, simulando o movimento de pedalar.'),
    ('Mountain Climber', 'Abdômen', 'Exercício dinâmico que trabalha o core e o condicionamento cardiovascular.'),
    ('Prancha Lateral', 'Abdômen', 'Variante da prancha para trabalhar os oblíquos e o core.'),
    ('Abdominal Canivete', 'Abdômen', 'Exercício onde as mãos e os pés se encontram no alto.'),
    ('Abdominal na Polia', 'Abdômen', 'Exercício para o abdômen realizado com a polia alta.'),
    ('Abdominal Declinado', 'Abdômen', 'Exercício realizado em banco declinado para maior amplitude.'),
    ('Prancha com Elevação de Braços', 'Abdômen', 'Variante da prancha que adiciona elevações de braços.'),
    ('Rollout com Roda', 'Abdômen', 'Exercício avançado para o core realizado com uma roda de abdominais.'),
    ('Abdominal com Bola Suíça', 'Abdômen', 'Exercício realizado em bola suíça para ativar o core.'),
    ('Abdominal com Kettlebell', 'Abdômen', 'Exercício que envolve o uso de kettlebell para aumentar a intensidade.');




INSERT INTO Periodizacao (nome, descricao)
VALUES
    ('Hipertrofia', 'Foco no aumento do volume muscular, com séries de 8 a 12 repetições.'),
    ('Força', 'Foco no aumento da força máxima, com séries de 1 a 5 repetições e alta carga.'),
    ('Resistência', 'Foco no aumento da resistência muscular, com séries de 15 a 20 repetições e menor carga.');
