# 🎸 Guitar Flash Bot: Ultimate Performance Edition

Este é um bot de alto desempenho para **Guitar Flash**, desenvolvido em Python com foco em precisão absoluta, imunidade a efeitos de tela (raios/flashes) e detecção inteligente de notas longas.

## 🚀 Funcionalidades Úteis

- **Sistema Look-Ahead (Radar):** Possui dois sensores de captura. O primeiro identifica a nota antecipadamente, preparando o "cérebro" do bot para o que está por vir.
- **Gatilho de Alta Precisão:** Uma rede de captura de 20 pixels de altura que garante que notas rápidas e rastros longos sejam processados sem interrupções.
- **Imunidade a Clarões (Anti-Flash):** Lógica customizada que detecta quando a tela fica branca (raios/especial) e congela o estado das teclas para evitar a perda do combo.
- **Modo Turbo:** Execução otimizada em segundo plano para reduzir a latência de processamento e maximizar os frames por segundo (FPS).
- **Filtro de Faíscas:** Ignora partículas e explosões de notas anteriores para evitar cliques duplos acidentais.

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter o **Python 3.x** instalado em sua máquina.

## 📦 Instalação

Abra o seu terminal e execute o comando abaixo para instalar as dependências necessárias:

```bash
pip install opencv-python numpy mss pynput
🎮 Como Usar
Configuração de Resolução: O código está calibrado para monitores 1919x1079.

Ajuste de Posição: No arquivo guitar.py, as variáveis TELA_TOP e TELA_LEFT definem onde o bot "olha". Ajuste-as conforme a posição da janela do seu jogo.

Execução:

Bash
python guitar.py
Calibração: Para ver o que o bot está enxergando durante o ajuste, mude MOSTRAR_TELA = True no topo do código. Para jogar pra valer, mantenha em False.

🧠 Lógica de Funcionamento
O bot utiliza a biblioteca OpenCV para converter a imagem da tela em valores HSV (Matiz, Saturação e Brilho). Isso permite que ele identifique as cores das notas com precisão, mesmo sob efeitos de luz.

Cores Mapeadas:
Verde, Vermelho, Amarelo, Azul, Laranja: Cores originais do Guitar Flash.

Especial/Star Power: Tons de Azul Ciano/Branco brilhante.

Sombras: Utilizado como recurso de segurança quando a tela está saturada de luz branca.

⚠️ Aviso Legal
Este projeto foi desenvolvido para fins educacionais e de estudo de Visão Computacional. O uso em partidas competitivas pode violar os termos de serviço do jogo.

Desenvolvido com ☕ e Python.