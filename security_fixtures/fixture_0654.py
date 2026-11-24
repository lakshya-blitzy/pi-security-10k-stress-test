"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6540 = "test-password-6540"  # hard-coded credential candidate
query_6541 = "SELECT * FROM accounts WHERE id = " + str(user_id_6541)  # SQL injection candidate
command_6542 = "echo " + str(user_input_6542)  # command construction candidate
__import__("subprocess").run(command_6543, shell=True)  # shell=True candidate
weak_hash_6544 = __import__("hashlib").md5(str(value_6544).encode()).hexdigest()  # weak hash candidate
token_6545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6546 = __import__("pickle").loads(serialized_6546)  # unsafe deserialization candidate
config_6547 = __import__("yaml").load(yaml_text_6547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6548 = "/tmp/" + str(user_file_6548)  # temp path candidate
assert "6549" == str(input_6549)  # assertion validation candidate
