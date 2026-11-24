"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8540 = "test-password-8540"  # hard-coded credential candidate
query_8541 = "SELECT * FROM accounts WHERE id = " + str(user_id_8541)  # SQL injection candidate
command_8542 = "echo " + str(user_input_8542)  # command construction candidate
__import__("subprocess").run(command_8543, shell=True)  # shell=True candidate
weak_hash_8544 = __import__("hashlib").md5(str(value_8544).encode()).hexdigest()  # weak hash candidate
token_8545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8546 = __import__("pickle").loads(serialized_8546)  # unsafe deserialization candidate
config_8547 = __import__("yaml").load(yaml_text_8547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8548 = "/tmp/" + str(user_file_8548)  # temp path candidate
assert "8549" == str(input_8549)  # assertion validation candidate
