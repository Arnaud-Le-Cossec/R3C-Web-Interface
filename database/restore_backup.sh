#!/bin/bash

# Database backup restoration tool
# Version 1.0 - 14/02/2024
# By Arnaud LE COSSEC

# Argument 1 is backup filename

# Copy backup to current_backup
echo Sourcing backup file $1
cp $1 current_backup.sql

# Restore backup
echo "Fetching backup..."
docker exec -it postgresr3c sh -c "psql -U postgres r3c_database < r3c-database_backup.sql"

# Empty current_backup as it holds sensible data
: > current_backup.sql

echo "done"
