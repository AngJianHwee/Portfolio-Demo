USE project_3000;

insert into food values('dr001','milktea','drink');
insert into food values('dr002','lemon_tea','drink');
insert into food values('dr003','cola','drink');
insert into food values('sn001','sausage','snack');
insert into food values('sn002','French_fries','snack');
insert into food values('nd001','beef_noodle','noodle');
insert into food values('nd002','chicken_noodle','noodle');
insert into food values('nd003','meatball_noodle','noodle');
insert into food values('rc001','chicken_wing_rice','rice');
insert into food values('rc002','fried_rice','rice');
insert into food values('pk001','package_box','package');
insert into food values('pk002','package_bottle','package');

insert into food_price values('dr001',1,20);
insert into food_price values('dr001',2,22);
insert into food_price values('dr002',1,16);
insert into food_price values('dr002',2,18);
insert into food_price values('dr003',1,12);
insert into food_price values('dr003',2,14);
insert into food_price values('sn001',1,8);
insert into food_price values('sn002',1,16);
insert into food_price values('nd001',1,38);
insert into food_price values('nd002',1,36);
insert into food_price values('nd003',1,36);
insert into food_price values('rc001',1,40);
insert into food_price values('rc002',1,33);
insert into food_price values('pk001',1,2);
insert into food_price values('pk002',1,1);

insert into member values('A0001','Ann','2000-01-01','11111111','12345@gmail.com');
insert into member values('A0002','Bob','1999-01-01','13543000000','54321@qq.com');
insert into member values('A0003','Jacky','2003-05-20','63030000','xx000@gmail.com');
insert into member values('A0004','Ms.Wang','1980-01-01',NULL,NULL);
insert into member values('A0005','Mr.Li','1978-12-31','66061234',NULL);
insert into member values('A0006','Jayson','1968-10-01','65432123','bb000@gmail.com');
insert into member values('A0007','Iris','2002-01-01','99998888',NULL);
insert into member values('A0008','Mr.a',NULL,NULL,NULL);
insert into member values('B0001','waiter',NULL,NULL,NULL);
insert into member values('C0001','Walk in guest',NULL,NULL,NULL); 

insert into waiter values('W0001','Amy','2019-01-01',NULL,NULL,'2025550163');
insert into waiter values('W0002','Derek','2019-02-01','2020-2-1',NULL,'00009999');
insert into waiter values('W0003','Zhang','2020-03-01',NULL,NULL,'2025550150');
insert into waiter values('W0004','Kiki','2018-01-01','2019-05-01','1999-01-01','22334455');

insert into payment_method_info values(0,'Unknown');
insert into payment_method_info values(1,'Cash');
insert into payment_method_info values(2,'Card');
insert into payment_method_info values(3,'Wechat');
insert into payment_method_info values(4,'Mpay');
insert into payment_method_info values(5,'Alipay');

insert into order_list values('00001','A0001','W0001','2021-01-01',0);
insert into order_list values('00002','A0002','W0001','2021-01-01',0);
insert into order_list values('00003','A0003','W0002','2021-01-02',1);
insert into order_list values('00004','A0007','W0002','2021-01-02',0);
insert into order_list values('00005','B0001','W0002','2021-01-02',1);
insert into order_list values('00006','C0001','W0003','2021-01-03',0);
insert into order_list values('00007','A0005','W0003','2021-01-03',0);
insert into order_list values('00008','A0006','W0003','2021-01-03',0);
insert into order_list values('00009','A0001','W0003','2021-01-04',0); 
insert into order_list values('00010','B0001','W0003','2021-01-04',1);

insert into order_info values('00001','rc001',1,1);
insert into order_info values('00002','nd002',1,1);
insert into order_info values('00002','sn001',1,1);
insert into order_info values('00003','rc001',1,2);
insert into order_info values('00003','pk001',1,3);
insert into order_info values('00004','dr001',1,1);
insert into order_info values('00004','dr001',2,1);
insert into order_info values('00005','dr002',1,2);
insert into order_info values('00005','pk002',1,2);
insert into order_info values('00006','nd003',1,1);
insert into order_info values('00006','dr002',1,1);
insert into order_info values('00007','nd002',1,1);
insert into order_info values('00007','rc002',1,1);
insert into order_info values('00008','nd001',1,1);
insert into order_info values('00008','sn002',1,1);
insert into order_info values('00009','dr002',1,1);
insert into order_info values('00010','dr001',2,2);
insert into order_info values('00010','pk002',1,2);

insert into payment_method values('00001',2);
insert into payment_method values('00002',1);
insert into payment_method values('00003',1);
insert into payment_method values('00004',5);
insert into payment_method values('00005',4);
insert into payment_method values('00006',1);
insert into payment_method values('00007',1);
insert into payment_method values('00008',1);
insert into payment_method values('00009',5);
insert into payment_method values('00010',4);

insert into discount_rate values('A',0.9);
insert into discount_rate values('B',0.8);
insert into discount_rate values('C',1);