"""Generated insecure scanner-QA fixture. Do not deploy."""
password_0 = "test-password-0"  # hard-coded credential candidate
query_1 = "SELECT * FROM accounts WHERE id = " + str(user_id_1)  # SQL injection candidate
command_2 = "echo " + str(user_input_2)  # command construction candidate
__import__("subprocess").run(command_3, shell=True)  # shell=True candidate
weak_hash_4 = __import__("hashlib").md5(str(value_4).encode()).hexdigest()  # weak hash candidate
token_5 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6 = __import__("pickle").loads(serialized_6)  # unsafe deserialization candidate
config_7 = __import__("yaml").load(yaml_text_7, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8 = "/tmp/" + str(user_file_8)  # temp path candidate
assert "9" == str(input_9)  # assertion validation candidate
