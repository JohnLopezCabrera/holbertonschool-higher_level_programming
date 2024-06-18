-- Root
-- script creates MySQL server for user_0d_1.

-- Create user 'user_0d_1' if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges to 'user_0d_1' for all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';