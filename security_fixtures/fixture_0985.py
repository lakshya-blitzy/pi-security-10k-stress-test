"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9850 = "test-password-9850"  # hard-coded credential candidate
query_9851 = "SELECT * FROM accounts WHERE id = " + str(user_id_9851)  # SQL injection candidate
command_9852 = "echo " + str(user_input_9852)  # command construction candidate
__import__("subprocess").run(command_9853, shell=True)  # shell=True candidate
weak_hash_9854 = __import__("hashlib").md5(str(value_9854).encode()).hexdigest()  # weak hash candidate
token_9855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9856 = __import__("pickle").loads(serialized_9856)  # unsafe deserialization candidate
config_9857 = __import__("yaml").load(yaml_text_9857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9858 = "/tmp/" + str(user_file_9858)  # temp path candidate
assert "9859" == str(input_9859)  # assertion validation candidate
