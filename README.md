# Order-Module
# Proje Kurulum Kılavuzu / Project Setup Guide

Bu döküman, projenin nasıl kurulacağı ve çalıştırılacağı hakkında talimatlar sağlar.

This document provides instructions on how to set up and run the project.

---

## Gereksinimler / Prerequisites

Aşağıdaki yazılımların kurulu olduğundan emin olun:
Make sure you have the following installed:

- Docker
- Docker Compose
- Make (isteğe bağlı, ancak önerilir / optional, but recommended)

---

## Projeyi Derleme ve Çalıştırma / Build and Run the Project

Projeyi derlemek ve çalıştırmak için, `docker-compose` komutunu doğrudan kullanabilir veya `Makefile`'dan yararlanabilirsiniz.

To build and run the project, you can either use `docker-compose` directly or leverage the `Makefile`.

### Docker Compose Kullanarak / Using Docker Compose

Container'ları oluşturmak ve çalıştırmak için şu komutu kullanın:
You can build and run the containers using the following command:

```bash
docker-compose up -d --build
```

### Makefile Kullanarak / Using Makefile

Eğer `Makefile` kullanmayı tercih ederseniz, aşağıdaki komutu çalıştırabilirsiniz:
If you prefer using `Makefile`, you can run the following command:

```bash
make build
```

---

## Veritabanı Göç İşlemleri / Database Migrations

Container'lar kurulduktan sonra, veritabanı göç işlemlerini yapmanız gerekir. `docker exec` komutlarını doğrudan çalıştırabilir veya işlemleri kolaylaştırmak için `Makefile` kullanabilirsiniz.

After setting up the containers, you will need to run the database migrations. You have two options: running the commands directly using `docker exec` or using the Makefile for convenience.

### Seçenek 1: Docker Exec Kullanarak / Option 1: Using Docker Exec

Veritabanı migrations işlemlerini uygulamak için sırasıyla şu komutları çalıştırın:
Run the following commands in sequence to apply the database migrations:

```bash
docker exec -it case_order_module alembic upgrade head
docker exec -it case_order_module alembic revision --autogenerate
docker exec -it case_order_module alembic upgrade head
```

### Seçenek 2: Makefile Kullanarak / Option 2: Using Makefile

Alternatif olarak, tek bir komutla migrations işlemlerini uygulayabilirsiniz:
Alternatively, you can apply the migrations with a single command:

```bash
make migrate_fresh
```

---

## Diğer Komutlar / Additional Commands

Diğer komutlar için `Makefile`'a göz atabilirsiniz. İş akışınızı kolaylaştırabilecek çeşitli hedefler içerir.

For more commands, you can refer to the `Makefile`. It contains various targets that may help streamline your workflow.

```bash
cat Makefile
```

---

## Notlar / Notes

- Docker ortamınızın düzgün bir şekilde yapılandırıldığından emin olun.
- Herhangi bir sorunla karşılaşırsanız, `docker logs case_order_module` komutunu kullanarak logları kontrol edebilirsiniz.

Make sure that your Docker environment is correctly configured.
If you encounter any issues, feel free to check the logs using `docker logs case_order_module`.

- Invoice-Module reposu bu projeye dahildir onuda indirmeyi unutmayın!
- Don't forget to also clone/download the invoice module repository.


## env ayarları / env settings (local)
DB_USER=root
DB_PASS=password
DB_HOST=case_order_db
DB_PORT=3306
DB_NAME=order_module_db
