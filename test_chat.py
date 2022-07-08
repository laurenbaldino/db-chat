import unittest
from src.chat import *
from src.swen344_db_utils import *
from src.users import *
from src.messages import *
from src.communities import *
from src.channels import *
from datetime import date

# datetime for date.today when creating new messages is a WIP still


class TestChat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setupTables()

    def test_gather_messages(self):
        messages = get_messages(sender_id='1', reciever_id='2')
        print(messages)
        self.assertEqual(
            'Hey Costello', messages[0][3], "No messages from Abbott to Costello Found")
        messages = get_messages(sender_id='2', reciever_id='1')
        self.assertEqual(
            'Hey Abbott', messages[0][3], "No messages from Costello to Abbott Found")

#     def test_gather_messages_range(self):
#         messages = get_messages_range(
#             sender_id='3', reciever_id='4', sent_on="1995-01-01")
#         self.assertEqual(
#             'Hey Larry', messages[0][3], "No messages from Moe to Larry in 1995 found")
#         messages = get_messages_range(
#             sender_id='4', reciever_id='3', sent_on="1995-01-01")
#         self.assertEqual(
#             'Hey Moe', messages[0][3], "No messages from Larry to Moe in 1995 found")

#     def test_unread_messages(self):
#         count = get_unread_count_dm(1)
#         self.assertEqual((1,), count, 'No unread messages found')

#     # def test_suspension(self):
#     #     result = get_suspension(user_id='4', community_id='1')
#     #     self.assertEqual(True, result[0], 'Larry is suspended from this community')
#     #     result = get_suspension(user_id='5', community_id='1')
#     #     self.assertEqual(False, result[0], 'Curly is not suspended from this community')

#     def test_add_user(self):
#         result = create_new_user(
#             email='drmarvin@gmail.com', username='Dr.Marvin', created_on='1991-05-16')
#         self.assertEqual(None, result, 'Unable to create user')
#         result = create_new_user(
#             email='bob@gmail.com', username='Bob', created_on='1991-05-17')
#         self.assertEqual(None, result, 'Unable to create user')

#     def test_add_message(self):
#         result = create_new_message(sender_id='7', reciever_id='6',
#                                     message='Im doing the work, Im baby stepping', sent_on='2020-10-10')
#         self.assertEqual(None, result, 'Message not sent')

#     def test_change_username(self):
#         result = change_username(
#             user_id='7', username='BabySteps2Door', change_end='1991-11-19')
#         self.assertEqual(None, result, 'Username cannot be changed')

#     def test_rechange_username(self):
#         result = change_username(
#             username='BabySteps2Elevator', user_id='7',  change_end='1991-05-20')
#         self.assertEqual(None, result, 'Username cannot be changed')

#     def test_mark_read(self):
#         result = mark_read(sender_id='7', reciever_id='6',
#                            message='Im doing the work, Im baby-stepping')
#         self.assertEqual(None, result, 'Message has not been read')

#     def marvin_checks_unread(self):
#         # was unsure if I could call this in test unread count too or not
#         result = get_unread_count_dm(6)
#         self.assertEqual((6,), result, 'No unread messages for Marvin found')

#     def test_join_community(self):
#         result = join_community(user_id='7', community_id='1')
#         self.assertEqual(None, result, 'User is unable to join community')

#     def test_message_count(self):
#         count1 = get_message_count(sender_id='7', reciever_id='3')
#         count2 = get_message_count(sender_id='3', reciever_id='7')
#         result = count1 + count2
#         self.assertEqual((2, 2), result, 'Unable to determine message count')

#     def test_send_channel_message(self):
#         result = insert_channel_message(
#             sender_id='7', channel_id='1', message='Hey Worms', sent_on='2020-10-15', is_read=False)
#         self.assertEqual(None, result, "Unable to send channel message")

#     # def test_mentions(self):
#     #     insert_channel_message(sender_id='7', channel_id='1',message='@spicelover hey', sent_on='2020-02-20', is_read=False)
#     #     result = get_mentions(username='spicelover')
#     #     self.assertEqual('@spicelover hey', result, 'unable to find mentions')
#     #     insert_channel_message(sender_id='3', channel_id='3',message='@spicelover miss you', sent_on='2020-02-20', is_read=False)
#     #     result = get_mentions(username='spicelover')
#     #     self.assertEqual(None, result, 'unable to find mentions')

#     # def test_unread_count_across_communities(self):
#     #     result = get_unread_count_channels(user_id='6', community_id='1')
#     #     self.assertEqual((2,), result, 'no unread channel messages')

#     # def test_stemmed_words(self):
#     #     result = get_stemmed_words(words='reply')
#     #     self.assertEqual("please reply", result[0], "No stemmed words found")
#     #     result = get_stemmed_words(words='reply please')
#     #     self.assertEqual("please reply", result[0], "No stemmed words found")

