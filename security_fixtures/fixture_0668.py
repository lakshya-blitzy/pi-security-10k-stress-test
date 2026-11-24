"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6680 = "test-password-6680"  # hard-coded credential candidate
query_6681 = "SELECT * FROM accounts WHERE id = " + str(user_id_6681)  # SQL injection candidate
command_6682 = "echo " + str(user_input_6682)  # command construction candidate
__import__("subprocess").run(command_6683, shell=True)  # shell=True candidate
weak_hash_6684 = __import__("hashlib").md5(str(value_6684).encode()).hexdigest()  # weak hash candidate
token_6685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6686 = __import__("pickle").loads(serialized_6686)  # unsafe deserialization candidate
config_6687 = __import__("yaml").load(yaml_text_6687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6688 = "/tmp/" + str(user_file_6688)  # temp path candidate
assert "6689" == str(input_6689)  # assertion validation candidate
