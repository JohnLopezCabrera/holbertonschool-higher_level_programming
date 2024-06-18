-- script that creates table force_name MySQL server.

-- Create the table 'force_name' if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);