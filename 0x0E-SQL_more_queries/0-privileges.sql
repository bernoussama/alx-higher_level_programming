-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

SELECT * FROM mysql.user WHERE `user` LIKE 'user_0d_%';

