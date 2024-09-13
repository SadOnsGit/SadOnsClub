# **SadOnsClub - лучший компьютерный клуб**
[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)
[![Django](https://a11ybadges.com/badge?logo=django)]()
[![PostgreSQL](https://a11ybadges.com/badge?logo=postgresql)]()
[![Docker](https://a11ybadges.com/badge?logo=docker)]()
[![Gunicorn](https://a11ybadges.com/badge?text=Gunicorn&badgeColor=green)]()
[![Nginx](https://a11ybadges.com/badge?text=Nginx&badgeColor=white)]()

---
**SadOnsClub** — идеальное место для отдыха и игр!

## Описание
Данный проект предназначен для коммерческого использования в сфере компьютерных клубов.
Проект написан на Django с использованием веб сервера Nginx, Application Server - Gunicorn, с использованием базы данных PostgreSQL.
Проект предпологает запуск с помощью Docker контейнеров с использованием многоконтейнерного запуска Docker Compose. 
### Какие задачи решает проект?
В первую очередь, проект решает для клиента задачи с удобным предварительным бронированием компьютеров в компьютерных клубах в 1 клик,
а так же автоматизации процессов бронирования на стороне компьютерного клуба для владельца.
Клиенты могут участвовать в системе лояльности(системе бонусов), пополнять личный кабинет.
Все бронирования учитываются в базе данных, что позволяет производить быструю систему расчётов прибыли по взаимодействию с API.

## Установка и запуск

1. Склонируйте этот репозиторий:

   ```bash
   git clone https://github.com/SadOnsGit/SadOnsClub.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd SadOnsClub
   ```
3. Создайте и запустите образы проекта в Docker Compose
   ```dockerfile
   docker compose up
   ```
4. 
