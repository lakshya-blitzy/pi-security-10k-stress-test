"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8620 = "test-password-8620"  # hard-coded credential candidate
query_8621 = "SELECT * FROM accounts WHERE id = " + str(user_id_8621)  # SQL injection candidate
command_8622 = "echo " + str(user_input_8622)  # command construction candidate
__import__("subprocess").run(command_8623, shell=True)  # shell=True candidate
weak_hash_8624 = __import__("hashlib").md5(str(value_8624).encode()).hexdigest()  # weak hash candidate
token_8625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8626 = __import__("pickle").loads(serialized_8626)  # unsafe deserialization candidate
config_8627 = __import__("yaml").load(yaml_text_8627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8628 = "/tmp/" + str(user_file_8628)  # temp path candidate
assert "8629" == str(input_8629)  # assertion validation candidate
