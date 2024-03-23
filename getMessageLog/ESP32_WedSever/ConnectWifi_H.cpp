#include "ConnectWifi_H.h"

#include <Arduino.h>
#include <WiFi.h>
#include <rtc_wdt.h>

void ConnectWifiESP32(const char *WIFI_SSID, const char *WIFI_PASSWORD)
{ 
    // Feed RTC Watchdog để ngăn chặn việc thiết bị bị khởi động lại
    rtc_wdt_feed();

    byte tryCount = 0;

    // Kết nối tới mạng WiFi
    WiFi.disconnect();
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    Serial.print(F("Đang kết nối tới Wifi"));
    while (WiFi.status() != WL_CONNECTED && tryCount <= 10)
    {
        delay(300); // Sử dụng hàm delay của FreeRTOS
        Serial.print(".");

        tryCount++;

        if (tryCount >= 10)
        {
            reconnectWifiESP32(true);
            break; // Thoát vòng lặp nếu đã thử quá 100 lần
        }
    }

    if (WiFi.status() == WL_CONNECTED)
    {
        Serial.print(F("\nĐã kết nối PI: "));
        Serial.print(WiFi.localIP());
        Serial.println();
        Serial.print(F("RSSI: "));
        Serial.println(WiFi.RSSI());
    }
    vTaskDelay(1000);
}

void reconnectWifiESP32(bool resetESP32)
{
    // Feed RTC Watchdog để ngăn chặn việc thiết bị bị khởi động lại
    rtc_wdt_feed();

    byte tryCount = 0;

    while (tryCount <= 5)
    {
        if (tryCount >= 5 || resetESP32)
        {
            ESP.restart(); // Khởi động lại ESP32 nếu cần
        }

        Serial.println("Reconnecting to WiFi...");
        WiFi.disconnect();
        WiFi.reconnect();
        tryCount++;
        delay(1000);
    }
}
