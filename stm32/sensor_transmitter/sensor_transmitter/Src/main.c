/* USER CODE BEGIN Includes */
#include <stdio.h>
#include <string.h>
/* USER CODE END Includes */

/* USER CODE BEGIN PV */
uint8_t rx_byte;
char tx_buf[64];
uint32_t counter = 0;
/* USER CODE END PV */

/* USER CODE BEGIN 0 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
  if (huart->Instance == USART1)
  {
    HAL_UART_Transmit(&huart1, &rx_byte, 1, 10);

    HAL_UART_Receive_IT(&huart1, &rx_byte, 1);
  }
}
/* USER CODE END 0 */

int main(void)
{
  // ... HAL_Init(), SystemClock_Config(), MX_GPIO_Init(), MX_USART1_UART_Init() ...

  /* USER CODE BEGIN 2 */
  HAL_UART_Receive_IT(&huart1, &rx_byte, 1);

  char *msg = "Will Conners BBL\r\n";
  HAL_UART_Transmit(&huart1, (uint8_t*)msg, strlen(msg), 100);
  /* USER CODE END 2 */

  while (1)
  {
    /* USER CODE BEGIN 3 */
    sprintf(tx_buf, "STM32 counter: %lu\r\n", counter++);
    HAL_UART_Transmit(&huart1, (uint8_t*)tx_buf, strlen(tx_buf), 100);

    HAL_Delay(1000);
    /* USER CODE END 3 */
  }
}
