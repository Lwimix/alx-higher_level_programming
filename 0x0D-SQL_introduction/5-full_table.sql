-- prints ful description of the table
-- first_table from hbtn_0c_0 database
SELECT column_name, data_type, is_nullable, column_default,
column_key, extra
FROM information_schema.columns
WHERE table_name = 'first_table'
