CREATE TABLE IF NOT EXISTS subscriber(subscriber_id INT PRIMARY KEY, subscriber_name TEXT,
  creation_timestamp INT DEFAULT UNIX_TIMESTAMP());

CREATE TABLE IF NOT EXISTS inspiration(inspiration_id INT AUTO_INCREMENT, 
subscriber_id INT, -- In case the inspiration is specific to a certain user, this will be non null
text TEXT, creation_timestamp INT DEFAULT UNIX_TIMESTAMP(),
PRIMARY KEY(inspiration_id),
FOREIGN KEY(subscriber_id) REFERENCES subscriber(subscriber_id) ON DELETE CASCADE); -- If a subscriber is deleted, their custom inspirations will be deleted


-- period is a byte representing the period(s), during which the subscriber wants to be inspired. It is calculated by 
-- adding the the numbers equivalent to subscriber's selected period
-- 0 = None, 1 = Morning, 2 = Mid-day, 3 = Night, 
-- So, 1 means they want only morning inspiration, while 6 means they want it all!

CREATE TABLE IF NOT EXISTS schedule(schedule_id INT AUTO_INCREMENT, period BYTE,
PRIMARY KEY(schedule_id) );