-- init_script.sql
-- DROP TABLE IF EXISTS users;

-- Change password of a role
ALTER ROLE postgres WITH PASSWORD 'postgres_password';

-- Create the 'users' table
CREATE TABLE users (
    username VARCHAR PRIMARY KEY,
    hashed_password VARCHAR,
    api_key VARCHAR UNIQUE
);

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE users TO postgres;