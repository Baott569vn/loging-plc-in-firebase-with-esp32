#include <Arduino.h>
#include <WiFi.h>
#include <WebSocketsServer.h>
#include <FirebaseESP32.h>
#include "ConnectWifi_H.h"

#include <rtc_wdt.h>

#define WIFI_SSID "Gia Bao"
#define WIFI_PASSWORD "b@o1231234"

/* 2. Define the API Key */
#define API_KEY "AIzaSyCd1rYV9pdI3dmVrvs3kS-daRatn9QTnXI"

/* 3. Define the RTDB URL */
#define DATABASE_URL "https://database-loging-tpk-default-rtdb.asia-southeast1.firebasedatabase.app/" //<databaseName>.firebaseio.com or <databaseName>.<region>.firebasedatabase.app

/* 4. Define the user Email and password that alreadey registerd or added in your project */
#define USER_EMAIL "baott569Circuit@gmail.com"
#define USER_PASSWORD "b@unnq tjxg iiye fkyz"

// Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

// wed sever
WebSocketsServer webSocket = WebSocketsServer(81); // Khởi tạo WebSocket server ở cổng 81

void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length)
{
  // Không cần thực hiện gì khi có kết nối mới hoặc ngắt kết nối
}

void setup()
{
  Serial.begin(115200);

  rtc_wdt_protect_off();                   // Turns off the automatic wdt service
  rtc_wdt_enable();                        // Turn it on manually
  rtc_wdt_set_time(RTC_WDT_STAGE0, 30000); // Define how long you desire to let dog wait.

  // Kết nối tới mạng WiFi
  ConnectWifiESP32(WIFI_SSID, WIFI_PASSWORD);

  webSocket.begin();                 // Bắt đầu WebSocket server
  webSocket.onEvent(webSocketEvent); // Thiết lập hàm xử lý sự kiện WebSocket
}

void loop()
{
  webSocket.loop(); // Lặp để xử lý các kết nối WebSocket

  // Gửi dữ liệu từ Serial qua WebSocket cho các client kết nối
  if (Serial.available())
  {
    String serialData = Serial.readStringUntil('\n'); // Đọc dữ liệu từ Serial và lưu vào biến serialData
    webSocket.broadcastTXT(serialData);               // Gửi dữ liệu đến tất cả các client kết nối
  }
}
