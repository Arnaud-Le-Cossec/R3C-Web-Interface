#!/bin/bash

# Database backup tool
# Version 1.0 - 14/02/2024
# By Arnaud LE COSSEC

# Fetching backup
echo "Fetching backup..."
docker exec -it postgresr3c sh -c "pg_dump -U postgres r3c_database > r3c-database_backup.sql"

# Copy backup
filename=$(date +"%d-%m-%Y_%X"_r3c-database-backup_backup.sql)
echo Backup archived at archive/$filename
cp current_backup.sql archive/$filename

# Empty current_backup as it holds sensible data
: > current_backup.sql

# Change file permissions
chmod +r archive/$filename

echo "done"
