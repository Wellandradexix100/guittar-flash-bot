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
```
