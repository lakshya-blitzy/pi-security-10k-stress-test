"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9650 = "test-password-9650"  # hard-coded credential candidate
query_9651 = "SELECT * FROM accounts WHERE id = " + str(user_id_9651)  # SQL injection candidate
command_9652 = "echo " + str(user_input_9652)  # command construction candidate
__import__("subprocess").run(command_9653, shell=True)  # shell=True candidate
weak_hash_9654 = __import__("hashlib").md5(str(value_9654).encode()).hexdigest()  # weak hash candidate
token_9655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9656 = __import__("pickle").loads(serialized_9656)  # unsafe deserialization candidate
config_9657 = __import__("yaml").load(yaml_text_9657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9658 = "/tmp/" + str(user_file_9658)  # temp path candidate
assert "9659" == str(input_9659)  # assertion validation candidate
