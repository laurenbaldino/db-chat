INSERT INTO users(email, username, created_on, changed_on, change_end) VALUES
    ('abbott@gmail.com','Abbott', '1900-01-01', NULL, NULL),
    ('costello@gmail.com','Costello', '1900-01-01', NULL, NULL),
    ('moe.gmail.com','Moe', '1990-01-01', NULL, NULL),
    ('larry@gmail.com', 'Larry', '1900-01-01', NULL, NULL),
    ('curly@gmail.com','Curly', '1990-01-01', NULL, NULL),
    ('spicelover@gmail.com', 'spicelover', '1990-10-10', NULL, NULL),
    ('paul@gmail.com', 'Paul', '1990-12-14',NULL, NULL)
;

INSERT INTO messages(sender_id, reciever_id, message, sent_on, is_read) VALUES
('3', '4', 'Hey Larry', '1995-02-05', TRUE),
('4', '3', 'Hey Moe', '1995-02-05', TRUE),
('3', '4', 'What kind of pizza do you want', '1995-02-05', TRUE),
('4', '3', 'Pepperoni is that ok with you', '1995-02-05', TRUE),
('3', '4', 'Yeah sounds good I can pick it up on my way', '1995-02-05', TRUE),
('4', '3', 'Okay thanks', '1995-02-05', TRUE),
('3', '4', 'Hi I am here', '1995-06-20', TRUE),
('4', '3', 'Ok come in', '1995-06-20', FALSE),
('3', '4', 'Why arent you answering me', '1995-11-30', FALSE),
('1', '2', 'Hey Costello', '1969-12-14', TRUE),
('2', '1', 'Hey Abbott', '1969-12-15', TRUE),
('1', '2', 'Do we have homework this weekend', '1969-12-15', TRUE),
('2', '1', 'No', '1969-12-15', TRUE),
('5', '1', 'Want to go to the mall','1923-05-01', FALSE),
('3', '7', 'Hey Paul', '1999-09-09', TRUE),
('7', '3', 'Hey Moe', '1999-09-09', TRUE),
('3', '7', 'Reply please', '1999-09-09', TRUE),
('7', '3', 'I replied already', '1999-09-09', TRUE)
;

INSERT INTO communities(name) VALUES
('Arrakis'),
('Comedy')
;

INSERT INTO channels(name, community_id) VALUES
('#Worms', '1'),
('#Random', '1'),
('#ArgumentClinic', '2'),
('#Dialogs', '2')
;

INSERT INTO users_to_communities(user_id, community_id) VALUES
('1','2'),
('2', '2'),
('3', '2'),
('4', '2'),
('5', '2'),
('6', '1'),
('6', '2'),
('7', '2')
;

INSERT INTO suspended_users(user_id, community_id, suspension_end) VALUES
('4', '1', '2012-05-04'),
('7', '1', '2020-2-20')
;
