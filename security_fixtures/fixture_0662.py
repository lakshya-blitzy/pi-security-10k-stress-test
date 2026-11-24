"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6620 = "test-password-6620"  # hard-coded credential candidate
query_6621 = "SELECT * FROM accounts WHERE id = " + str(user_id_6621)  # SQL injection candidate
command_6622 = "echo " + str(user_input_6622)  # command construction candidate
__import__("subprocess").run(command_6623, shell=True)  # shell=True candidate
weak_hash_6624 = __import__("hashlib").md5(str(value_6624).encode()).hexdigest()  # weak hash candidate
token_6625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6626 = __import__("pickle").loads(serialized_6626)  # unsafe deserialization candidate
config_6627 = __import__("yaml").load(yaml_text_6627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6628 = "/tmp/" + str(user_file_6628)  # temp path candidate
assert "6629" == str(input_6629)  # assertion validation candidate
