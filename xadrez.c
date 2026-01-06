#include <stdio.h>

// ========================================
// FUNÇÕES RECURSIVAS
// ========================================

// Função recursiva para movimentar a Torre para cima
void mover_torre_cima(int casas) {
    if (casas == 0) return;  // Caso base: parar quando não houver mais casas
    printf("Cima\n");
    mover_torre_cima(casas - 1);  // Chamada recursiva
}

// Função recursiva para movimentar o Bispo na diagonal (cima e direita)
void mover_bispo_recursivo(int casas) {
    if (casas == 0) return;  // Caso base
    printf("Cima\n");
    printf("Direita\n");
    mover_bispo_recursivo(casas - 1);  // Chamada recursiva
}

// Função recursiva para movimentar a Rainha para a direita
void mover_rainha_direita(int casas) {
    if (casas == 0) return;  // Caso base
    printf("Direita\n");
    mover_rainha_direita(casas - 1);  // Chamada recursiva
}

// ========================================
// FUNÇÕES COM LOOPS COMPLEXOS
// ========================================

// Função para movimentar o Cavalo em "L" (2 cima, 1 direita) usando loops aninhados
void mover_cavalo() {
    int movimentos_verticais = 2;  // Número de casas para cima
    int movimentos_horizontais = 1;  // Número de casas para a direita

    // Loop externo: controla os movimentos verticais
    for (int i = 0; i < movimentos_verticais; i++) {
        printf("Cima\n");

        // Condição para demonstrar uso de continue
        if (i < movimentos_verticais - 1) {
            continue;  // Pula para a próxima iteração se não for a última
        }

        // Loop interno: controla os movimentos horizontais (executado apenas na última iteração vertical)
        for (int j = 0; j < movimentos_horizontais; j++) {
            printf("Direita\n");

            // Condição para demonstrar uso de break
            if (j == movimentos_horizontais - 1) {
                break;  // Sai do loop interno após o último movimento horizontal
            }
        }
    }
}

// Função para movimentar o Bispo usando loops aninhados (externo vertical, interno horizontal)
void mover_bispo_loops() {
    int casas = 5;  // Número de casas na diagonal

    // Loop externo: controla o movimento vertical
    for (int vertical = 0; vertical < casas; vertical++) {
        printf("Cima\n");

        // Loop interno: controla o movimento horizontal
        for (int horizontal = 0; horizontal < 1; horizontal++) {
            printf("Direita\n");
        }
    }
}

// ========================================
// FUNÇÃO PRINCIPAL
// ========================================

int main() {
    // Definição das constantes para número de casas
    const int CASAS_TORRE = 5;
    const int CASAS_BISPO_RECURSIVO = 5;
    const int CASAS_RAINHA = 8;

    // ========================================
    // TORRE - Movimento recursivo
    // ========================================
    printf("Torre:\n");
    mover_torre_cima(CASAS_TORRE);
    printf("\n");  // Linha em branco para separar

    // ========================================
    // BISPO - Movimento recursivo
    // ========================================
    printf("Bispo (Recursivo):\n");
    mover_bispo_recursivo(CASAS_BISPO_RECURSIVO);
    printf("\n");  // Linha em branco para separar

    // ========================================
    // BISPO - Movimento com loops aninhados
    // ========================================
    printf("Bispo (Loops Aninhados):\n");
    mover_bispo_loops();
    printf("\n");  // Linha em branco para separar

    // ========================================
    // RAINHA - Movimento recursivo
    // ========================================
    printf("Rainha:\n");
    mover_rainha_direita(CASAS_RAINHA);
    printf("\n");  // Linha em branco para separar

    // ========================================
    // CAVALO - Movimento com loops complexos
    // ========================================
    printf("Cavalo:\n");
    mover_cavalo();
    printf("\n");  // Linha em branco para separar

    return 0;
}
