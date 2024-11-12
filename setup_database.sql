-- Drop database if exists (be careful with this in production!)
DROP DATABASE IF EXISTS restaurant_offers;
DROP USER IF EXISTS restaurant_user;

-- Create database and user
CREATE USER restaurant_user WITH PASSWORD '123456';
CREATE DATABASE restaurant_offers WITH OWNER restaurant_user;

-- Connect to the database
\c restaurant_offers;

-- Create required extensions
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Grant privileges
ALTER ROLE restaurant_user SET client_encoding TO 'utf8';
ALTER ROLE restaurant_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE restaurant_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE restaurant_offers TO restaurant_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO restaurant_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO restaurant_user; 