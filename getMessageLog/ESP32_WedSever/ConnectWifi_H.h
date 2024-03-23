#ifndef ConnectWifi_H
#define ConnectWifi_H

#include <Arduino.h>
#include <WiFi.h>

void ConnectWifiESP32(const char* WIFI_SSID, const char* WIFI_PASSWORD);
void reconnectWifiESP32(bool resetESP32); // Khai báo hàm reconnectWifiESP32

#endif
