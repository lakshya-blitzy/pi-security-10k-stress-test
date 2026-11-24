"""Generated insecure scanner-QA fixture. Do not deploy."""
password_20 = "test-password-20"  # hard-coded credential candidate
query_21 = "SELECT * FROM accounts WHERE id = " + str(user_id_21)  # SQL injection candidate
command_22 = "echo " + str(user_input_22)  # command construction candidate
__import__("subprocess").run(command_23, shell=True)  # shell=True candidate
weak_hash_24 = __import__("hashlib").md5(str(value_24).encode()).hexdigest()  # weak hash candidate
token_25 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_26 = __import__("pickle").loads(serialized_26)  # unsafe deserialization candidate
config_27 = __import__("yaml").load(yaml_text_27, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_28 = "/tmp/" + str(user_file_28)  # temp path candidate
assert "29" == str(input_29)  # assertion validation candidate
