TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER assign_staff_after_order_insert\nAFTER INSERT ON order_table\nFOR EACH ROW\nBEGIN\n    DECLARE staff_id INT;\n\n    \n    SELECT Staff_id INTO staff_id\n    FROM Staff\n    ORDER BY RAND()\n    LIMIT 1;\n\n    \n    IF staff_id IS NOT NULL THEN\n        \n        INSERT INTO Order_assigned_to (Order_id, Staff_id)\n        VALUES (NEW.Order_id, staff_id);\n    END IF;\nEND' 'CREATE DEFINER=`root`@`localhost` TRIGGER `reduce_price_after_order_insert` AFTER INSERT ON `order_table` FOR EACH ROW BEGIN\n    DECLARE item_price DECIMAL(10, 2);\n    \n    \n    SELECT Price INTO item_price\n    FROM Item\n    WHERE Item_id = NEW.Item_id;\n    \n    \n    IF item_price > 1 THEN\n        UPDATE Item\n        SET Price = Price + 1\n        WHERE Item_id = NEW.Item_id;\n    END IF;\nEND'
sql_modes=1411383296 1411383296
definers='root@localhost' 'root@localhost'
client_cs_names='utf8mb4' 'utf8mb4'
connection_cl_names='utf8mb4_general_ci' 'utf8mb4_general_ci'
db_cl_names='utf8mb4_general_ci' 'utf8mb4_general_ci'
created=1713422900435474 1713423642720806
