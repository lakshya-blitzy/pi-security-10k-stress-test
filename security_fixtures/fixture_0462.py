"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4620 = "test-password-4620"  # hard-coded credential candidate
query_4621 = "SELECT * FROM accounts WHERE id = " + str(user_id_4621)  # SQL injection candidate
command_4622 = "echo " + str(user_input_4622)  # command construction candidate
__import__("subprocess").run(command_4623, shell=True)  # shell=True candidate
weak_hash_4624 = __import__("hashlib").md5(str(value_4624).encode()).hexdigest()  # weak hash candidate
token_4625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4626 = __import__("pickle").loads(serialized_4626)  # unsafe deserialization candidate
config_4627 = __import__("yaml").load(yaml_text_4627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4628 = "/tmp/" + str(user_file_4628)  # temp path candidate
assert "4629" == str(input_4629)  # assertion validation candidate
